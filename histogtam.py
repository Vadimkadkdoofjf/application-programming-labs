import cv2
import matplotlib.pyplot as plt
from numpy import ndarray

def create_hist(img:ndarray)->tuple:

    r_hist = cv2.calcHist(img, [0], None, [256], [0, 256])
    g_hist = cv2.calcHist(img,[1],None,[256],[0,256])
    b_hist = cv2.calcHist(img,[2],None,[256],[0,256])
    return r_hist,g_hist,b_hist

def draw(r_hist:ndarray,g_hist:ndarray,b_hist:ndarray)->None:

    plt.figure(figsize=(10,5))

    plt.plot(r_hist, color='red', label='Красный канал')
    plt.plot(g_hist, color='green', label='Зеленый канал')
    plt.plot(b_hist, color='blue', label='Синий канал')
    plt.xlim([0, 256])
    plt.title('Гистограмма изображения')
    plt.xlabel('Интенсивность пикселей')
    plt.ylabel('Количество пикселей')
    plt.legend()
    plt.show()