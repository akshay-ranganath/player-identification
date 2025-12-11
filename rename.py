import os
from glob import glob
import re



images = glob('./data/*.jpg')
index = 1
players = []
for img in images:
    file_name = img
    img = img.replace('./data/','')
    img = img.split('_2025_')[0]
    name = img.replace('_', ' ')
    players.append({
        "name:": name,
        "index": index
    })
    index += 1
    # now rename the file
    os.rename(file_name, f'./data/{index}.jpg')


print(players)
    