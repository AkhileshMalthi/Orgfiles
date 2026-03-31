# Agent Policy and Operating Scope

**Version:** 1.0  
**Status:** Draft  
**Applies to:** Orgfiles AI Agent (MVP)

---

## 1. Root Directory Boundaries

The agent **must** operate exclusively within a single, explicitly declared working root directory (the *agent root*) that is provided by the user at invocation time or resolved from the current working directory.

| Rule | Detail |
|------|--------|
| All file paths must be absolute descendants of the agent root | Path traversal (`../`) sequences are rejected before any operation executes |
| Symlinks that resolve outside the agent root are treated as out-of-scope and skipped | A warning is emitted for each skipped symlink |
| The agent root itself may not be the filesystem root (`/` or a drive root on Windows) | The user will be prompted to choose a more specific directory |
| Agent state files (e.g., `file_movements.json`) are stored inside the agent root | They are never written to system directories |

---

## 2. Allowed File Operations (MVP)

Only the following operations are permitted in the MVP. Any operation not in this list is **denied by default**.

| Operation | Description |
|-----------|-------------|
| `list` | Enumerate files and directories one level deep (or recursively with a depth cap of **5**) |
| `search` | Find files by name, extension, or keyword — read-only, no mutations |
| `read-snippet` | Read a portion of a file's content (first 200 lines or 10 KB, whichever is smaller) for preview purposes |
| `move` | Relocate a file from one path to another within the agent root; staged before execution |
| `rename` | Rename a file in-place (equivalent to a `move` within the same directory); staged before execution |
| `apply` | Execute all pending staged operations after explicit user confirmation |
| `undo` | Reverse the most recent `apply` batch, restoring files to their pre-apply locations |

**Explicitly prohibited operations (all versions unless upgraded policy is adopted):**

- `delete` / `unlink` — permanent removal of files or directories
- `write` / `overwrite` — modifying file contents
- `chmod` / `chown` — changing file permissions or ownership
- Operations on files outside the agent root

---

## 3. Safety Defaults

| Default | Value | Notes |
|---------|-------|-------|
| Staging required | **Yes** | Every mutating operation (`move`, `rename`) is added to a staging area and does not execute until `apply` is called |
| Delete disabled | **Yes** | `delete` is unconditionally disabled; any code path that would remove a file must raise a policy error |
| Max files per `apply` without re-confirmation | **50** | If a pending batch exceeds 50 files, the user must explicitly confirm a second time before `apply` proceeds |
| Max recursive depth | **5** | `list` and `search` will not descend beyond 5 directory levels |
| Max `read-snippet` size | **10 KB / 200 lines** | Prevents accidental loading of very large binary or text files |
| Undo history retained | **1 batch** | Only the immediately preceding `apply` batch can be undone; older history is not kept in MVP |

---

## 4. Code Enforcement Guardrails

The following guardrails **must** be implemented in code, not just documented as policy:

### 4.1 Path Validation

```python
import pathlib

def assert_within_root(path: str, agent_root: str) -> str:
    """Resolve path and verify it stays inside agent_root. Raise PolicyError otherwise."""
    resolved = pathlib.Path(path).resolve()
    root     = pathlib.Path(agent_root).resolve()
    # is_relative_to() (Python 3.9+) handles cross-platform separator edge cases
    if not resolved.is_relative_to(root):
        raise PolicyError(f"Path '{resolved}' is outside the agent root '{root}'.")
    return str(resolved)
```

Every file argument passed to any operation is run through `assert_within_root` before the operation proceeds.

### 4.2 Operation Allow-list

```python
ALLOWED_OPERATIONS = {"list", "search", "read-snippet", "move", "rename", "apply", "undo"}

def dispatch(operation: str, **kwargs):
    if operation not in ALLOWED_OPERATIONS:
        raise PolicyError(f"Operation '{operation}' is not permitted by agent policy.")
    # ... route to handler
```

### 4.3 Staging Gate

```python
def stage(operation: str, src: str, dst: str, staging_area: list):
    staging_area.append({"op": operation, "src": src, "dst": dst})

def apply(staging_area: list, agent_root: str):
    if len(staging_area) > 50:
        # Case-insensitive comparison; prompt text must make the exact required input clear
        confirm = input(f"Batch contains {len(staging_area)} files. Type 'yes' to continue: ")
        if confirm.strip().lower() != "yes":
            raise PolicyError("Batch apply cancelled by user.")
    for item in staging_area:
        assert_within_root(item["src"], agent_root)
        assert_within_root(item["dst"], agent_root)
        # execute move/rename
```

### 4.4 Delete Guard

```python
def delete(*args, **kwargs):
    raise PolicyError("delete is disabled by agent policy in MVP.")
```

`os.remove`, `os.unlink`, and `shutil.rmtree` must not be called in any code path reachable during normal agent operation.

---

## 5. Policy Violation Handling

- A `PolicyError` (a dedicated exception class, not a generic `Exception`) is raised immediately.
- The error message includes the rule that was violated and the offending path or operation.
- The staging area is **not** cleared on a policy violation; the user can inspect and correct the batch.
- All policy violations are logged to a file named `agent-policy.log` inside the agent root.

---

*This document is the authoritative source of truth for agent behavior in MVP. Changes require a new version number and a PR review.*
