import numpy as np
import matplotlib.pyplot as plt
from tfNormalization import Normalization

class Plotting:
  @staticmethod
  def subplots(zip, row, col, R=[], figsize=(10, 15)):
    _, ax = plt.subplots(row, col, figsize=figsize)
    for i, samples in enumerate(zip):
      if row>1 and col>1:
        for j in range(col):
          img = samples[j]
          if img.shape[-1] == 1:
            img = img[:, :, 0]
          ax[i, j].imshow(Normalization.denormalize_img(img, R=R[j]))
          ax[i, j].axis('off')
      elif row>1 and col<=1:
        img = samples[0]
        if img.shape[-1] == 1:
          img = img[:, :, 0]
        ax[i].imshow(Normalization.denormalize_img(img, R=R[0]))
        ax[i].axis('off')
      elif row<=1 and col>1:
        for j in range(col):
          img = samples[j]
          if img.shape[-1] == 1:
            img = img[:, :, 0]
          ax[j].imshow(Normalization.denormalize_img(img, R=R[j]))
          ax[j].axis('off')
    plt.show()
