import os
import visualkeras
import numpy as np
import matplotlib.pyplot as plt
from tfNormalization import Normalization

class Plotting:
  @staticmethod
  def model(model, name, params):
    if not os.path.exists(f'/content/{params["Net"]}'):
      os.makedirs(f'/content/{params["Net"]}')
    keras.utils.plot_model(model, f'/content/{params["Net"]}/{name}_graph.png', show_shapes=True)
    visualkeras.layered_view(model, to_file=f'/content/{params["Net"]}/{name}_simple3D.png')
    with open(f'/content/{params["Net"]}/{name}_summary.txt', 'w') as fh:
      model.summary(print_fn=lambda x: fh.write(x + '\n'))
  
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
