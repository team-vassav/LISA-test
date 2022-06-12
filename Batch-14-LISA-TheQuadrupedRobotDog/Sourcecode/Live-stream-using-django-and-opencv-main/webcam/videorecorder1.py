import numpy as np
import os
import cv2

class VideoCamera(object):
        def __init__(self):
                self.video=cv2.VideoCapture(0)
                self.filename='video.mp4';
                self.frames_per_second=24.0
                self.res="720p"
                
        def change_res(self,cap,width,height):
                cap.set(3,width)
                cap.set(4,width)
                
        def get_dims(self,cap,re):
                STD_DIMENSIONS={"480p":(680,480),"720p":(1280,720),"1080P":(1920,1080),"4k":(1840,2160)}
                width,height=STD_DIMENSIONS[re]
                if re in STD_DIMENSIONS:
                        width,height=STD_DIMENSIONS[re]
                self.change_res(cap,width,height)
                return width,height
        def get_video_type(self,file):
                VIDEO_TYPE={"avi":cv2.VideoWriter_fourcc(*'XVID'),"mp4":cv2.VideoWriter_fourcc(*'XVID')}
                file,ext=os.path.splitext(file)
                if ext in VIDEO_TYPE:
                        return VIDEO_TYPE[ext]
                return VIDEO_TYPE['mp4']
        
        def get_frame(self):
                success, image = self.video.read()
                while success==True:
		# We are using Motion JPEG, but OpenCV defaults to capture raw images,
		# so we must encode it into JPEG in order to correctly display the
		# video stream.
                        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        		frame_flip = cv2.flip(image,1)
        		ret, jpeg = cv2.imencode('.jpg', frame_flip)
        		frame=jpeg.tobytes()
                        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')