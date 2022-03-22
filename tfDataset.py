import tensorflow as tf

class Dataset:
  def __new__(self, preprocessing, classTags, B=32):
    self.classTags = classTags
    self.B = B
    self.D = []
    dpaths = preprocessing.keys()
    for dpath in dpaths:
      d = tf.data.Dataset.list_files(dpath, shuffle=False)
      d = d.shuffle(1000).map(preprocessing[dpath]).prefetch(tf.data.AUTOTUNE).cache().batch(self.B)
      self.D.append(d)
    return self.D
  
  @staticmethod
  def sliceFromBatch(Batch, Bi=0, Bj=4):
    B = None
    for batch in Batch:
      B = batch[0][Bi:Bj, :,:,:]
    return B
