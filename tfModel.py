import datetime
import tensorflow as tf  
from tensorflow import keras
from tfCallback import Logger

class Model(keras.Model):
  def __init__(self):
    super(Model, self).__init__()
  
  def getCallbacks(self, params, fit=[], evaluate=[], predict=[], indexing=None):
    cb = {
      'fit': [
        keras.callbacks.BackupAndRestore(backup_dir=f'/content/backup/{params["model"]}'),
        Logger(path=f'{params["DIR_ROOT"]}/experimental/{params["model"]}/fit.csv', parameters=params),
#         keras.callbacks.ModelCheckpoint(filepath=f'{params["DIR_ROOT"]}/experimental/{params["model"]}/weights/'+'epoch: {epoch:02d}, val_loss: {val_loss:.2f}/weights', monitor='val_loss', verbose=0, save_best_only=True, save_weights_only=True, mode='min', save_freq='epoch', options=None, initial_value_threshold=None),
#         keras.callbacks.CSVLogger(filename=params["DIR_ROOT"]+'/experimental/'+params["model"]+'/metrics(fit)_'+str(datetime.datetime.now())+'_.csv', separator=',', append=False),
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
  

