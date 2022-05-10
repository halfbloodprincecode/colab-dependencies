from torchvision import utils

class Tensorboard:
  def __init__(self, TB):
    self.TB = TB
    
  def Img(self, tag, X):
    self.TB.add_image(tag, utils.make_grid(X))
