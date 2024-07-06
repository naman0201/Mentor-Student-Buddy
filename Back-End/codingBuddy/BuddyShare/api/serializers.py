from dataclasses import fields
from email.policy import default
from random import choices
from BuddyHome.serializers import Buddy_S_User
import shutil
from sqlite3 import Time
from rest_framework import serializers
from .serializers import *
from BuddyShare.models import *
import datetime

class FileBuddyGETShare(serializers.Serializer):
    B_Userid = serializers.CharField()

class AllUsers(serializers.Serializer):
    B_Userid = serializers.CharField()
    user = serializers.CharField()
    u_ID = serializers.CharField(max_length=30)
    Busername = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=120)
    name = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    profile_pic = serializers.ImageField()
    date_created = serializers.DateTimeField()
    usertype = serializers.CharField(max_length=20)    

class FileAllData(serializers.Serializer):
    FileDid =           serializers.CharField()
    UserID =            serializers.CharField(max_length=200)
    tobeDelete =        serializers.BooleanField()
    TimeForDeletion =   serializers.DateTimeField()
    ShareWithEveryOne = serializers.BooleanField()
    toShareWith =       serializers.CharField(max_length=100) 

class FileRelatedDataShare(serializers.ModelSerializer):
    DateName = serializers.CharField(default="2030-10-05")
    TimeName = serializers.CharField(default="05:02:12")
    class Meta:  
        model = FileData
        fields = ['UserID','tobeDelete','ShareWithEveryOne','toShareWith','TimeName','DateName']

class FileListSerializer(serializers.Serializer):
    FileDataId = serializers.CharField(default="000")
    files = serializers.ListField(
        child = serializers.FileField(max_length = 10000,allow_empty_file=False,use_url=False)
    )
    def zip_files(self,folder):
        shutil.make_archive(f'public/static/zip/{str(folder)}','zip',f'media/{folder}')
    fildatavar = ""
    # def FileExtraData(self,FileData):
    #     self.fildatavar = FileData
    
    def create(self, validated_data):
        # FileExtraDataOBJ = self.fildatavar
        fileDataIdLocal=validated_data.pop('FileDataId')
        # FileUserDataObj = FileData(FileDid=FileExtraDataOBJ)
        FileUserDataObj = FileData(FileDid=int(fileDataIdLocal))
        folder = Folder.objects.create(FileUserData=FileUserDataObj)
        files = validated_data.pop('files')
        files_objs = []
        for file in files:
            files_obj = Files.objects.create(folder=folder,file=file)
            files_objs.append(files_obj)

        self.zip_files(folder.uid)

        return {'files':{},'folder':str(Folder.uid)}
 

# {
# "UserID":"bhavna@123",
# "tobeDelete":"True",
# "TimeForDeletion" :  "2022-09-07 01:16",
# "ShareWithEveryOne": "True",
# "toShareWith": ["ritik"]
# }

class GetFilesAPISerializer(serializers.Serializer):
    fileSerField = serializers.CharField()
