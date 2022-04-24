import os
import sys
import shutil
import pathlib 
import tensorflow as tf  
from tensorflow import keras
from google.colab import drive
from argparse import ArgumentParser

index_vars = None

def Mkdir(path):
  pathlib.Path(path).mkdir(parents=True, exist_ok=True)

def Rmdir(path):
  shutil.rmtree(path)

def Drive():
  if os.path.isdir('/content/drive'):
    drive.flush_and_unmount()
    drive.mount('/content/drive')
  else:
    drive.mount('/content/drive')

def System(paths=[]):
  print('!!!!!!!!!!!!!!!!!!!',index_vars['DIR_ROOT'])
  root = index_vars['DIR_ROOT']
  paths.extend([
    root,
    root + '/network',
    root + '/callback',
    root + '/model',
    root + '/model/layer'
  ])
  
  for path in paths:
    sys.path.insert(0, path)
    Mkdir(path)

def Kaggle(datasets={}):
  print('@@@@@@@@@@@@@@@',index_vars['DIR_ROOT'])
  root = index_vars['DIR_ROOT']
  shutil.copy(root + '/kaggle.json', '/content')
  shutil.copy('/content/kaggle.json', '/root/.kaggle')
  os.chmod('/root/.kaggle/kaggle.json', 600)
  os.remove('/content/kaggle.json')
  for Dkey in datasets:
    os.system(f'kaggle datasets download -d {datasets[Dkey]} -p /content/datasets/{Dkey}')
    os.system(f'unzip /content/datasets/{Dkey}/*.zip -d /content/datasets/{Dkey}')
    os.system(f'rm -rf /content/datasets/{Dkey}/*.zip')

def Parser(NET, *args):
  H = ArgumentParser(NET)
  H.add_argument('-f')
  H.add_argument('--NET', type=str, default=NET)
  for arg in args:
    H.add_argument(arg[0].upper(), **arg[1])
  return H.parse_args()
