
import cv2
import os
from numpy import ndarray


def read_img(image:str)-> ndarray:
    img = cv2.imread(image)

    if not os.path.exists(image):
        raise FileNotFoundError("image is not found")

    if img is None:
        raise ValueError("The image could not be uploaded")

    if not image.endswith(".jpg"):
        raise ValueError("It is not image")
    return img

def print_h_w(img:ndarray)->None:
    height,width = img.shape[:2]
    print(f"Высота: {height}, Ширина: {width}")

def show(image:ndarray)->None:
    cv2.imshow("image",image)
    cv2.waitKey(0)

def inverted(image:ndarray)->ndarray:
    return cv2.bitwise_not(image)

def save(img: ndarray, path_to_image:str)->None:
    if not path_to_image.endswith(".jpg"):
        raise ValueError("this file should be jpg format")

    cv2.imwrite(path_to_image,img)

