import os
import sys
import shutil
import pathlib 
import torch
import tensorflow as tf  
import logging as tools_logging
from tensorflow import keras
from google.colab import drive
from argparse import ArgumentParser

index_vars = None
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

class CustomFormatter(tools_logging.Formatter):
  grey = '\x1b[38;20m'
  blue = '\x1b[34;20m'
  yellow = '\x1b[33;20m'
  red = '\x1b[31;20m'
  bold_red = '\x1b[31;1m'
  reset = '\x1b[0m'
  format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)'

  FORMATS = {
    tools_logging.DEBUG: grey + format + reset,
    tools_logging.INFO: blue + format + reset,
    tools_logging.WARNING: yellow + format + reset,
    tools_logging.ERROR: red + format + reset,
    tools_logging.CRITICAL: bold_red + format + reset
  }

  def format(self, record):
    log_fmt = self.FORMATS.get(record.levelno)
    formatter = tools_logging.Formatter(log_fmt)
    return formatter.format(record)

def tools():
  logger = tools_logging.getLogger('logger')
  logger.setLevel(tools_logging.DEBUG)

  # create console handler with a higher log level
  ch = tools_logging.StreamHandler()
  ch.setLevel(tools_logging.DEBUG)
  ch.setFormatter(CustomFormatter())

  logger.addHandler(ch)
  return logger,

logger, = tools()
  
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
  paths.extend([
    index_vars['Environment'],
    index_vars['DIR_ROOT'],
    index_vars['DIR_ROOT'] + '/HTTP',
    index_vars['DIR_ROOT'] + '/Socket',
    index_vars['DIR_ROOT'] + '/Messaging',
    index_vars['DIR_ROOT'] + '/Telegram',
    index_vars['DIR_ROOT'] + '/Instagram',
    index_vars['DIR_ROOT'] + '/ML',
    index_vars['DIR_ROOT'] + '/ML' + '/network',
    index_vars['DIR_ROOT'] + '/ML' + '/model',
    index_vars['DIR_ROOT'] + '/ML' + '/experimental',
    index_vars['DIR_ROOT'] + '/ML' + '/experimental' + '/' + index_vars['Net'],
    index_vars['DIR_ROOT'] + '/ML' + '/experimental' + '/' + index_vars['Net'] + '/tensorboard',
  ])
  for path in paths:
    sys.path.insert(0, path)
    Mkdir(path)

def Kaggle(datasets={}):
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
