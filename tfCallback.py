import os
import datetime
import shutil
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

class Logger(keras.callbacks.Callback):
  def __init__(self, path, parameters):
    self.parameters = parameters
    self.flag = True
    self.df = pd.DataFrame()
    self.path = path
    dirpath = os.sep.join(path.split(os.sep)[:-1])
    self.path_weights = dirpath + '/weights'
    self.path_figure = dirpath + '/figure'
    if not os.path.exists(dirpath):
      os.makedirs(dirpath)
    if not os.path.exists(self.path_weights):
      os.makedirs(self.path_weights)
    if not os.path.exists(self.path_figure):
      os.makedirs(self.path_figure)
    if not os.path.exists('/content/drive/MyDrive/backup'):
      os.makedirs('/content/drive/MyDrive/backup')

  def on_epoch_begin(self, epoch, logs=None):
    if self.flag:
      if epoch == 0:
        self.assume = True
      else:
        self.assume = False
    self.flag = False
    self.df = pd.DataFrame()
    if epoch == 0:
      self.df.to_csv(self.path, mode='w+', index=False, header=False)
      self.bestLoss = float('inf')
    else:
      if self.assume == False:
        E = int(epoch)
        D = pd.read_csv(self.path)
        D = D.iloc[0:E]
        D.to_csv(self.path, mode='w+', index=False, header=True)
        self.bestLoss = D['loss'].min()

  def on_train_batch_end(self, batch, logs=None):
    self.df = self.df.append(logs, ignore_index = True)
  
  def on_test_batch_end(self, batch, logs=None):
    pass
  
  def on_train_end(self, logs=None):
    D = pd.read_csv(self.path)
    Query = D.loc[D['Decrease'] == True]

    plt.plot(list(D['epoch']), list(D['loss']), color='c', label='training loss')
    plt.plot(list(Query['epoch']), list(Query['loss']), '.', color='m', markersize=10, label='optimal point')
    plt.xlabel('epoch')
    plt.ylabel('Loss')
    plt.title(self.parameters['Net'])
    plt.legend()
    plt.savefig(f'{self.path_figure}/training_loss_{str(datetime.datetime.now())}.png')
    plt.show();

  def on_epoch_end(self, epoch, logs=None):
    self.df = self.df.mean(axis=0)
    row = pd.DataFrame().append(self.df.to_dict(), ignore_index=True)
    row.insert(0, 'epoch', int(epoch))
    meanLossInEpoch = row['loss'][0]
    Decrease = meanLossInEpoch < self.bestLoss
    row['Decrease'] = Decrease
    row['datetime'] = str(datetime.datetime.now())
    if epoch == 0:
      row.to_csv(self.path, mode='a', index=False, header=True)
    else:
      row.to_csv(self.path, mode='a', index=False, header=False)

    if Decrease:
      self.bestLoss = meanLossInEpoch
      self.model.save_weights(f'{self.path_weights}/epoch: {str(int(epoch))}, loss: {str(meanLossInEpoch)}/weights')
    
    row = None
    self.df = None
    
    if int(epoch) % 50 == 0 and int(epoch) > 1:
      distpath = f'/content/drive/MyDrive/backup/{self.parameters['Net']}_epoch{str(epoch)}_{str(datetime.datetime.now())}'
      shutil.make_archive(distpath, 'zip', '/content/backup')
