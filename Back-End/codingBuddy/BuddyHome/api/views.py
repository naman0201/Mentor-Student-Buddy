from django.http import HttpResponse
from django.shortcuts import render,redirect
from random import randint
import re
import io
from django.contrib.auth.models import Group
from rest_framework.parsers import JSONParser
## user works
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import login as auth_login

# API works
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from BuddyHome.models import Buddy_S_User
from .serializers import RegisterSerializer,LoginSerializer,ContactSerializer
from rest_framework.renderers import JSONRenderer
# from TSA.ProjectHome.api import serializers


@api_view(["GET",])
def index(request):
    context={}
    if request.user.is_authenticated:
        username = request.user.username
        filterUser = User.objects.filter(username=username).values()
        context['userDetail']=filterUser[0]
        context['status']="200" # success protocol
        context['message'] = "Successfully Got Data"
        return Response(context)
    context['status']="420" # success protocol
    context["message"] = "Invalid credentials! Please try again"
    return Response(context)

@api_view(["POST",])
def loginuser(request):
    serializer = LoginSerializer(data=request.data)
    data={}
    if serializer.is_valid():
        loginusername = serializer.validated_data['email']
        loginpassword = serializer.validated_data['password']
        try:
            if valiemail(loginusername):
                email1 = User.objects.filter(email=loginusername)
                user=authenticate(username= email1[0], password= loginpassword)
                filterUser = Buddy_S_User.objects.filter(user=user).values()
            else:
                user=authenticate(username= loginusername, password= loginpassword)
            if user is not None:
                auth_login(request, user)
                data['status']="200" # success protocol
                data['userDetail'] = filterUser[0]
                data['message'] = "Successfully Logged in"
            else:
                data['status']="420" # success protocol
                data['message'] = "Invalid credentials! Please try again"
        except:
            data['status']="420" # success protocol
            data["message"] = "Invalid credentials! Please try again"
    return Response(data)        
    
@api_view(["POST",])
def registeruser(request):
    serializer = RegisterSerializer(data=request.data)
    data ={}
    if serializer.is_valid():
        branch = "CS"
        fields = ['u_ID','email','name','password','password2','usertype']
        u_ID = serializer.validated_data['u_ID']
        email = serializer.validated_data['email']
        name = serializer.validated_data['name']
        password1 = serializer.validated_data['password']
        password2 = serializer.validated_data['password2']
        usertype = serializer.validated_data['usertype']
        if usertype.lower() == 'student' and len(u_ID)<=12 :
            branch = u_ID[4:6].upper()
        elif usertype.lower() == 'teacher' and len(u_ID)==10 :
            branch = u_ID[4:6].upper()      
        else:
            data['message'] = " Your Enrollment does not belong to any branch ! Enter correct enrollment number"
            data['status']="420" # success protocol
            return Response(data)

        if len(email) > 200:
                data['message'] = " Your email must be under 200 characters"
                data['status']="420" # success protocol
                return Response(data)
                
        if (password1!= password2):
            data['message'] = "passwords does not match !"
            data['status']="420" # Error protocol
            return Response(data)


        try:
            print("try")
            userobj = User.objects.filter(email = email)
            BuddyUseremail = Buddy_S_User.objects.filter(email=email)
            BuddyuserId = Buddy_S_User.objects.filter(u_ID=u_ID)
            if userobj or BuddyUseremail or BuddyuserId:
                print("User Already Exist")
                data['message'] = "User Already Registered.please Login .."
                data['status']="420" # error protocol
                return Response(data)
                
            username = 'U'+ email[:3]+str(random_with_N_digits((len(email)%5)+1))
            myuser = User.objects.create_user(username, email, password1)
            myuser.save()
                                # adding into the group 
            group = Group.objects.get(name=usertype.lower())
            myuser.groups.add(group) 
            Branchgroup = Group.objects.get(name=branch.upper())
            myuser.groups.add(Branchgroup) # student Branch Group
            Buddy_S_User.objects.create(user=myuser,u_ID=u_ID,name=name,Busername=username,password=password1,email=email,usertype=usertype)
            
            data['message'] = "successfully registered a new user."
            data['status']="200" # success protocol
        except Exception as e:
            print("Exception is here ",e)
    else:
        data = serializer.errors
    return Response(data)

def logoutuser(request):
    data = {}
    try:
        logout(request)
        data['message'] = "successfully registered a new user."
        data['status']="200" # success protocol
        return Response(data)
    except:
        return HttpResponse("There is some error at server please try again later !")

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def valiemail(emailva):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.fullmatch(regex, emailva)

@api_view(["POST",])
def Contact(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser().parse(stream)
        serializer = ContactSerializer(data=pythonData)
        if serializer.is_valid():
            serializer.save()
            data = {
                'message':'Your Query has been Save ! We you Try to Respond you Soon ..'
            }
            data['status']="200" # success protocol
        else:
            data['error'] = "Error Occured While Saving Data Contact ! Try Contacting Later .."

        return Response(data)
@api_view(["GET",])
def userProfile(request,u_ID):
    if request.user.is_authenticated:
        username = request.user.username
        filterUser = User.objects.filter(username=username).values()
        LoggedInUserId = filterUser[0]['id']
        if LoggedInUserId == u_ID:
            Buddy_S_User_Detail = Buddy_S_User.objects.filter(user = LoggedInUserId).values()
            context = {
                "userDetail":filterUser,
                "Buddy_S_User_Detail":Buddy_S_User_Detail
            }
            return Response({
                'status':200,
                'message':'files uploaded successfully ',
                'data':context
            })            
        else:
            return Response({
                'status':200,
                'message':'files uploaded successfully ',
                'data':"profile not Found"
            })    
    return Response({
            'status':200,
            'message':'files uploaded successfully ',
            'data':"You Are not LoggedIn please Login"
        })
        