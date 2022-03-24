import numpy as np
import matplotlib.pyplot as plt
from tfNormalization import Normalization

class Plotting:
  @staticmethod
  def subplots(zip, row=4, col=2, figsize=(10, 15)):
    _, ax = plt.subplots(row, col, figsize=figsize)
    for i, samples in enumerate(zip):
      if col > 1:
        for j in range(col):
          img = samples[j]
          if img.shape[-1] == 1:
            img = img[:, :, 0]
          ax[i, j].imshow(Normalization.denormalize_img(img))
          ax[i, j].axis('off')
      else:
        img = samples[0]
        if img.shape[-1] == 1:
          img = img[:, :, 0]
        ax[i].imshow(Normalization.denormalize_img(img))
        ax[i].axis('off')
    plt.show()
