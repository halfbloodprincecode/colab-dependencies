import numpy as np
import matplotlib.pyplot as plt
from tfNormalization import Normalization

class Plotting:
  @staticmethod
  def subplots(zip, row=4, col=2, figsize=(10, 15)):
    _, ax = plt.subplots(row, col, figsize=figsize)
    for i, samples in enumerate(zip):
      for j in range(col):
        ax[i, j].imshow(Normalization.denormalize_img(samples[j][i]))
    plt.show()
