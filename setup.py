from setuptools import setup

setup(
  name = 'Topsis-Jayant-102097013',
  packages = ['topsis'],
  version = '1.0',
  license='MIT',
  description = 'Topsis Implementation',
  author = 'Jayant Katia',
  author_email = 'jayantkatia65@gmail.com',
  url = 'https://github.com/jayantkatia/topsis',
  download_url = 'https://github.com/jayantkatia/topsis/archive/refs/tags/v1.0.tar.gz',
  keywords = ['topsis', 'python', 'pypi'],
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