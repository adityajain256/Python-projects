import os

dir = "images"  #images is the name of directory you can put your dir name

files = os.listdir(dir)

i = 1

for file in files:
        if file.endswith('.png'):
                os.rename(f"images\{file}", f'images\{i}.png')
                i = i+1