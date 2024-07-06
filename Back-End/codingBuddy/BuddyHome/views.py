from urllib import response
from django.shortcuts import render,redirect
from django.http import HttpResponse
from BuddyHome.models import Contact,Buddy_S_User
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth import logout,authenticate,login
# from BuddyHome.models import Register_user
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='/login')
def teamMembers(request):
    if request.user.is_authenticated:
        username = request.user.username
        filterUser = User.objects.filter(username=username).values()
        LoggedInUserId = filterUser[0]['id']
    
    return render(request, 'BuddyHome/team.html',{'userDetail':filterUser[0]})    

@login_required(login_url='/login')
def index(request):
    context={}
    if request.user.is_authenticated:
        username = request.user.username
        filterUser = User.objects.filter(username=username).values()
        context['userDetail']=filterUser[0]
    return render(request, 'BuddyHome/index.html',context)

@login_required(login_url='/login')
def home(request):
    context={}
    if request.user.is_authenticated:
        username = request.user.username
        filterUser = User.objects.filter(username=username).values()
        context['userDetail']=filterUser[0]
    return render(request, 'BuddyHome/index.html',context)

def register_user(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        if request.method == "POST":
            username=request.POST['Username']
            password=request.POST['password']
            confpassword=request.POST['Confpassword']
            u_id = request.POST['U_Id']
            email = request.POST['email'] 
            usertype = request.POST.get('usertype').lower()
            if len(u_id)==12 and usertype == 'student':
                branch = u_id[4:6].upper()
            if len(u_id)==10 and usertype == 'teacher':
                branch = u_id[4:6].upper()
            print(usertype)
            try:
                #check for erroneous inputs
                useObj = User.objects.filter(email=email)
                Buddy_S_OBj_email = Buddy_S_User.objects.filter(email= email)
                Buddy_S_OBj_uid = Buddy_S_User.objects.filter(u_ID = u_id)
                
                if useObj or Buddy_S_OBj_email or Buddy_S_OBj_uid:
                    messages.error(request,'Already account created please login ')
                    return redirect("/register")
                if password == confpassword:
                    myuser = User.objects.create_user(username,email, password)
                    myuser.save()
                    # adding into the group 
                    group = Group.objects.get(name=usertype)
                    myuser.groups.add(group) 
                    Branchgroup = Group.objects.get(name=branch)
                    myuser.groups.add(Branchgroup) # student Branch Group
                    Buddyuser = Buddy_S_User(user = myuser,u_ID = u_id  ,Busername = username,password=password,email= email ,usertype=usertype)
                    Buddyuser.save()

                    messages.success(request, "your account has been successfully created")
                    return redirect("/login")
                else:
                    messages.error(request, "password doesn't match! ")
                    return redirect("/register")
            except Exception as e:
                print("Except")
                messages.error(request,f"Exception : {e}")
                return redirect("/register")
        return render(request, 'BuddyHome/register.html')

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        if request.method=="POST":
            username=request.POST.get('Username')
            password=request.POST.get('password')
            print("USerNAme: ",username)
            print("PAssword",password)
            user=authenticate(username= username, password= password)
            
            if user is not None:
                print("USer is not none")
                #A backend authenticated the credentials
                login(request,user)
                messages.success(request,"login successfully")
                return redirect("/home")
            else:
                #No backend authenticated the credentials
                messages.warning(request,"Invalid Credentials or If you don't have account please SignUp")
                return redirect("/login")
                
        return render(request, 'BuddyHome/login.html')
    
def logout_user(request):
    logout(request)
    return redirect("/login")

@login_required(login_url='/login')
def about(request):
    context={}
    if request.user.is_authenticated:
        username = request.user.username
        filterUser = User.objects.filter(username=username).values()
        context['userDetail']=filterUser[0]

    return render(request, 'BuddyHome/about.html',context)

@login_required(login_url='/login')
def contact(request):
    context={}
    if request.user.is_authenticated:
        username = request.user.username
        filterUser = User.objects.filter(username=username).values()
        context['userDetail']=filterUser[0]
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'BuddyHome/contact.html',context)

@login_required(login_url='/login')
def services(request):
    context={}
    if request.user.is_authenticated:
        username = request.user.username
        filterUser = User.objects.filter(username=username).values()
        context['userDetail']=filterUser[0]
    return render(request, 'BuddyHome/services.html',context)

def userProfile(request,u_ID):
    context = {}
    if request.user.is_authenticated:
        username = request.user.username
        filterUser = User.objects.filter(username=username).values()
        LoggedInUserId = filterUser[0]['id']
        if LoggedInUserId == u_ID:
            Buddy_S_User_Detail = Buddy_S_User.objects.filter(user = LoggedInUserId).values()[0]
            context = {
                "userDetail":filterUser[0],
                "Buddy_S_User_Detail":Buddy_S_User_Detail
            }
            return render(request,"BuddyHome\profile.html",context)
        else:
            messages.error(request, "profile not Found !")
            context['ErrorMessage'] = "profile not Found"
            return render(request,"BuddyHome\profile.html",{'data':"profile not Found"})    
    messages.error(request, "You are Not Logged In Please Login !")
    context['ErrorMessage'] = "You Are Not Logged In"
    return render(request,"BuddyHome\profile.html",context)
        

