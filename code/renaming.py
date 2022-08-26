# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os

import numpy as np
import pandas as pd
from PIL import Image

#import matplotlib.pyplot as plt
#import tensorflow as tf
#import sklearn

#from tensorflow import keras
#from tensorflow.keras import layers
#from tensorflow.keras.models import Sequential
#from sklearn import metrics

path = 'C:/Users/username/Desktop/ml_imgs/Neverland/87/' #這就是欲進行檔名更改的檔案路徑，路徑的斜線是為/，要留意下！
files = os.listdir(path)
print(files) #印出讀取到的檔名稱，用來確認自己是不是真的有讀到

n = 2754
for i in files: #因為資料夾裡面的檔案都要重新更換名稱
	oldname = path + files[n-2754] #指出檔案現在的路徑名稱，[n]表示第n個檔案
	newname = path + 'train_' + str(n) + '.jpg'
	os.rename(oldname, newname)
	print(oldname + '>>>' + newname) #印出原名與更名後的新名，可以進一步的確認每個檔案的新舊對應
	n += 1
    
    
    
    
    
    
    
    
    