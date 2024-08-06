from setuptools import setup, find_packages

def read(filename):
  """
  Reads the content of the README.
  """
  with open(filename, 'r') as f:
    return f.read()

setup(
    name="orgfiles",
    version="0.1.0",
    author='Akhilesh Malthi',
    author_email='akhileshmalthi2299@gmail.com',
    packages=find_packages(),
    description="A File Organizer using python",  
    long_description=read('./README.md'),
    long_description_content_type="text/markdown",
    license="MIT",  
    url="https://www.github.com/AkhileshMalthi/Orgfiles",  
    install_requires=[
      'typer',
      'rich'
    ],
    entry_points={
        'console_scripts': [
            'orgfiles = orgfiles.app:app',
        ],
    },
)
