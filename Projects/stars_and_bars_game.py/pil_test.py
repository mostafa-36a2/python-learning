from PIL import Image

base_width= 170
img = Image.open('/home/mostafa/Documents/Learning/Python/Projects/stars_and_bars_game.py/image.png')
base_width= 170
wpercent = (base_width / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((base_width, hsize), Image.Resampling.LANCZOS)
img.save('somepic.png')