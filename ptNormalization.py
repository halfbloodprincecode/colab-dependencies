import numpy as np

class Normalization:
  @staticmethod
  def normalize_img(img, R): # R: Range
    if R == '-1to1':
      # Map values in the range [-1, 1]
      return (img / 127.5) - 1.0
    elif R == '0to1':
      return (img/255.)
  
  @staticmethod
  def denormalize_img(img, R): # R: Range
    if R == '-1to1':
      return (((img * 127.5) + 127.5).numpy()).astype(np.uint8)
    elif R == '0to1':
      return ((img*255.).numpy()).astype(np.uint8)
