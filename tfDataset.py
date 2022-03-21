import tensorflow as tf

class Dataset:
  def __new__(self, preprocessing, dpaths=[], classTags={}, B=32):
    self.preprocessing = preprocessing
    self.classTags = classTags
    self.B = B
    self.D = []
    for dpath in dpaths:
      d = tf.data.Dataset.list_files(dpath, shuffle=False)
      d = d.shuffle(1000).map(self.preprocessing).prefetch(tf.data.AUTOTUNE).cache().batch(self.B)
      self.D.append(d)
    return self.D
