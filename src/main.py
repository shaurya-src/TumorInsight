from func import *
from skimage.util import img_as_ubyte
from skimage.filters import rank
from skimage.morphology import watershed, disk
from skimage import data
from imageio import imread
from scipy import ndimage, misc
from PIL import Image
from tkinter.filedialog import askopenfilename
from tkinter import Tk, ttk, messagebox
import sys
import random
import math
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib
matplotlib.use("TkAgg")


filename = "unassigned"
top = Tk()
top.title('Hello, Tkinter!')
top.geometry('1000x1000')

limit = 100
maxCycle = 3000
D = 50
lb = -5.12
RAND_MAX = 2147483647
ub = 5.12
runtime = 1
ObjValSol = 0
FitnessSol = 0
neighbor = 0
param2change = 0
GlobalMin = 0
run = 0


def process():
    img = cv2.imread(filename)
    global blur
    blur = cv2.bilateralFilter(img, 9, 75, 75)
    b = numpy.zeros([blur.shape[0], blur.shape[1], blur.shape[2]])
    b = numpy.copy(blur)
    cv2.imwrite('color_img.tif', b)

    # s=cv2.imread(blur,0)
    # imshow('s',s)
    plt.subplot(121), plt.imshow(img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
    plt.xticks([]), plt.yticks([])
    plt.show()


def FCM():
    class FCM():
        def __init__(self, imageName, n_clusters, epsilon=0.05, max_iter=-1):
            self.m = 2
            self.n_clusters = n_clusters
            self.max_iter = max_iter
            self.epsilon = epsilon

            read = ReadImage(imageName)
            print("THIS IS READ", read.getData())
            self.X, self.numPixels = read.getData()
            self.X = self.X.astype(np.float)
            print("initial X:", self.X, self.X.shape)

            self.U = []
            for i in range(self.numPixels):
                index = i % n_clusters
                l = [0 for j in range(n_clusters)]
                l[index] = 1
                self.U.append(l)
            self.U = np.array(self.U).astype(np.float)
            self.U = self.U.reshape(self.numPixels, self.n_clusters)

            #self.U_new = np.zeros((self.numPixels,self.n_clusters))
            self.U_new = np.copy(self.U)
            #self.h = np.zeros((self.n_clusters,self.numPixels))

            self.C = []
            self.C = [1, 85, 255]
            #self.C = [0,255]
            #self.C = [150,200]
            self.C = np.array(self.C).astype(np.float)
            self.C = self.C.reshape(self.n_clusters, 1)
            print("initial C:\n", self.C, self.C.shape)

            Lambda = 2
            self.hesitation = np.zeros((self.numPixels, self.n_clusters))
            for i in range(self.numPixels):
                for j in range(self.n_clusters):
                    self.hesitation[i][j] = 1.0 - self.U[i][j] - \
                        ((1 - self.U[i][j]) / (1 + (Lambda * self.U[i][j])))

            print(self.hesitation)
