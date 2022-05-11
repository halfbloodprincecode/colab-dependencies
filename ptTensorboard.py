from torchvision import utils

class Tensorboard:
  def __init__(self, TB):
    self.TB = TB
    
  def Img(self, tag, X):
    self.TB.add_image(tag, utils.make_grid(X))
    self.TB.close()
  
  def Graph(self, model, X):
    self.TB.add_graph(model, X)
    self.TB.close()
  
  def Scalar(self, tag, scalar, step):
    self.TB.add_scalar(tag, scalar, step)
    self.TB.close()
