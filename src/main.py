import sys
import random
import math
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib
matplotlib.use("TkAgg")

from tkinter import Tk, ttk, messagebox
from tkinter.filedialog import askopenfilename

from PIL import Image

from scipy import ndimage, misc
from imageio import imread
from skimage import data
from skimage.morphology import watershed, disk
from skimage.filters import rank
from skimage.util import img_as_ubyte

from func import *

def main():
    print("Hello world")


if __name__ == '__main__':
    main()
