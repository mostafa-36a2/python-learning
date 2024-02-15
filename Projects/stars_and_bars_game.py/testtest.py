from ascii_art import ascii_art
# Load an image
image_path = "image.png"
with open(image_path, "rb") as f:
   image_data = f.read()
# Convert the image to ASCII art
ascii_data = ascii_art(image_data)
# Display the ASCII art in the terminal
print(ascii_data)