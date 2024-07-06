from ast import USub
from traceback import print_tb
from BuddyHome.models import *
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import  AllUsers
from rest_framework.parsers import MultiPartParser
from rest_framework.parsers import JSONParser
import io
import datetime
import shutil
from dateutil.tz import *
# API works
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import FileData,Folder,Files
from BuddyShare import serializers

def Upload_file(request):
    return render(request,"uploadFileHome.html")

# Getting all users from DB 
def getallusers(request):
    try:
        data = {}
        allusers = Buddy_S_User.objects.all()

        serializer = AllUsers(allusers,many=True)
        if serializer:
            return JsonResponse(serializer.data,safe=False)

        data['message'] = "successfully getting the data for users."
        data['status']="200" # success protocol
        return Response(data)
    except Exception as e:
        print("Exception : ",e)
        return HttpResponse("This is giving Exception !")

def DateCreate(DateName,TimeName):
    if DateName and TimeName:
        Year,Month,Day,Hours,Minute,Secounds = [DateName[0:4],DateName[5:7],DateName[8:],TimeName[0:2],TimeName[3:5],55]
        Year = int(Year)
        if Month[0] == '0':
            Month = int(Month[1])
        else:
            Month = int(Month)
        if Day[0] == '0':
            Day = int(Day[1])
        else:
            Day = int(Day)
        if Hours[0] == '0' or Hours == '00':
            Hours = int(Hours[1])
        else:
            Hours = int(Hours)
        if Minute[0] == '0' or Minute == '00':
            Minute = int(Minute[1])
        else:
            Minute = int(Minute)
        DateTimeName = datetime.datetime(Year,Month,Day,Hours,Minute,Secounds) 
        return DateTimeName
    else:
        DateTimeName = datetime.datetime(2030,12,12,11,12,12) 
        return DateTimeName
 
 

# def search(request):
#     query=request.GET['query']
#     if len(query)>78:
#         allprojalop=Projects1.objects.none()
#     else:
#         allprojTitle= Projects1.objects.filter(projectname=query)
#         allprojcreat= Projects1.objects.filter(creator=query)
#         allprojCategory =Projects1.objects.filter(category=query)
#         allprojesc = Projects1.objects.filter(desc=query)
#         allprojalop=  allprojTitle.union( allprojcreat,allprojCategory, allprojesc)
#     if allprojalop.count()==0:
#         messages.warning(request, "No search results found. Please refine your query.")
#     params={'project': allprojalop, 'query': query}
#     return render(request, 'Projects1\search.html', params)



def BuddyShare(request):
    print("Ritik is Runnig it ......")
    EveryOneFileDataObj,EveryOneFolderobj,EveryOneFilesobj = [[],[],[]]
    Fileobj = FileData.objects.all().values()
    # print(Fileobj)
    if request.user.is_authenticated:
        username = request.user.username
        filterUser = User.objects.filter(username=username).values()
        LoggedInUserId = filterUser[0]['id']
        ##################  Changes Here ##################################


        ################## ############# ##################################
        specificFileDataObj = []
        ################################ now specific user changes performed at here ####################################
        count = len(specificFileDataObj)
        for ij in Fileobj:
            lisarray = ij['toShareWith'][1:-1].split(",")
            if(str(LoggedInUserId) in lisarray):
                # print("LoggesUSerID :: ",LoggedInUserId)
                # print("lis array :: ",lisarray)
                specificFileDataObj.append([ij])
                Folderobj0 = Folder.objects.filter(FileUserData=ij['FileDid']).values()
                for ik in Folderobj0:
                    specificFileDataObj[count].append(ik)
                    if ik['FileUserData_id']:
                        Filesobj0 = Files.objects.filter(folder=ik['uid']).values()
                        for ok in Filesobj0:
                            specificFileDataObj[count].append(ok)
                count+=1
        specificuserLoggedIn = []
        for ik in specificFileDataObj:
            d3 = {}
            d3 = ik[0].copy()
            if "UserID" in ik[0].keys():
                user = Buddy_S_User.objects.filter(B_Userid=ik[0]['UserID']).values()
                d3['UserID'] = user[0]['Busername']
            countImglist = []
            iddvar = ""
            for io in range(1,len(ik)):
                if "id" in ik[io].keys():
                    iddvar = ik[io]['id']
                    
                for key, value in ik[io].items():
                    if key == "id" or key in d3.keys():
                        d3[key+str(iddvar)] = value
                    if key =="file":
                        countImglist.append(ik[io]['file'])
                    
                    d3[key] = value

            d3["countImglist"] = countImglist
            specificuserLoggedIn.append(d3)
        ################################ ########################################### ####################################
        ######################################### everyOne Changes at here  #############################################
        Count = len(EveryOneFileDataObj)
         
        for ik in Fileobj:
            if(ik['ShareWithEveryOne']):
                EveryOneFileDataObj.append([ik])
                Folderobj = Folder.objects.filter(FileUserData=ik['FileDid']).values()
                for ij  in Folderobj:
                    EveryOneFileDataObj[Count].append(ij)
                    if ij['FileUserData_id']:
                        Filesobj = Files.objects.filter(folder=ij['uid']).values()
                        for ok in Filesobj:
                            EveryOneFileDataObj[Count].append(ok)
                Count+=1
        EveryOneFileOutLogin = []
        for ik in EveryOneFileDataObj:
            d3 = {}
            d3 = ik[0].copy()
            if "UserID" in ik[0].keys():
                user = Buddy_S_User.objects.filter(B_Userid=ik[0]['UserID']).values()
                d3['UserID'] = user[0]['Busername']
            countImglist = []
            for io in range(1,len(ik)):
                if "id" in ik[io].keys():
                    iddvar = ik[io]['id']
                    
                for key, value in ik[io].items():
                    if key == "id" or key in d3.keys():
                        d3[key+str(iddvar)] = value
                    if key =="file":
                        countImglist.append(ik[io]['file'])
                    
                    d3[key] = value

            d3["countImglist"] = countImglist
            EveryOneFileOutLogin.append(d3)
        # ########################  #############################################
        context = {'EveryOneFileOutLogin':EveryOneFileOutLogin,'EveryOneFileDataObj':EveryOneFileDataObj,'EveryOneFolderobj':EveryOneFolderobj,'EveryOneFilesobj':EveryOneFilesobj,
                    'specificuserLoggedIn':specificuserLoggedIn}
    else:
        Count = len(EveryOneFileDataObj)
        for ik in Fileobj:
            if(ik['ShareWithEveryOne']):
                EveryOneFileDataObj.append([ik])
                Folderobj = Folder.objects.filter(FileUserData=ik['FileDid']).values()
                for ij  in Folderobj:
                    EveryOneFileDataObj[Count].append(ij)
                    if ij['FileUserData_id']:
                        Filesobj = Files.objects.filter(folder=ij['uid']).values()
                        for ok in Filesobj:
                            EveryOneFileDataObj[Count].append(ok)
                Count+=1
        # print(EveryOneFileDataObj)
        EveryOneFileOutLogin = []
        for ik in EveryOneFileDataObj:
            d3 = {}
            d3 = ik[0].copy()
            if "UserID" in ik[0].keys():
                user = Buddy_S_User.objects.filter(B_Userid=ik[0]['UserID']).values()
                d3['UserID'] = user[0]['Busername']
            countImglist = []
            for io in range(1,len(ik)):
                if "id" in ik[io].keys():
                    iddvar = ik[io]['id']
                    
                for key, value in ik[io].items():
                    if key == "id" or key in d3.keys():
                        d3[key+str(iddvar)] = value
                    if key =="file":
                        countImglist.append(ik[io]['file'])
                    
                    d3[key] = value

            d3["countImglist"] = countImglist
            EveryOneFileOutLogin.append(d3)

        context = {'EveryOneFileDataObjWithOutLogin':EveryOneFileDataObj,'EveryOneFileOutLogin':EveryOneFileOutLogin,'EveryOneFilesobj':EveryOneFilesobj}
    return render(request,"BuddyShare/ViewAllFileFolder.html",context)



def APIBuddyShare(request):
    return render(request,"ViewAllFiles.html",{})

def zip_files(folder):
    shutil.make_archive(f'public/static/zip/{str(folder)}','zip',f'public/static/{folder}')

def uploadFile(request):
    print("Inside function !")
    if request.method == 'POST':
        print("Inside If condition")
        ToShareWithAll = request.POST.get('ToShareWith')
        StudentSelect = request.POST.getlist('StudentSelect')
        SlectCollegues = request.POST.getlist('SlectCollegues')
        DeleteChechbox = request.POST.get('DeleteChechbox')
        TimeName = request.POST.get('timeName')
        DateName = request.POST.get('DateName')      
        if len(request.FILES) != 0:
            filepond = request.FILES.getlist('filepond')

        DateTimeName = DateCreate(DateName,TimeName)
        
        if DeleteChechbox == "on":
            DeleteChechbox = True
        else:
            DeleteChechbox = False
            DateTimeName = None
        UserList = []
        if ToShareWithAll == "1":
            ToShareWithAll = True
        elif ToShareWithAll == "2" or ToShareWithAll == "3":
            ToShareWithAll = False
            UserList.extend(StudentSelect)
            UserList.extend(SlectCollegues)

        UserList = [int(i) for i in UserList]
        FileData1 = FileData(UserID=3,tobeDelete=DeleteChechbox ,TimeForDeletion=DateTimeName ,ShareWithEveryOne=ToShareWithAll,toShareWith=UserList)
        FileData1.save()
        Folder1 = Folder(FileUserData = FileData1)
        Folder1.save()
        files_objs = []
        for file in filepond:
            files_obj = Files.objects.create(folder=Folder1,file=file)
            files_objs.append(files_obj)
        zip_files(Folder1.uid)
        print(str(Folder.uid))
        return HttpResponse("Data Getting !")    
    else:
        return render(request,"BuddyShare/uploadFiles.html",{})


import os
import datetime
import glob
import sys
from pathlib import Path
@api_view(["GET",])
def DeleteFiles(request):
    BASE_DIR = os. getcwd() 
    BASE_DIR += '\public\static\\'
    AllFileData =FileData.objects.all().values() # tobeDelete
    AllFileData =FileData.objects.filter(tobeDelete=True).values() # all().values() 
    for t_file in AllFileData:
        DeletableFolder = Folder.objects.filter(FileUserData=t_file['FileDid']).values()
        for Del_Folder in DeletableFolder:
            # print(Del_Folder)
            # print(Del_Folder['uid'])
            # DeletableFiles = Files.objects.filter(folder = Del_Folder['uid']).values()
            path_imgs = Del_Folder['uid']
            path_zip = Del_Folder['uid']
            path_imgs = BASE_DIR + str(path_imgs)
            path_zip = BASE_DIR+"zip\\"+ str(path_zip) +".zip"
            all_img_files = os.path.join(path_imgs,'*.png')
            # print(all_img_files)
            all_img_files = glob.glob(all_img_files)
            # print(all_img_files)
            date_and_time_file = t_file['TimeForDeletion']
            only_date_field = date_and_time_file.strftime("%Y-%m-%d")
            only_time_field = date_and_time_file.strftime("%H:%M")
            current_time = datetime.datetime.now()
            only_current_date = current_time.strftime("%Y-%m-%d")
            only_current_time = current_time.strftime("%H:%M")
            if only_current_date == only_date_field:
                only_current_minute = current_time.strftime("%M")
                only_minute_field = date_and_time_file.strftime("%M")
                if only_current_time == only_time_field or only_current_minute>=only_minute_field:
                    # selecting file data 
                    selected_file_data = FileData.objects.get(FileDid = t_file['FileDid'])
                    # selecting folders 
                    selected_folder = Folder.objects.get(FileUserData = t_file['FileDid'])
                    # selecting all specific files 
                    slected_file = Files.objects.filter(folder = Del_Folder['uid'])
                    # deleting the entries in DB 
                    try:
                        slected_file.delete()
                        selected_folder.delete()
                        selected_file_data.delete()
                    except Exception:
                        print(f"Getting Exception While Delete :: {Exception}")
                    # deleting the files 
                    try:
                        os.remove(path_zip)
                        print('Deleete :Zip File: Yes')
                    except Exception:
                        print('Delete : No')
                        print(f'Error : {sys.exc_info()}')
                    
                    for img_trav in all_img_files:
                        print(img_trav)
                        try:
                            os.remove(img_trav)
                            print('Deleete :img file: Yes')
                        except Exception:
                            print('Delete : No')
                            print(f'Error : {sys.exc_info()}')  
                else:
                    print("Time is not Matching")
            else:
                print("No Need To Delete File")
            
            


        print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    # ,Folder,Files
    # retention = 1
    # current_time = datetime.datetime.now()
    # retention_time = current_time - datetime.timedelta(days=retention)

    # print(f'Current Time : {current_time}')
    # print(f'rententition Time : {retention_time}')

    # log_dir = '/home/shrkhar/Desktop/pCode/logdir'
    # search_log = os.path.join(log_dir,'*.log')

    # l_logfiles = glob.glob(search_log)
    # print(l_logfiles)

    # for t_file in l_logfiles:
    #     t_mod = os.path.getatime(t_file)
    #     t_mod = datetime.datetime.fromtimestamp(t_mod)
    #     print(f"{t_file}{t_mod}")
    #     if retention_time>t_mod:
    #         try:
    #             os.remove(t_file)
    #             print('Deleete : Yes')
    #         except Exception:
    #             print('Delete : No')
    #             print(f'Error : {sys.exc_info()}')
    #     else:
    #         print('Delete : Not Required')
    return HttpResponse(f"Data Getting ! <br> {AllFileData}")    
    return Response({
                    'status':200,
                    'message':'files delete function successfully'
                })

 