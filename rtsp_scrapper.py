#!/usr/bin/env python
# coding: utf-8

# In[43]:


import cv2
import cv2 as cv
import numpy as np
from datetime import datetime
import time
import argparse


# In[ ]:


parser = argparse.ArgumentParser()
parser.add_argument("-t", "--time", type=int, required=True,
                        help='How long will scratch in hours')
parser.add_argument("--fps", type=int, required=True,
                        help='FPS wanted to download the video')
args = vars(parser.parse_args())


# In[19]:


#Camera 26
rtsp_path26 = "rtsp://10.143.59.182:554>/live?id=26&stream=high"
rtspCam26 = cv2.VideoCapture(rtsp_path26)
# Get current width of frame
width26 = rtspCam26.get(cv2.CAP_PROP_FRAME_WIDTH)   # float
# Get current height of frame
height26 = rtspCam26.get(cv2.CAP_PROP_FRAME_HEIGHT) # float

#Camera 29
rtsp_path29 = "rtsp://10.143.59.182:554>/live?id=29&stream=high"
rtspCam29 = cv2.VideoCapture(rtsp_path29)
# Get current width of frame
width29 = rtspCam29.get(cv2.CAP_PROP_FRAME_WIDTH)   # float
# Get current height of frame
height29 = rtspCam29.get(cv2.CAP_PROP_FRAME_HEIGHT) # float

#Camera 35
rtsp_path35 = "rtsp://10.143.59.182:554>/live?id=35&stream=high"
rtspCam35 = cv2.VideoCapture(rtsp_path35)
# Get current width of frame
width35 = rtspCam35.get(cv2.CAP_PROP_FRAME_WIDTH)   # float
# Get current height of frame
height35 = rtspCam35.get(cv2.CAP_PROP_FRAME_HEIGHT) # float

#Camera 36
rtsp_path36 = "rtsp://10.143.59.182:554>/live?id=36&stream=high"
rtspCam36 = cv2.VideoCapture(rtsp_path36)
# Get current width of frame
width36 = rtspCam36.get(cv2.CAP_PROP_FRAME_WIDTH)   # float
# Get current height of frame
height36 = rtspCam36.get(cv2.CAP_PROP_FRAME_HEIGHT) # float

#Camera 39
rtsp_path39 = "rtsp://10.143.59.182:554>/live?id=39&stream=high"
rtspCam39 = cv2.VideoCapture(rtsp_path39)
# Get current width of frame
width39 = rtspCam39.get(cv2.CAP_PROP_FRAME_WIDTH)   # float
# Get current height of frame
height39 = rtspCam39.get(cv2.CAP_PROP_FRAME_HEIGHT) # float

#Camera 40
rtsp_path40 = "rtsp://10.143.59.182:554>/live?id=40&stream=high"
rtspCam40 = cv2.VideoCapture(rtsp_path40)
# Get current width of frame
width40 = rtspCam40.get(cv2.CAP_PROP_FRAME_WIDTH)   # float
# Get current height of frame
height40 = rtspCam40.get(cv2.CAP_PROP_FRAME_HEIGHT) # float


# In[35]:


#Create encoder for avi file
fourcc = cv2.VideoWriter_fourcc(*'XVID')

#Creates de output to save de new video file
now = datetime.now()
date = now.strftime("%d-%m-%Y-%H:%M:%S")

out26 = cv2.VideoWriter('results/camera26_'+date+'.avi', fourcc, args['fps'], (int(width26),int(height26)) )
out29 = cv2.VideoWriter('results/camera29_'+date+'.avi', fourcc, args['fps'], (int(width29),int(height29)) )
out35 = cv2.VideoWriter('results/camera35_'+date+'.avi', fourcc, args['fps'], (int(width35),int(height35)) )
out36 = cv2.VideoWriter('results/camera36_'+date+'.avi', fourcc, args['fps'], (int(width36),int(height36)) )
out39 = cv2.VideoWriter('results/camera39_'+date+'.avi', fourcc, args['fps'], (int(width39),int(height39)) )
out40 = cv2.VideoWriter('results/camera40_'+date+'.avi', fourcc, args['fps'], (int(width40),int(height40)) )


# In[36]:


startTime = time.time()
hours=0
while( hours / args['time'] <= 1):
    #Camera 26
    ret26, frame26 = rtspCam26.read()
    if ret26==True:
        out26.write(frame26)
       # cv2.imshow('frame28',frame28)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

    #Camera 29
    ret29, frame29 = rtspCam29.read()
    if ret29==True:
        out29.write(frame29)
      #  cv2.imshow('frame29',frame29)
        
    #Camera 35
    ret35, frame35 = rtspCam35.read()
    if ret35==True:
        out35.write(frame35)
        #cv2.imshow('frame35',frame35)
        
    #Camera 36
    ret36, frame36 = rtspCam36.read()
    if ret36==True:
        out36.write(frame36)
       # cv2.imshow('frame36',frame36)
        
    #Camera 39
    ret39, frame39 = rtspCam39.read()
    if ret39==True:
        out39.write(frame39)
       # cv2.imshow('frame39',frame39)
        
    #Camera 40
    ret40, frame40 = rtspCam40.read()
    if ret40==True:
        out40.write(frame40)
      #  cv2.imshow('frame40',frame40)
    
    currentTime = time.time()
    hours = (currentTime - startTime)/3600


# In[39]:


# Release everything if job is finished
rtspCam26.release()
rtspCam29.release()
rtspCam35.release()
rtspCam36.release()
rtspCam39.release()
rtspCam40.release()
out26.release()
out29.release()
out35.release()
out36.release()
out39.release()
out40.release()

