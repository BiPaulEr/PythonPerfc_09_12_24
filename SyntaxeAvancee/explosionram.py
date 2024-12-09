import os
from PIL import Image

def load_images(image_directory):
    for filename in os.listdir(image_directory):
        if filename.endswith(".jpg"):
            image_path = os.path.join(image_directory, filename)
            image  = Image.open(image_path)
            yield image

for idx, img in enumerate(load_images("C:/Users/PaulE/Documents/DataSet/Baroque")):
    img.save(f"C:/Users/PaulE/Documents/DataSet/TEST/{idx}.jpg")


