from email.headerregistry import Group
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.core.validators import RegexValidator

class Buddy_S_User(models.Model):
    CATEGORY = (
			('Principal', 'Principal'),
			('HOD_S', 'HOD_S'),
			('Special_Teacher', 'Special_Teacher'),
			('Special_Student', 'Special_Student'), 
			('Teacher', 'Teacher'),
            ('Student', 'Student'),
			)
    B_Userid = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    u_ID = models.CharField(max_length=30, null=False)
    Busername = models.CharField(max_length=50)
    password = models.CharField(max_length=120)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="profile1.png",upload_to= "BuddyHome/images", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    usertype = models.CharField(max_length=20, null=True, choices=CATEGORY)
    def __str__(self):
        return self.name


class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex = r'^\+?1?\d{10}$',message = "The format should be exactly be of 10 digits"   )
    contactno = models.CharField(max_length=25,validators=[phone_regex])
    dateTimeNow = models.DateTimeField(auto_now_add=True)
    query = models.TextField()
