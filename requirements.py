import os
import sys
from google.colab import drive

def Drive():
  if os.path.isdir('/content/drive'):
    drive.flush_and_unmount()
    drive.mount('/content/drive')
  else:
    drive.mount('/content/drive')

def Sys(paths=[]):
  [sys.path.insert(0, path) for path in paths]

def Callback(params):
  return {
    'fit': [
      keras.callbacks.experimental.BackupAndRestore(backup_dir=f'{params["DIR_ROOT"]}/backup/params["model"]'),
      keras.callbacks.ModelCheckpoint(filepath='{params["DIR_ROOT"]}/experimental/params["model"]/weights/{int(epoch):09d}, {val_loss:.2f}/weights', monitor='val_loss', verbose=0, save_best_only=True, save_weights_only=True, mode='min', save_freq='epoch', options=None, initial_value_threshold=None),
      keras.callbacks.CSVLogger(filename=f'{params["DIR_ROOT"]}/experimental/params["model"]/metrics/fit.csv', separator=',', append=True),
      keras.callbacks.ProgbarLogger(count_mode='steps', stateful_metrics=None),
    ],
    'evaluate': [],
    'predict': []
  }
