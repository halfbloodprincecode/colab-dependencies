import os
import sys
import tensorflow as tf  
from tensorflow import keras
from google.colab import drive

def Drive():
  if os.path.isdir('/content/drive'):
    drive.flush_and_unmount()
    drive.mount('/content/drive')
  else:
    drive.mount('/content/drive')

def Sys(paths=[]):
  [sys.path.insert(0, path) for path in paths]
