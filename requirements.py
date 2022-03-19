import os
import sys
import shutil
import tensorflow as tf  
from tensorflow import keras
from google.colab import drive

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
    root + '/model',
    root + '/model/layer'
  ])
  [sys.path.insert(0, path) for path in paths]

def Kaggle(root='/'):
  shutil.copy(root + '/kaggle.json', '/content')
