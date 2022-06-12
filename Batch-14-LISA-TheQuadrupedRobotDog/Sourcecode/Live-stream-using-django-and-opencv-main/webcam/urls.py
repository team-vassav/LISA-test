from django.contrib import admin
from django.urls import path, include
from webcam import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Live', views.Live, name='Live'),
    path('End', views.End, name='End'),
    path('Record', views.Record, name='Record'),
    path("Takepic",views.Takepic,name="Takepic"),
    path('RecordStop',views.RecordStop,name="RecordStop"),
    path('Heat',views.Heat,name="Heat"),
    path('Stopmap',views.Stopmap,name='Stopmap'),
    path('video_recordd', views.video_recordd, name='video_recordd'),
    path('video_feed', views.video_feed, name='video_feed'),
    path('video_record', views.video_record, name='video_record'),
    path('ImgCapture',views.ImgCapture,name='ImgCapture'),
    path('stoprecord',views.stoprecord,name="stoprecord"),
    path('Heat_map',views.Heat_map,name='Heat_map'),
]