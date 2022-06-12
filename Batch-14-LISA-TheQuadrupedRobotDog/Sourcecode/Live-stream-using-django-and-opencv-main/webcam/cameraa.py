from django.conf import Settings
from imutils.video import VideoStream
import imutils
import cv2
import datetime
import time
import os
import numpy as np
import copy

class VideoCamera(object):
	def __init__(self):
		self.video = cv2.VideoCapture(0)
		self.filename="video.mp4"
		self.pic="new_img.jpg"
		self.res="720p"
		self.is_record = False
		self.out = None
		self.recordingThread=None
		self.record=False

	def __del__(self):
		self.video.release()
		cv2.destroyAllWindows()

	def change_res(self,cap,width,height):
		cap.set(3,width)
		cap.set(4,height)
	
	def get_dims(self,cap,re):
		STD_DIMENSIONS={"720p":(1280,720)}
		width,height=STD_DIMENSIONS[re]
		if re in STD_DIMENSIONS:
			width,height=STD_DIMENSIONS[re]
		self.change_res(cap,width,height)
		return width,height

	def get_video_type(self,file):
		VIDEO_TYPE = 
			{"avi":cv2.VideoWriter_fourcc(*'mp4v'),
			"mp4":cv2.VideoWriter_fourcc(*'mp4v')}
		file,ext=os.path.splitext(file)
		if ext in VIDEO_TYPE:
			return VIDEO_TYPE[ext]
		return VIDEO_TYPE['mp4']

	def file(self,c,f):
		if f:
			self.filename="video"+str(c)+".mp4"
			return self.filename
		else:
			return self.filename

	def img(self,d,g):
		if g:
			self.pic="new_img"+str(d)+".jpg"
			return self.pic
		else:
			return self.pic

			
	#web streaming
	def get_frame(self,record,videocapture,imagecapture,
		hmap=False,c=None,f=False,d=None,g=False):
		if record:
			out = 
			cv2.VideoWriter(self.file(c,f), 
				self.get_video_type(self.filename), 
				15, self.get_dims(self.video, self.res))
			newimg=self.img(d,g)
			casx='haarcascade_frontalface_default.xml'
			faceCascade=cv2.CascadeClassifier(casx)
			ret,frame=self.video.read()
			fgbg=cv2.createBackgroundSubtractorMOG2()
			height,width=frame.shape[:2]
			accum_image=np.zeros((height,width),np.uint8)
			while True:
				ret,image = self.video.read()
				gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
				faces = faceCascade.detectMultiScale(gray,1.1,4)
				font = cv2.FONT_HERSHEY_COMPLEX
				text = "width: "+str(self.video.get(3))+
					"height: "+str(self.video.get(4))
				dates = str(datetime.datetime.now())
				frame_flip = 
					cv2.putText(image,dates,(10,50),
						font,1,(0,255,255),2,cv2.LINE_AA)
				for (x,y,w,h) in faces:
					cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
				if hmap:
					fgmask=fgbg.apply(gray)
					thresh=2
					maxvalue=2
					ret,th1 = 
						cv2.threshold(fgmask,thresh,maxvalue,
								cv2.THRESH_BINARY)
					accum_image = cv2.add(accum_image,th1)
					color_image, im_color=
						cv2.applyColorMap(accum_image,cv2.COLORMAP_HOT)
					frame_flip = 
						cv2.addWeighted(image,0.7,color_image,0.7,0)
				if videocapture:
					out.write(frame_flip)
				if imagecapture:
					cv2.imwrite(newimg,frame_flip)
					imagecapture=False
				ret, jpeg = cv2.imencode('.jpg', frame_flip)
				frame=jpeg.tobytes()
				yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' 
					+ frame + b'\r\n\r\n')
		else:
			out.release()