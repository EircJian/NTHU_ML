# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 17:13:34 2022

@author: Eric Jian
"""

import os

import numpy as np
import pandas as pd
from PIL import Image

path = 'C:/Users/username/Desktop/total/'
files = os.listdir(path)
print(files) #印出讀取到的檔名稱，用來確認自己是不是真的有讀到

n = 2754
for i in files: #因為資料夾裡面的檔案都要重新更換名稱
    
    img = Image.open("C:/Users/username/Desktop/ml_imgs/Neverland/87/train_{j}.jpg".format(j = n))
    new_img = img.resize( (288, 160), Image.BILINEAR )
    new_img.save("C:/Users/username/Desktop/resize_total/resize_train_{j}.jpg".format(j = n))
	
    n += 1
    