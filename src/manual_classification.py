import cv2
import pandas as pd
import numpy as np
import math

def record_click(event,x,y,flags,param):
    global mouseX, mouseY
    if event == cv2.EVENT_LBUTTONDOWN:
        mouseX, mouseY = x, y
        return mouseX, mouseY

#NOT FINISHED
def turn_coord_to_label(coords, class_division=10):
    #The coordinates are placed in classes and mapped to a number
    #which the function spits out
    index_sequence = np.arange(class_division*class_division)
    index_matrix = index_sequence.reshape((10, 10))
    #rescale
    img = cv2.imread('./training_data/img_0.jpg')
    height = img.shape[0]
    width = img.shape[1]
    x_scaled = coords[0]*class_division
    y_scaled = coords[1]*class_division
    print x_scaled
    x_sector = int(x_scaled/class_division)
    y_sector = int(y_scaled/class_division)
    #print index_matrix[x_sector, y_sector]
    return
    # y_vector = np.zeros(13)
    # coords = row[0], row[1]
    # x_sector = int(coords[0]/13)
    # y_sector = int(coords[1]/10)
    # y_vector[x_sector*y_sector] = 1
    # all_sectors.append(y_vector)

#Call this function for the directory you want to classify
#images. E.g. current_dir = './training_data'
#Then click on the spot on the image where you want the
#classification to be stored.
def record_coords(current_dir, number_pictures):
    allCords = pd.DataFrame([[0,0]])
    for i in range(0, number_pictures):
        path = current_dir + '/img_%s.jpg'%i
        img = cv2.imread(path)
        cv2.namedWindow('image')
        cv2.setMouseCallback('image', record_click)
        cv2.imshow('image', img)
        cv2.waitKey(0)
        allCords.loc[i] = [mouseX, mouseY]
    save_dir = current_dir + '/labels.txt'
    allCords.to_csv(save_dir, sep=",", header=None, index=False)
    return

def canny_edge_detection(tar_dir):
    img = cv2.imread(tar_dir)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gauss = cv2.GaussianBlur(img_gray, (5, 5), 0)
    img_canny = cv2.Canny(gauss, 10,20)
    return img_canny

def find_center():
    tar_dir = './../Output/img_81.jpg'
    contour = canny_edge_detection(tar_dir)
    indices = np.where(contour != 0)
    x = int(np.mean(indices[0]))
    y = int(np.mean(indices[1]))
    return x,y

x, y = find_center()
print x, y
