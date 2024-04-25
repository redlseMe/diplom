import os
from PIL import Image

def cutImages(imgPath, scale):
    outputFolder = 'output_images'
    # Load the image
    img = Image.open(imgPath)
    width, height = img.size
    sub_width = width // scale
    sub_height = height // scale
    os.makedirs(outputFolder, exist_ok=True)
    for i in range(scale):
        for j in range(scale):
            left = j * sub_width
            upper = i * sub_height
            right = left + sub_width
            lower = upper + sub_height
            sub_img = img.crop((left, upper, right, lower))
            sub_img.save(os.path.join(outputFolder, f'sub_img_{i}_{j}.png'))

    return outputFolder