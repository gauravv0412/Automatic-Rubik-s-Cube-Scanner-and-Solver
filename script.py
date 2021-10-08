import kociemba
import cv2
# import matplotlib.pyplot as plt
import numpy as np
from util import *
import glob
import os
from class_cube import *

################ Scanning User's Cube #############

face_seq, color_to_side = scan_cube()
print(color_to_side)
final_config = get_config(face_seq, color_to_side)


# final_config = "FBBDUBRLLFLLRRDBFUDUDFFBLLRDDDUDUUFRUBFRLLLRBUURRBFBDF"

fw = open('initial_config.txt', 'w')
fw.write(final_config)
fw.close()

cube = Cube(flag = True, config = final_config)

file = open('./solution.txt', 'w')
while cube.get_string() != 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB':
    soln = kociemba.solve(cube.get_string())
    print(soln)
    file.write(soln + ' ')
    for move in soln.split():
        if move[0] == 'D':
            if len(move) == 2:
                if move[1] == '2':
                    cube.rd()
                    cube.rd()
                else:
                    cube.rd_()
            else:
                cube.rd()
        if move[0] == 'U':
            if len(move) == 2:
                if move[1] == '2':
                    cube.rt()
                    cube.rt()
                else:
                    cube.rt_()
            else:
                cube.rt()
        if move[0] == 'L':
            if len(move) == 2:
                if move[1] == '2':
                    cube.rl()
                    cube.rl()
                else:
                    cube.rl_()
            else:
                cube.rl()
        if move[0] == 'R':
            if len(move) == 2:
                if move[1] == '2':
                    cube.rr()
                    cube.rr()
                else:
                    cube.rr_()
            else:
                cube.rr()
        if move[0] == 'B':
            if len(move) == 2:
                if move[1] == '2':
                    cube.rb()
                    cube.rb()
                else:
                    cube.rb_()
            else:
                cube.rb()
        if move[0] == 'F':
            if len(move) == 2:
                if move[1] == '2':
                    cube.rf()
                    cube.rf()
                else:
                    cube.rf_()
            else:
                cube.rf()  
                
    print(cube.get_string())
print('Solved')
file.close()

################ Blender module #############

os.system('rm -rf ./blender/video/*')
os.system('/Applications/Blender/blender.app/Contents/MacOS/./blender -b ./blender/rubikcube_final.blend -x 1 -o //video/video_tutorial -a')

################ Play Video module #############

files = list(glob.glob('./blender/video/*'))
file = files[0]

cap = cv2.VideoCapture(file)
   
if (cap.isOpened()== False): 
  print("Error opening video  file")
   
while(cap.isOpened()):
      
  ret, frame = cap.read()
  if ret == True:
   
    cv2.imshow('Video_Tutorial', frame)
   
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
   
  else: 
    break
   
cap.release()
   
if cv2.waitKey(10000) & 0xFF == ord('q'): 

	cv2.destroyAllWindows()
