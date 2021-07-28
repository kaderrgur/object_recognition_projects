import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    ret, frame=cap.read()
    
    frame=cv2.flip(frame, 1)
    frame=cv2.resize(frame, (960,720))
    
    frame_width=frame.shape[1]
    frame_height=frame.shape[0]
    
    frame_blob=cv2.dnn.blobFromImage(frame, 1/255, (416,416), swapRB=True, crop=False)
    
    labels=["Mask", "None", "without_Mask"]
    
    
    colors=["0,0,255", "0,0,255", "255,0,0", "255,255,0", "0,255,0"]
    colors=[np.array(color.split(",")).astype("int") for color in colors]
    colors=np.array(colors)
    colors=np.title(colors, (18,1))
    
    
    model=cv2.dnn.readNetFromDarknet()
    
    layers=model.getLayerNames()
    
    