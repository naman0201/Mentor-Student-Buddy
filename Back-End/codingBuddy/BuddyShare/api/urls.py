
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    path("getAllusers",getallusers),
    path("FileRelatedInfoSave",FileRelatedInfoSave),
    path("APIFileShare",HandleFileUpload.as_view()),
    # path('APIBuddyShare', APIBuddyShare),l
    path('APIBuddyView', APIBuddyAllFilesView),
    path('APIBuddyEveryOneView', APIBuddyAllFilesEveryOneView),
    path("APIBuddyView/<int:FileId>",APIBuddySpecificFileShare),
    
]
