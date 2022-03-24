import tensorflow as tf

class Dataset:
  def __new__(self, preprocessing, classTags, B=32, shuffle=[]):
    self.classTags = classTags
    self.B = B
    self.D = []
    dpaths = preprocessing.keys()
    for i, dpath in enumerate(dpaths):
      d = tf.data.Dataset.list_files(dpath, shuffle=shuffle[i])
      d = d.map(preprocessing[dpath]).prefetch(tf.data.AUTOTUNE).cache().batch(self.B)
      self.D.append(d)
    return self.D
  
  @staticmethod
  def sliceFromBatch(Batch, Bi=0, Bj=4):
    L = []
    for i, B in enumerate(Batch):
      for j in range(len(B)):
        L.append(B[j][Bi:Bj, :,:,:])
    return L
