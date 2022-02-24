# Topsis Package (API & CLI)

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/jayantkatia/topsis/Upload%20Python%20Package?style=for-the-badge)
![PyPI](https://img.shields.io/pypi/v/Topsis-Jayant-102097013?color=orange&style=for-the-badge)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/jayantkatia/topsis?style=for-the-badge)
![GitHub](https://img.shields.io/github/license/jayantkatia/topsis?color=informational&style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/jayantkatia/topsis?style=for-the-badge)

Python package that can be used as an API or as a CLI tool to calculate TOPSIS performance score and ranks.

> CLI scripts takes `csv/excel` files as input!

## Installation
```
pip install Topsis-Jayant-102097013
```

## Command Line Usage
```
topsis input_file weights impacts output_file
```
### Arguments
| Arguments | Description |
|------------| -----------------|
| input_file |  "CSV/Excel" file path |
| weights | Comma separated numbers |
| impacts | Comma separated '+' or '-' |
| output_file | Output CSV file path |

### Output
Creates a *output_file*, that contains the original data with performance score and rank.

## API Usage
### Steps
1. Import topsis function from module topsis
2. Invoke topsis function by passing in data, weights, impacts

> Note: Impacts should be a list of -1 and 1. -1 depicting -ve and 1 depicting +ve impact

Example:
```python
from topsis import topsis
import pandas as pd

df = pd.read_csv('data.csv')
weights = [2,2,3,3,4]
impacts=[1,-1,1,-1,1]
print(topsis(df, weights, impacts))
```

## License
Licensed under the [MIT License](https://github.com/jayantkatia/topsis/blob/main/LICENSE). 

## Development and Contributing
Yes, please! Feel free to [contribute, raise issues and recommend best practices.](https://github.com/jayantkatia/topsis/issues)