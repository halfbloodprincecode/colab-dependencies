import tensorflow as tf  
from tensorflow import keras

class Model(keras.Model):
  def __init__(self):
    super(Model, self).__init__()
  
  @staticmethod
  def getCallbacks(params, fit=[], evaluate=[], predict=[], indexing=None):
    cb = {
      'fit': [
        keras.callbacks.BackupAndRestore(backup_dir=f'{params["DIR_ROOT"]}/backup/params["model"]'),
        keras.callbacks.ModelCheckpoint(filepath='{params["DIR_ROOT"]}/experimental/params["model"]/weights/{int(epoch):09d}, {val_loss:.2f}/weights', monitor='val_loss', verbose=0, save_best_only=True, save_weights_only=True, mode='min', save_freq='epoch', options=None, initial_value_threshold=None),
        keras.callbacks.CSVLogger(filename=f'{params["DIR_ROOT"]}/experimental/params["model"]/metrics/fit.csv', separator=',', append=True),
        keras.callbacks.ProgbarLogger(count_mode='steps', stateful_metrics=None),
      ],
      'evaluate': [],
      'predict': []
    }
    if indexing == None:
      cb['fit'].extend(fit)
      cb['evaluate'].extend(evaluate)
      cb['predict'].extend(predict)
    return cb
  

