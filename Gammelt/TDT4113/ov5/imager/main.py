from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

# Image.save(imagepath)
class PILWrapper():
  def __init__(self, imagepath=False, image=False):
    self.image = image if not imagepath else Image.open(imagepath)
    self.xmax = self.image.size[0]
    self.ymax = self.image.size[1]
  def save(self, savepath):
    self.image.save(savepath)
  def display(self):
    self.image.show()
  def resize(self, new_x, new_y):
    self.image = self.image.resize((new_x, new_y))
  def scale(self, factor):
    self.image = self.image.resize((round(self.xmax*factor), round(self.ymax*factor)))


pw = PILWrapper('./julialf.jpg')
pw.scale(0.5)
pw.display()
