import kociemba
import cv2
# import matplotlib.pyplot as plt
import numpy as np
import os

def get_colours():
#     colours = {'Red' : [140,45,30], 'Green' : [30,80,30], 'Blue' : [30,30,80], 'Orange' : [170,60,40],
#           'White' : [180,180,180], 'Yellow' : [190,175,30]}
#     colours = {'Red' : [180,60,50], 'Green' : [30,80,30], 'Blue' : [30,30,80], 'Orange' : [230,150,50],
#           'White' : [180,180,180], 'Yellow' : [190,175,30]}
#     colours = {'Red' : [180,60,50], 'Green' : [60,130,60], 'Blue' : [30,30,130], 'Orange' : [230,150,50],
#           'White' : [230,230,230], 'Yellow' : [230,200,50]}
    colours = {'Red' : [210,80,70], 'Green' : [90,170,80], 'Blue' : [80,120,150], 'Orange' : [225,120,60],
          'White' : [180,180,180], 'Yellow' : [200,160,60]}
    return colours

def detect_shape(c):
    shape = "unidentified"
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.04 * peri, True)
    if len(approx) == 4:
        (x, y, w, h) = cv2.boundingRect(approx)
        ar = w / float(h)
        shape = "square" if ar >= 0.80 and ar <= 1.20 else "rectangle"
    return shape
    
def draw_squares(contours, img):
    all_contours = cv2.cvtColor(cv2.drawContours(img.copy(), contours, -1, (0,255,0), 1), cv2.COLOR_BGR2RGB)
#     cv2.imshow('All contours', seg)

    colours = get_colours()
    squares_img = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2RGB)
    areas = []
    num = 1
    
    squares = []
    for i, cnt in enumerate(contours):
        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
        if (detect_shape(cnt) == 'square'):
            if(800 <= cv2.contourArea(approx) <= 1000):
                x,y,w,h = cv2.boundingRect(approx)
                squares.append((x,y,w,h))
    
    squares = sorted(squares, reverse = True)
    
    for x,y,w,h in squares:
        cv2.rectangle(squares_img, (x,y), (x+w, y+h), (0,255,0), 3)
        cv2.putText(squares_img, f'{num}', ((2*x+w)//2, (2*y+h)//2), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255,0,0), 1)
        arr = []
        pixel1 = img[(2*y+h)//2, (2*x+w)//2,:]
        diff = {}
        cls = {}
        for col, val in colours.items():
            diff[np.dot(pixel1, val)/(np.linalg.norm(pixel1)*np.linalg.norm(val))] = col
            arr.append(np.dot(pixel1, val)/(np.linalg.norm(pixel1)*np.linalg.norm(val)))
        colour = diff[max(arr)]
        cls[colour] = cls.get(colour, 0) + 1
        ls = []
        for col, val in cls.items():
            ls.append((val, col))
        final_colour = sorted(ls, reverse = True, key = lambda x :x[0])[0][1]
        cv2.putText(squares_img, f'{final_colour[:3]}', ((2*x+w)//2, (2*y+h)//2 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0,255,0), 1)
        num += 1
        areas.append(w*h)
#     cv2.imshow('Final-close', squares_img)
    return squares, all_contours, squares_img

def detect_face(squares, image):
    
    img = image.copy()
    colours = get_colours()
    if len(squares) != 9:
        print('Error')
        return False
    face = []
    for x,y,w,h in squares:
        arr = []
        pixel1 = img[(2*y+h)//2, (2*x+w)//2,:]
        diff = {}
        cls = {}
        for col, val in colours.items():
            diff[np.dot(pixel1, val)/(np.linalg.norm(pixel1)*np.linalg.norm(val))] = col
            arr.append(np.dot(pixel1, val)/(np.linalg.norm(pixel1)*np.linalg.norm(val)))
        colour = diff[max(arr)]
        cls[colour] = cls.get(colour, 0) + 1
        ls = []
        for col, val in cls.items():
            ls.append((val, col))
        final_colour = sorted(ls, reverse = True, key = lambda x :x[0])[0][1]
        face.append(final_colour)
    return face

def is_final(arr):
    if len(arr) > 4:
        if arr[-2] == arr[-1] == arr[-3] == arr[-4] == arr[-5]:
            return True
        else:
            return False
    else:
        return False

def scan_face():
    vid = cv2.VideoCapture(0) 
    check_face_similarity = []
    while True:
        ret, img = vid.read()
        img = cv2.resize(img, (320,180), cv2.INTER_AREA)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        blur = cv2.medianBlur(gray, 5)
        sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        sharpen = cv2.filter2D(blur, -1, sharpen_kernel)

        thresh = cv2.threshold(sharpen,10,255, cv2.THRESH_BINARY_INV)[1]
        thresh = cv2.medianBlur(thresh, 3) + thresh
#         cv2.imshow('thresh',thresh)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
        close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)
#         cv2.imshow('close', close)

        canny = cv2.Canny(thresh, np.median(thresh)*1.5, 255)
#         cv2.imshow('canny', canny)

        kernel = np.ones((3,3), np.uint8)
        dilated = cv2.dilate(canny, kernel, iterations=2)

    # Final from close

        contours, hierarchy = cv2.findContours(close, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        squares, all_contours, squares_img = draw_squares(contours, img.copy())

#         cv2.imshow('All contours', all_contours)
        cv2.imshow('Final-close', squares_img)
        cv2.waitKey(100)
    #     plt.imshow(squares_img)
    #     plt.show()

        if len(squares) == 9:
            face = detect_face(squares, img.copy())
            check_face_similarity.append(face)
            if is_final(check_face_similarity):
                # plt.imshow(cv2.cvtColor(squares_img, cv2.COLOR_BGR2RGB))
                # plt.show()
                print(face)
                break
    vid.release()
#     cv2.destroyAllWindows()
    return face

def scan_cube():
    colours = get_colours()
    color_to_side = {}
    
    os.system('say "Scanning started!!!!"')
    
    print("Front")
    front = scan_face()
    color_to_side[front[4]] = 'F'
    
    # os.system('say "This side is done. Rotate Left"')
    cv2.waitKey(200)
    
    print("right")
    right = scan_face()
    color_to_side[right[4]] = 'R'
    
    # os.system('say "This side is done. Rotate Left"')
    cv2.waitKey(200)
    
    print("back")
    back = scan_face()
    color_to_side[back[4]] = 'B'
    
    # os.system('say "This side is done. Rotate Left"')
    cv2.waitKey(200)
    
    print("left")
    left = scan_face()
    color_to_side[left[4]] = 'L'

    # os.system('say "This side is done. Rotate Left and then rotate Up"')
    cv2.waitKey(200)
    
    print("up")
    up = scan_face()
    color_to_side[up[4]] = 'U'

    # os.system('say "This side is done. Rotate Down and again rotate Down"')
    cv2.waitKey(200)
    
    print("bottom")
    down = scan_face()
    color_to_side[down[4]] = 'D'
    
    # os.system('say "Scanning Completed!!!"')
    cv2.waitKey(200)
    
    face_seq = [up, right, front, down, left, back]
    
    return face_seq, color_to_side


def get_config(face_seq, color_to_side):
    num_seq = [9,6,3,8,5,2,7,4,1]
    final_config = ""
#     mp = {0:8, 1:5, 2:2, 3:7, 4:4, 5:1, 6:6, 7:3, 0:0}
    for face in face_seq:
        for i in num_seq:
            final_config = final_config + color_to_side[face[i-1]]
    # final_config = 'LBBLUBRRRDLLLRBFDLFBFFFURUUBRLFDRBFDDDUFLLURDUUBDBUFDR'
    return final_config