import os
import visualkeras
import numpy as np
import pandas as pd
import seaborn as sns
from tensorflow import keras
import matplotlib.pyplot as plt
from tfNormalization import Normalization

class Plotting:
  @staticmethod
  def model(model, name, params):
    dirpath = f'/content/{params["Net"]}'
    if not os.path.exists(dirpath):
      os.makedirs(dirpath)
    keras.utils.plot_model(model, f'{dirpath}/{name}_graph.png', show_shapes=True)
    visualkeras.layered_view(model, to_file=f'{dirpath}/{name}_simple3D.png')
    with open(f'{dirpath}/{name}_summary.txt', 'w') as fh:
      model.summary(print_fn=lambda x: fh.write(x + '\n'))
  
  @staticmethod
  def tsne2Dplot(z, y, title='', axis_x='comp-1', axis_y='comp-2'):
    df = pd.DataFrame()
    df['y'] = y
    df['comp-1'] = z[:,0]
    df['comp-2'] = z[:,1]
    C = len(np.unique(y))

    sns.scatterplot(
      x=axis_x, 
      y=axis_y, 
      hue=df.y.tolist(),
      palette=sns.color_palette('hls', C),
      data=df
    ).set(title=title) 
  
  @staticmethod
  def subplots(zip, row, col, R=[], figsize=(10, 15)):
    cmap = 'viridis'
    _, ax = plt.subplots(row, col, figsize=figsize)
    for i, samples in enumerate(zip):
      if row>1 and col>1:
        for j in range(col):
          img = samples[j]
          if img.shape[-1] == 1:
            cmap = 'gray'
            img = img[:, :, 0]
          ax[i, j].imshow(Normalization.denormalize_img(img, R=R[j]), cmap=cmap)
          ax[i, j].axis('off')
      elif row>1 and col<=1:
        img = samples[0]
        if img.shape[-1] == 1:
          cmap = 'gray'
          img = img[:, :, 0]
        ax[i].imshow(Normalization.denormalize_img(img, R=R[0]), cmap=cmap)
        ax[i].axis('off')
      elif row<=1 and col>1:
        for j in range(col):
          img = samples[j]
          if img.shape[-1] == 1:
            cmap = 'gray'
            img = img[:, :, 0]
          ax[j].imshow(Normalization.denormalize_img(img, R=R[j]), cmap=cmap)
          ax[j].axis('off')
    plt.show()
