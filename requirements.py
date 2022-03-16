import os
from google.colab import drive

def Drive(path=None):
  if os.path.isdir('/content/drive'):
    drive.flush_and_unmount()
    drive.mount('/content/drive')
  else:
    drive.mount('/content/drive')
  if path:
    %cd {path}
