# encoding: utf-8
from django.urls import path
from fileupload.views import (
        BasicVersionCreateView, BasicPlusVersionCreateView,
        jQueryVersionCreateView, AngularVersionCreateView,
        PictureCreateView, PictureDeleteView, PictureListView,
        )

urlpatterns = [
    path('basic/', BasicVersionCreateView.as_view(), name='upload-basic'),
    path('basic/plus/', BasicPlusVersionCreateView.as_view(), name='upload-basic-plus'),
    path('new/', PictureCreateView.as_view(), name='upload-new'),
    path('angular/', AngularVersionCreateView.as_view(), name='upload-angular'),
    path('jquery-ui/', jQueryVersionCreateView.as_view(), name='upload-jquery'),
    path('delete/<int:pk>', PictureDeleteView.as_view(), name='upload-delete'),
    path('view/', PictureListView.as_view(), name='upload-view'),
]
