import tensorflow as tf

class Dataset:
  def __new__(self, preprocessing, classTags, B=32, shuffle=False):
    self.classTags = classTags
    self.B = B
    self.D = []
    dpaths = preprocessing.keys()
    for dpath in dpaths:
      d = tf.data.Dataset.list_files(dpath, shuffle=shuffle)
      d = d.map(preprocessing[dpath]).prefetch(tf.data.AUTOTUNE).cache().batch(self.B)
      self.D.append(d)
    return self.D
  
  @staticmethod
  def sliceFromBatch(Batch, hasLabel=True, Bi=0, Bj=4):
    for i, B in enumerate(Batch):
      if hasLabel:
        return B[0][Bi:Bj, :,:,:]
      else:
        return B[Bi:Bj, :,:,:]
        
