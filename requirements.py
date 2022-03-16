import os
import sys
from google.colab import drive

def Drive():
  if os.path.isdir('/content/drive'):
    drive.flush_and_unmount()
    drive.mount('/content/drive')
  else:
    drive.mount('/content/drive')

def add(paths=[]):
  [sys.path.insert(0, path) for path in paths]
