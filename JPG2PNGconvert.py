import sys
import os
from PIL import Image

start_folder = sys.argv[1]
output_folder = sys.argv[2]


if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    

for filename in os.listdir(start_folder):
  clean_name = os.path.splitext(filename)[0]
  img = Image.open(f"{start_folder}{filename}") 
  img.save(f"{output_folder}/{clean_name}.png", "png")
  print("all done!")
