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

            # self.U_new = np.zeros((self.numPixels,self.n_clusters))
            self.U_new = np.copy(self.U)
            # self.h = np.zeros((self.n_clusters,self.numPixels))

            self.C = []
            self.C = [1, 85, 255]
            # self.C = [0,255]
            # self.C = [150,200]
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


        def update_U(self):
            for i in range(self.numPixels):
                for j in range(self.n_clusters):
                    sumation = 0
                    for k in range(self.n_clusters):
                        sumation += (self.eucledian_dist(self.X[i], self.C[j]) / self.eucledian_dist(self.X[i], self.C[k])) ** (2 / (self.m-1))
                        self.U[i][j] = 1 / sumation

            print("U : ", self.U)

        def update_C(self):
            for j in range(self.n_clusters):
                num_sum = 0
                den_sum = 0
                for i in range(self.numPixels):
                    num_sum += np.dot((self.U[i][j] ** self.m),self.X[i])
                    den_sum += self.U[i][j] ** self.m
                self.C[j] = np.divide(num_sum,den_sum)

            print("C : ",self.C)

        def calculate_h(self):
            # self.h = np.zeros((self.n_clusters,self.numPixels))
            h = np.zeros((self.n_clusters,self.numPixels))
            u_rolled = np.zeros((self.numPixels ** 0.5,self.numPixels ** 0.5))
            kernel = np.ones((5,5))
            # kernel[2][2] = 4
            # kernel[2][1] = kernel[1][2] = kernel[3][2] = kernel[2][3] = 2
            # print self.U.transpose().shape,self.U.transpose()[0].shape
            for i in range(self.n_clusters):
                u_rolled = self.U.transpose()[i].reshape(self.numPixels ** 0.5,self.numPixels ** 0.5)
                print(u_rolled.shape)
                h_rolled = ndimage.convolve(u_rolled,kernel,mode='constant',cval=0.0)
                # self.h[i] = h_temp.reshape(1,self.numPixels)
                h[i] = h_rolled.reshape(1,self.numPixels)

            h = h.transpose()
            # self.h = self.h.transpose()
            print("\n",h,h.shape)
            return h

        def compute_intuitionistic_U(self):
            Lambda = 0.5
            for i in range(self.numPixels):
                for j in range(self.n_clusters):
                    self.hesitation[i][j] = 1.0 - self.U[i][j] - ( (1 - self.U[i][j]) / (1 + (Lambda * self.U[i][j]) ) )
            int_U = np.add(self.U,self.hesitation)
            self.U = np.copy(int_U)

        def computeNew_U(self):
            p = 1
            q = 2
            self.h = self.calculate_h()
            for j in range(self.numPixels):
                numer = 0.0
                denom = 0.0
                for i in range(self.n_clusters):
                    numer = (self.U[j][i] ** p) * (self.h[j][i] ** q)
                    for k in range(self.n_clusters):
                            denom += (self.U[j][k] ** p) * (self.h[j][k] ** q)
                    self.U_new[j][i] = numer/denom

            self.U = np.copy(self.U_new)

        def calculate_DB_score(self):
            sigma = np.zeros((3,1)).astype(np.float)
            count = np.zeros((3,1))
            result = np.zeros(shape=(self.numPixels,1))
            result = np.argmax(self.U, axis = 1)
            # self.Y = np.copy(self.X.astype(np.uint8))
            # for i in xrange(self.numPixels):
            #	self.Y[i] = self.C[self.result[i]].astype(np.int)

            for i in range(self.n_clusters):
                sigma[i] = 0
                for j in range(self.numPixels):
                    if result[j] == i:
                        count[i] += 1
                        sigma[i] += self.eucledian_dist(self.C[i],self.X[j])
                sigma[i] = sigma[i]/count[i]

            # print result,sigma,count

            R_01 = (sigma[0] + sigma[1])/self.eucledian_dist(self.C[0],self.C[1])
            R_02 = (sigma[0] + sigma[2])/self.eucledian_dist(self.C[0],self.C[2])
            R_12 = (sigma[1] + sigma[2])/self.eucledian_dist(self.C[1],self.C[2])

            D0 = max(R_01,R_02)
            D1 = max(R_01,R_12)
            D2 = max(R_02,R_12)

            DB_score = (D0 + D1 + D2)/self.n_clusters
            print("DB_score: ",DB_score)
