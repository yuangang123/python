from PIL import Image,ImageFilter

kitten = Image.open("/home/yuangang/桌面/1485186822215.jpeg")
blurrikitten= kitten.filter(ImageFilter.GaussianBlur)
blurrikitten.save("GaussianBlur.jpeg")
blurrikitten.show()
