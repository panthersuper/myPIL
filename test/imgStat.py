'''
Created on Feb 2, 2015

@author: Wenzhe Peng
'''
from math import *

def pixel_of(img,a,b):
    return img.getpixel((a,b))    

def greeness(img,thresh=200):
    wid = img.size[0]
    hei = img.size[1]
    count = 0
    for i in range(wid):
        for j in range(hei):
            if pixel_of(img,i,j)[1]>=thresh:
                count+=1
    return float(count)/(wid*hei)

def redness(img,thresh=200):
    wid = img.size[0]
    hei = img.size[1]
    count = 0
    for i in range(wid):
        for j in range(hei):
            if pixel_of(img,i,j)[0]>=thresh:
                count+=1
    return float(count)/(wid*hei)

def blueness(img,thresh=200):
    wid = img.size[0]
    hei = img.size[1]
    count = 0
    for i in range(wid):
        for j in range(hei):
            if pixel_of(img,i,j)[0]>=thresh:
                count+=1
    return float(count)/(wid*hei)

def whiteness(img,thresh=55):
    gr_im = img.convert('LA').convert('RGB')
    wid = gr_im.size[0]
    hei = gr_im.size[1]
    count = 0
    for i in range(wid):
        for j in range(hei):
            if pixel_of(img,i,j)[0]<=thresh:
                count+=1
    return float(count)/(wid*hei)

def likeness_pix(rgb,tp):
    div = 255*3
    sub = abs(rgb[0]-tp[0]) + abs(rgb[1]-tp[1]) + abs(rgb[1]-tp[1])
    return float(sub)/div
    
def likeness_img(img,tp,thresh):
    wid = img.size[0]
    hei = img.size[1]
    count = 0
    for i in range(wid):
        for j in range(hei):
            if likeness_pix(pixel_of(img,i,j),tp)>=thresh:
                count+=1
    return float(count)/(wid*hei)
    
    