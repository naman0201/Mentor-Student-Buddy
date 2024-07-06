from uuid import *
from pyexpat import model
from django.core.checks import messages
from django.db import models
from django.contrib.auth.models import User
from BuddyHome.models import Buddy_S_User
import os

class FileData(models.Model):
    FileDid = models.AutoField(primary_key=True)
    UserID = models.CharField(max_length=200)
    tobeDelete = models.BooleanField(default=False)
    TimeForDeletion = models.DateTimeField(blank=True,null=True)
    ShareWithEveryOne = models.BooleanField(default=True)
    toShareWith = models.CharField(max_length=100,default="[]") 

class Folder(models.Model):
    uid =  models.UUIDField(primary_key=True,editable=False,default = uuid4)
    FileUserData = models.ForeignKey(FileData,default="101", on_delete=models.CASCADE)
    crated_at = models.DateField(auto_now=True)

def get_upload_path(instance , filename):
    return os.path.join(str(instance.folder.uid),filename)

class Files(models.Model):
    folder = models.ForeignKey(Folder,on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_upload_path)
    created_at = models.DateField(auto_now=True)

# class FilesShare(models.Model):
#     File_id = models.AutoField(primary_key=True)
#     File_name = models.CharField(max_length=50,unique=True)
#     desc = models.CharField(max_length=300,default="File Shared by .. ")
#     pub_date = models.DateTimeField(auto_now=True)
#     Userid = models.ForeignKey(Buddy_S_User, null=True, blank=True, on_delete=models.CASCADE)
#     ToShareWith = models.ManyToManyField()
#     def __str__(self):
#         return self.File_name

# class jointable(models.Model):
#     uploaderid = models.ManyToManyField(Buddy_S_User,blank=True) 
#     File_id = models.ManyToManyField(FilesShare,blank=True)
#     image = models.ImageField(upload_to= "carsell/images",default="")
  