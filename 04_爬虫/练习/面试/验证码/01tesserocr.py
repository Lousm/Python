import tesserocr
from PIL import Image

print(tesserocr)
image = Image.open('1.jpg')
result = tesserocr.image_to_text(image)
print(result)
