#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 12:33:57 2019

@author: rohit
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np


source_img='img2.jpeg';save_img=source_img.split('.')[0]+'_save.jpeg'

img = cv2.imread(source_img)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
rows,cols,ch = img.shape
img=cv2.resize(img,(cols//1,rows//1))


#select first 4 coords for pts1 perspective transform and thair projection onto pts2
  
pts1 = np.float32([[35, 28], [149, 9], [152, 216], [35, 256]])
pts2 = np.float32([[0,0],[1000,0],[1000,1000],[0,1000]])

M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(1000,1000))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

#write frame in memory
dst=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
cv2.imwrite(save_img, dst)