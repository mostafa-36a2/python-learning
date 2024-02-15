from PIL import Image
import random

from numpy import average
#str = input()

def get_random_pixel(width,height):
    x=random.randrange(0,width)
    y=random.randrange(0,height)
    return (x,y)

def randomize_image_pixels(img):
    for i in range(0,img.width*img.height):
        pixel1 = get_random_pixel(img.width,img.height)
        pixel2 = get_random_pixel(img.width,img.height)
        #print(f"pixel {x},{y}, {type(x)}, {type(y)}")
        #print(f"pixel {x},{y}: {img.getpixel((x,y))}")
        img.putpixel(
            pixel1,img.getpixel(pixel2)
        )
    return img
def overexpose_image(img):
    for x in range(0,img.width):
        for y in range(0,img.height):
            pixel = img.getpixel((x,y))
            img.putpixel(
                (x,y),max(pixel)
            )
    return img
def underexposed_image(img):
    for x in range(0,img.width):
        for y in range(0,img.height):
            pixel = img.getpixel((x,y))
            m = min(pixel)
            min_p=(m,m,m)
            img.putpixel(
                (x,y),min_p
            )
    return img
def greyscale_image(img):
    for x in range(0,img.width):
        for y in range(0,img.height):
            pixel = img.getpixel((x,y))
            img.putpixel(
                (x,y),average(pixel)
            )
    return img
def print_image_details(img):
    print(f"Image bands: {img.getbands()}")
    print(f"image width: {img.width}")
    print(f"image height: {img.height}")

list_of_images = [
    'balloon.png',
    'dragonfly.png',
    'cat.png'
]
for img_name in list_of_images:
    print(f"Processing {img_name}")
    try:
        img = Image.open(img_name)
    except Exception as e:
        print(f"Failed to load image, with excetion: {e}")
        exit()

    print_image_details(img)
    #img = randomize_image_pixels(img)
    overexpose_image(img.copy()).save(f'overexpose.{img_name}')
    underexposed_image(img.copy()).save(f'underexpose.{img_name}')
    greyscale_image(img.copy()).save(f'grayscale.{img_name}')
    #img.save(f'tmp.{img_name}')