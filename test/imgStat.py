'''
Created on Feb 2, 2015

@author: Wenzhe Peng
'''
def pixel_of(img,a,b):
    return img.getpixel((a,b))    

def greeness(img,thresh):
    wid = img.size[0]
    hei = img.size[1]
    count = 0
    for i in range(wid):
        for j in range(hei):
            if pixel_of(img,i,j)[1]>=thresh:
                count+=1
    return float(count)/(wid*hei)

def redness(img,thresh):
    wid = img.size[0]
    hei = img.size[1]
    count = 0
    for i in range(wid):
        for j in range(hei):
            if pixel_of(img,i,j)[0]>=thresh:
                count+=1
    return float(count)/(wid*hei)

def blueness(img,thresh):
    wid = img.size[0]
    hei = img.size[1]
    count = 0
    for i in range(wid):
        for j in range(hei):
            if pixel_of(img,i,j)[0]>=thresh:
                count+=1
    return float(count)/(wid*hei)

def whiteness(img,thresh):
    gr_im = img.convert('LA').convert('RGB')
    wid = gr_im.size[0]
    hei = gr_im.size[1]
    count = 0
    for i in range(wid):
        for j in range(hei):
            if pixel_of(img,i,j)[0]<=thresh:
                count+=1
    return float(count)/(wid*hei)