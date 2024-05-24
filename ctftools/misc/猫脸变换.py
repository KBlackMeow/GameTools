import cv2
import numpy as np
import tqdm
import hashlib
def arnold(img, shuffle_times, a, b):
    r, c, d = img.shape
    p = np.zeros(img.shape, np.uint8)
    for s in range(shuffle_times):
        for i in range(r):
            for j in range(c):
                x = (i + b * j) % r
                y = (a * i + (a * b + 1) * j) % c
                p[x, y, :] = img[i, j, :]
        img = np.copy(p)
    return p

def de_arnold(img, shuffle_times, a, b):
    r, c, d = img.shape
    p = np.zeros(img.shape, np.uint8)
    for s in range(shuffle_times):
        for i in range(r):
            for j in range(c):
                x = ((a * b + 1) * i - b * j) % r
                y = (- a * i + j) % c
                p[x, y, :] = img[i, j, :]
        img = np.copy(p)
    return p

def quick_calc_all_arnold_times(src_img_path,img_path_s,a,b,max_iter=255):

    img = cv2.imread(src_img_path)
    img = img[:, :, [2]]
    trans = {hashlib.md5(bytes(img)).hexdigest():0}
    r, c, d = img.shape
    p = np.zeros(img.shape, np.uint8)

    for s in tqdm.tqdm(range(max_iter)):
        for i in range(r):
            for j in range(c):
                x = (i + b * j) % r
                y = (a * i + (a * b + 1) * j) % c
                p[x, y, :] = img[i, j, :]
        img = p.copy()
        trans[hashlib.md5(bytes(img)).hexdigest()]=s+1
    
    ans = [0 for i in range(len(img_path_s))]
    for i in tqdm.tqdm(img_path_s):
        img2 = cv2.imread("img/"+i)
        img2 = img2[:, :, [2]]
        ans[int(i.split(".")[0])]=trans[hashlib.md5(bytes(img2)).hexdigest()]
    return ans
        


import os 
imgs = os.listdir('img')

ans = quick_calc_all_arnold_times("img/9.png",imgs,1,1)
f=open("solver.zip","wb")
f.write(bytes(ans))
f.close()

