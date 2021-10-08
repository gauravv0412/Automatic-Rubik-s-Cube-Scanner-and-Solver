import glob
import cv2
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
   
if cv2.waitKey(100000) & 0xFF == ord('q'): 

	cv2.destroyAllWindows()