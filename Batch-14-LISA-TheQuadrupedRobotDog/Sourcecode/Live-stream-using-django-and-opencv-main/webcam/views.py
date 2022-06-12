from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from webcam.cameraa import VideoCamera
# Create your views here.
#home page
c=0
d=0
livestr=False
endstr=False
liverec=False
heatmap=False
def index(request):
	return render(request, 'home.html')

#live stream
def Live(request):
	global livestr
	livestr=True
	return render(request, 'LiveStream.html')

def gen2(camera):
	record=True
	videorecord=False
	imagecapture=False
	return camera.get_frame(record,videorecord,imagecapture)

def video_record(request):
	return StreamingHttpResponse(gen2(VideoCamera()),content_type='multipart/x-mixed-replace; boundary=frame')

#live stream end
def End(request):
	global livestr
	if livestr:
		livestr=False
		return render(request,'Endstream.html')
	else:
		raise Exception("Live stream not yet started or Live stream has Ended")

def gen(camera):
	record=False
	videorecord=False
	imagecapture=False
	return camera.get_frame(record,videorecord,imagecapture)

def video_feed(request):
	return StreamingHttpResponse(gen(VideoCamera()),content_type='multipart/x-mixed-replace; boundary=frame')

#live stream recording
def Record(request):
	global liverec
	liverec=True
	if livestr:
		return render(request,'RecordStream.html')
	else:
		raise Exception("Live stream not yet started")

def gen3(camera):
	global c
	c=c+1
	record=True
	videorecord=True
	imagecapture=False
	f=True
	return camera.get_frame(record,videorecord,imagecapture,False,c,f)

def video_recordd(request):
	return StreamingHttpResponse(gen3(VideoCamera()),content_type='multipart/x-mixed-replace; boundary=frame')

#live stream stop
def RecordStop(request):
	global liverec
	if livestr:
		if liverec:
			liverec=False
			return render(request,'RecStop.html')
		else:
			raise Exception("Live Recording not yet started")
	else:
		#return render(request,'Live Stream not yet started')
		raise Exception("Live stream not yet started")

def gen5(camera):
	record=False
	videorecord=False
	imagecapture=False
	return camera.get_frame(record,videorecord,imagecapture)

def stoprecord(request):
	return StreamingHttpResponse(gen5(VideoCamera()),content_type='multipart/x-mixed-replace; boundary=frame')

#image capture
def Takepic(request):
	if livestr:
		return render(request,'Takepic.html')
	else:
		raise Exception("Live stream not yet started")

def gen4(camera):
	global d
	d=d+1
	record=True
	videorecord=True
	imagecapture=True
	return camera.get_frame(record,videorecord,imagecapture,False,None,False,d,True)

def ImgCapture(request):
	return StreamingHttpResponse(gen4(VideoCamera()),content_type='multipart/x-mixed-replace; boundary=frame')

#heat map
def Heat(request):
	global heatmap
	heatmap=True
	if livestr:
		return render(request,'heat.html')
	else:
		raise Exception("Live stream not yet started")

def gen6(camera):
	record=True
	videorecord=False
	imagecapture=False
	hmap=True
	return camera.get_frame(record,videorecord,imagecapture,hmap)


def Heat_map(request):
	global heatmap
	heatmap=True
	return StreamingHttpResponse(gen6(VideoCamera()),content_type='multipart/x-mixed-replace; boundary=frame')

#stop heat map
def Stopmap(request):
	global heatmap
	if livestr:
		if heatmap:
			heatmap=True
			return render(request,'Stopmap.html')
		else:
			raise Exception("Heap map not yet started")
	else:
		raise Exception("Live stream not yet started")



