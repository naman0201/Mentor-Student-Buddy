from dataclasses import fields
from email.policy import default
from random import choices
from BuddyHome.serializers import Buddy_S_User
import shutil
from sqlite3 import Time
from rest_framework import serializers
from .serializers import *
from .models import *
import datetime

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
