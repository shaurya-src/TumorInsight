import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils
from imutils import perspective
import sys

cv2.namedWindow('image', cv2.WINDOW_NORMAL)


def nothing(x):
    pass


def tumor_part(c):
    area = cv2.contourArea(c)
    print(area)
    hull = cv2.convexHull(c)
    hull_area = cv2.contourArea(hull)
    if hull_area != 0:
        solidity = float(area) / hull_area
    else:
        solidity = 0
    # print(solidity,area)
    if solidity > 0.5 and area > 2000:
        # print(area)
        return True
    else:
        return False


def blur_image(img):
    # blur = cv2.GaussianBlur(img,(5,5),0)
    # blur=cv2.bilateralFilter(img,9,75,75)
    kernel = np.ones((5, 5), np.float32) / 25
    blur = cv2.filter2D(img, -1, kernel)
    return blur


# Adaptive Histogram enhancement
def enhance(img):
    clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(8, 8))
    gray = cv2.equalizeHist(img)
    # gray = clahe.apply(blur)
    return gray


def threshold(img, b):
    ret, thresh = cv2.threshold(img, b, 255, cv2.THRESH_BINARY)
    # thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,2)
    # kernel = np.ones((5,5),np.uint8)
    # # erosion = cv2.erode(thresh,kernel,iterations = 1)
    # # dilation = cv2.dilate(erosion,kernel,iterations = 1)
    # dilation = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    # dilation = cv2.dilate(dilation,kernel,iterations = 1)

    return thresh


def contours(img, org, b):
    # emg2=enhance(img2)
    img2 = threshold(img, b)
    cnts = cv2.findContours(img2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    # print(len(cnts))
    img2 = RGB(img2)
    org = RGB(org)
    for (i, c) in enumerate(cnts):
        if tumor_part(c):
            # print("so",area,solidity)
            cv2.drawContours(org, [c], -1, (1, 255, 11), 2)
            cv2.drawContours(img2, [c], -1, (1, 255, 11), 2)

    return (org, img2)


def RGB(img):
    return cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)


def k_means(img):
    Z = img.reshape((-1, 1))
    Z = np.float32(Z)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 8
    ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))
    return res2


def edge_ex(img):
    return cv2.Canny(img, 100, 200)


def show_images(gray, blur, seg, cont_org, cont_mask):
    res1 = np.hstack((blur, seg))
    res2 = np.hstack((cont_org, cont_mask))
    res = np.vstack((res1, res2))
    cv2.imwrite("result_kmean.jpg", res)
    cv2.imshow("image", res)


def process(img3, b):
    gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
    blur = blur_image(gray)
    seg = k_means(blur)
    cont_org, cont_mask = contours(seg, gray, b)
    seg = RGB(seg)
    blur = RGB(blur)
    gray = RGB(gray)
    show_images(gray, blur, seg, cont_org, cont_mask)


img_name = input("Enter the name of MRI Image: ")
# img1 = cv2.imread(f"sample_dataset/brain_tumor_dataset/yes/{sys.argv[1]}")
img1 = cv2.imread(f"sample_dataset/brain_tumor_dataset/yes/{img_name}")
org = img1.copy()
process(img1, 144)

for b in range(0):
    process(img1, b)
    # img1 = cv2.imread(f"sample_dataset/brain_tumor_dataset/yes/{sys.argv[1]}")
    img1 = cv2.imread(f"sample_dataset/brain_tumor_dataset/yes/{img_name}")
    k = cv2.waitKey(1) & 0xFF
    print()
    if k == ord('q'):
        break

# plt.subplot(121),plt.imshow(res)
# plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(out)
# plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
# plt.suptitle(methods[0])
# plt.show()

# sol.sort(reverse=True)


# for i in range(len(sol)):
#     print(*sol[i], sep=" ")


#
# plot_image = np.concatenate((img, dilation), axis=1)
# plt.imshow(cv2.cvtColor(plot_image, cv2.COLOR_BGR2RGB))
# plt.show()


# cv2.imshow("Br",img)
#
# cv2.waitKey(0)
cv2.destroyAllWindows()
