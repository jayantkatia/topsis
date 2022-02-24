"""TOPSIS Package
It could be run using the command line, and can also be used as an API in 
your code.

API USAGE
---------
from topsis import topsis
result = topsis(df, weights, impacts)

# Note(API)
Impacts should be [1,-1,1], ie, 1 for +ve and -1 for -ve

CLI USAGE
---------
topsis input_file_name weights impacts output_file_name

# Note(API)
Impacts should be [+,-,+]
"""

import logging
import sys
import pandas as pd
import numpy as np


## set up logger
def get_logger():
  script_name = sys.argv[0]
  logging.basicConfig(filename='topsis_log.txt', level=logging.WARNING, format='%(asctime)s %(levelname)s ' + script_name + ' %(name)s %(message)s')
  return logging.getLogger(__name__)

def console_success(s): print('✔ ' + s)
def console_error(e): print('✗ Error: ' + str(e) + ', check topsis_log.txt for more details'); exit(-1)


## Read the file and returns df
def get_df(input_file_path):
  ## if excel file then convert and save it to csv
  split_path = input_file_path.split('.')
  extension = split_path[-1].lower()
  if extension == 'xlsx' or extension == 'xls':
    read_file = pd.read_excel(input_file_path)
    input_file_path = f"{''.join(split_path[:-1])}.csv"
    read_file.to_csv(input_file_path, index = None, header=True)

  df = pd.read_csv(input_file_path)
  return df

## Validate data
def validate_data(df, weights, impacts):
  if len(impacts) != len(weights): raise Exception('Number of Weights do not match number of Impacts')
  elif len(df.columns) - 1 != len(weights): raise Exception('Number of cols do not match number of Weights and number of Impacts')
  elif len(df.columns) < 3: raise Exception('Columns less than 3')
  elif len(df.columns) - 1 != len(df.loc[:, df.dtypes <= np.number].columns) : raise Exception('2nd column onwards are not all numeric')
  elif not all(x==1 or x==-1 for x in impacts):
    raise Exception('Impacts, not all values are either 1 or -1') 

## Topsis
def topsis(df, weights, impacts):
  """
  Validates dataframe, impacts, weights and calculates performance score.
  Outputs a dataframe with "Performance Score" and "Rank" column appended.
  """
  
  validate_data(df, weights, impacts)

  ops_df = df.iloc[:,1:]
  ## normalized matrix
  ops_df = ops_df ** 2
  demoninator = np.sqrt(ops_df.sum(axis=0))
  ops_df = ops_df.div(demoninator)

  ## weighted matrix
  ops_df = ops_df.mul(weights)

  ## Separation from ideal solution
  ideal_soln = []
  neg_ideal_soln = []

  for i in range(0, len(impacts)):
    if impacts[i] == 1:
      ideal_soln.append(ops_df.iloc[:,i].max())
      neg_ideal_soln.append(ops_df.iloc[:,i].min())
    else:
      neg_ideal_soln.append(ops_df.iloc[:,i].max())
      ideal_soln.append(ops_df.iloc[:,i].min())
  ideal_soln = ops_df.apply(lambda row: np.sqrt(((row-ideal_soln)**2).sum()) , axis=1)
  neg_ideal_soln = ops_df.apply(lambda row: np.sqrt(((row-neg_ideal_soln)**2).sum()) , axis=1)

  performance_score = neg_ideal_soln / (neg_ideal_soln + ideal_soln)

  ## ans
  df['Topsis Score'] = performance_score
  df['Rank'] = performance_score.rank(ascending=0).astype(int)
  return df

def parse_arguments():
  len_arguments = len(sys.argv)
  if len_arguments != 5:
    raise Exception('Wrong number of arguments')
  
  input_file_path = sys.argv[1]
  weights = sys.argv[2]
  impacts = sys.argv[3]
  output_file_path = sys.argv[4]

  impacts_split = impacts.split(',')
  if not all(x=='-' or x=='+' for x in impacts_split): 
    raise Exception('Not all values are either + or - in Impacts')
  impacts = list(map(lambda x: -1 if x=='-' else 1, [x for x in impacts_split]))  
  weights = list(map(float, weights.split(',')))
  
  return input_file_path, weights, impacts, output_file_path

## Main
def main():
  try:    
    ## logger
    logger = get_logger()
    console_success('Logger Initialized')

    ## parse arguments
    input_file_path, weights, impacts, output_file_path = parse_arguments() 
    console_success('Parsed Arguments')

    ## get df
    df = get_df(input_file_path)
    console_success('Read Input')

    ## validate df and get topsis result
    result = topsis(df, weights, impacts)
    console_success('TOPSIS Calculated')

    ## save results
    result.to_csv(output_file_path, index=0)
    console_success('Output Generated')
    
  except FileNotFoundError as f:
    logger.error(f)
    console_error('input file not found')
  except Exception as e:
    logger.error(e)
    console_error(e)
