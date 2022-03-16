import os
from google.colab import drive

def Drive():
  if os.path.isdir('/content/drive'):
    drive.flush_and_unmount()
    drive.mount('/content/drive')
    return 0
  else:
    drive.mount('/content/drive')
    return 1
