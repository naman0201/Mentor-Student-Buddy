
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [

    path('', BuddyShare),
    path("frontFile",Upload_file),
    path("getAllusers",getallusers),
    path('UploadFile', uploadFile),
    path('APIBuddyShare', APIBuddyShare),
    path('ShareGetApi/',include("BuddyShare.api.urls")),
    path('deleteFile', DeleteFiles),
]
