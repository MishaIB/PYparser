import cv2
import numpy as np
import tqdm
import os
names={"cat","dog"}
#пересохранение
for name in names:
    os.makedirs('dataset1/{name}')
    os.makedirs('dataset1/{name}')
    for i in range(1,1020):
        img=cv2.imread(f'dataset/{name}/{str(i).zfill(4)}.jpg')
        cv2.imwrite(f'dataset1/{name}/{str(i).zfill(4)}.jpg', img)



#проверка на повтор
mypath = r"dataset1\cat"

from os import listdir
from os.path import isfile, join
onlyfiles = [join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)
def cmp(image1: cv2.Mat, image2: cv2.Mat) -> bool:
    if image1 is None or image2 is None:
        return False
    return image1.shape == image2.shape and not(np.bitwise_xor(image1,image2).any())


images = []

for file in onlyfiles:
    image = cv2.imread(file)
    images.append((image, file))


images2 = images.copy()
for im1, file in tqdm.tqdm(images):
    images2.remove((im1, file))
    for im2, file2 in (images2):
        if cmp(im1, im2):
            if not os.path.exists(f'dataset/del'):
                os.makedirs(f'dataset/del')
            print(file, file2)
            os.remove(file2)