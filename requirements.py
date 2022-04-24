import os
import sys
import shutil
import tensorflow as tf  
from tensorflow import keras
from google.colab import drive
from argparse import ArgumentParser

def Drive():
  if os.path.isdir('/content/drive'):
    drive.flush_and_unmount()
    drive.mount('/content/drive')
  else:
    drive.mount('/content/drive')

def Sys(root='/', paths=[]):
  paths.extend([
    root,
    root + '/network',
    root + '/callback',
    root + '/model',
    root + '/model/layer'
  ])
  [sys.path.insert(0, path) for path in paths]

def Kaggle(root='/', datasets={}):
  shutil.copy(root + '/kaggle.json', '/content')
  shutil.copy('/content/kaggle.json', '/root/.kaggle')
  os.chmod('/root/.kaggle/kaggle.json', 600)
  os.remove('/content/kaggle.json')
  for Dkey in datasets:
    os.system(f'kaggle datasets download -d {datasets[Dkey]} -p /content/datasets/{Dkey}')
    os.system(f'unzip /content/datasets/{Dkey}/*.zip -d /content/datasets/{Dkey}')
    os.system(f'rm -rf /content/datasets/{Dkey}/*.zip')

def parser(NET, *args):
  H = ArgumentParser(NET)
  H.add_argument('-f')
  H.add_argument('--NET', type=str, default=NET)
  for arg in args:
    H.add_argument(arg[0], **arg[1])
  return H.parse_args()
