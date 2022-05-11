from torchvision import utils

class Tensorboard:
  def __init__(self, TB):
    self.TB = TB
    
  def Img(self, tag, X):
    self.TB.add_image(tag, utils.make_grid(X))
    tensorboard.TB.close()
  
  def Graph(self, model, X):
    self.TB.add_graph(model, X)
    tensorboard.TB.close()
  
  def Scalar(self, tag, scalar, step):
    self.TB.add_scalar(tag, scalar, step)
    tensorboard.TB.close()
