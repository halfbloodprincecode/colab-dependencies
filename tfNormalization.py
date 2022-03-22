import numpy as np

class Normalization:
  @staticmethod
  def normalize_img(img):
    img = tf.cast(img, dtype=tf.float32)
    # Map values in the range [-1, 1]
    return (img / 127.5) - 1.0
  
  @staticmethod
  def denormalize_img(img):
    return (((img * 127.5) + 127.5).numpy()).astype(np.uint8)
