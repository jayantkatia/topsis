from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(  
  name = 'Topsis-Jayant-102097013',
  packages = ['topsis'],
  version = '1.1.2',
  license='MIT',
  description = 'API and CLI tool to calculate Topsis, CLI tool inputs CSV/Excel files',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Jayant Katia',
  author_email = 'jayantkatia65@gmail.com',
  url = 'https://github.com/jayantkatia/topsis',
  download_url = 'https://github.com/jayantkatia/topsis/archive/refs/tags/v1.1.2.tar.gz',
  keywords = ['topsis', 'python', 'pypi', 'csv', 'xlsx', 'xls', 'cli'],
  install_requires=[
          'numpy',
          'pandas',
      ],
  entry_points={
    'console_scripts': [
      'topsis = topsis.topsis:main'
      ]
  },
)