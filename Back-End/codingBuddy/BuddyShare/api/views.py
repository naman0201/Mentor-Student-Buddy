from ast import USub
from traceback import print_tb
from urllib import response
from BuddyHome.models import *
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FileListSerializer,FileRelatedDataShare,AllUsers
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
from BuddyShare.models import FileData,Folder,Files
from BuddyShare.api.serializers import *

 
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

@api_view(["POST",])
def FileRelatedInfoSave(request):
    serializer = FileRelatedDataShare(data=request.data)
    data ={}
    print("Request Data",request.data)
    try:
        if serializer.is_valid():
            UserID = serializer.validated_data['UserID']
            tobeDelete = serializer.validated_data['tobeDelete']
            TimeName = serializer.validated_data['TimeName']
            DateName = serializer.validated_data['DateName']
            ShareWithEveryOne = serializer.validated_data['ShareWithEveryOne']
            DateTimeName = DateCreate(DateName,TimeName)
            print(UserID,tobeDelete,TimeName,DateName,ShareWithEveryOne)
            # ToShareWith = serializer.validated_data['toShareWith']
            print(UserID,tobeDelete,TimeName,DateName,ShareWithEveryOne)
            FileDataObj = FileData.objects.create(UserID=UserID,tobeDelete=tobeDelete,TimeForDeletion=DateTimeName,ShareWithEveryOne=ShareWithEveryOne,toShareWith="[1,2,3,4]")
            print("File Data Object : ",FileDataObj)
            print("File id ",FileDataObj.FileDid)
            data["File_Data"] = FileDataObj.FileDid
            request.session['FileDataObj'] = FileDataObj.FileDid
            request.session.set_expiry(300)
            request.session.modified = True
            print("File Session :: ",request.session['FileDataObj'])
            data['message'] = "successfully registered a new File Data."
            data['status']="200" # success protocol
            return Response(data)
        else:
            print("Serializer Errors :: ",serializer.errors)
            data['440']="200" # success protocol
            data['error'] = "Error Occured While Saving Data ! Try Uploading Data Later .."
            return Response(data)
    except Exception as e:
        return Response({
                'status':400,
                'message':f'something went wrong {e}',
                'data':serializer.errors
        }) 
class HandleFileUpload(APIView):
    parser_classes = [MultiPartParser]
    def post(self, request):
        print("Inside Post Method !")
        print("Request Object",request.data)
        try:
            print("Inside try fo this ")
            data = request.data
            # ExtaFiledata =  request.session['FileDataObj']
            # print(ExtaFiledata)
            serializer= FileListSerializer(data=data)
            print(serializer)
            
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status':200,
                    'message':'files uploaded successfully ',
                    'data':serializer.data
                })
            return Response({
                'status':400,
                'message':'something went wrong',
                'data':serializer.errors
            })
        except Exception as e:
            print("Exception :> ",e)
            return Response({
                'status':400,
                # 'userDetail':filterUser[0],
                'message':f'This is Exception something went wrong {e}',
                # 'data':serializer.errors
            })

@api_view(["POST",])
def APIBuddyAllFilesView(request):
    serializer = FileBuddyGETShare(data=request.data)
    EveryOneFileDataObj,EveryOneFilesobj = [[],[]]
    Fileobj = FileData.objects.all().values()
    if serializer.is_valid():
        B_Userid = serializer.validated_data['B_Userid']
        specificFileDataObj = []
        count = len(specificFileDataObj)
        for ij in Fileobj:
            if(ij['ShareWithEveryOne']):
                continue
            lisarray = ij['toShareWith'][1:-1].split(",")
            if(str(B_Userid) in lisarray):
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
        print("+++++++++++++++++>>>>>>>>>>>specificFileDataObj<<<<<<<<<<<<<<+++++++++++++++++++",specificFileDataObj)
        for ik in specificFileDataObj:
            d3 = {}
            d3 = ik[0].copy()
            if "UserID" in ik[0].keys():
                user = Buddy_S_User.objects.filter(B_Userid=ik[0]['UserID']).values()
                print("++++++++++++++++ =================================",user[0]['Busername'])
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
        return Response({
                    'status':200,
                    'message':'Getting Files successfully ',
                    'data':{'specificuserLoggedIn':specificuserLoggedIn,'EveryOneFileOutLogin':EveryOneFileOutLogin}
                })
    else:
        return Response({
                    'status':400,
                    'message':f'something went wrong',
                    'data':'Error While Serving Data Please Try Again Later...'
                })  

@api_view(["GET",])
def APIBuddyAllFilesEveryOneView(request):
    EveryOneFileDataObj,EveryOneFilesobj = [[],[]]
    Fileobj = FileData.objects.all().values()
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
    return Response({
                    'status':200,
                    'message':'Getting Files successfully ',
                    'data':{'EveryOneFileDataObjWithOutLogin':EveryOneFileOutLogin}
                })

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

@api_view(["GET",])
def APIBuddySpecificFileShare(request,FileId):
    if request.user.is_authenticated:
        username = request.user.username
        filterUser = User.objects.filter(username=username).values()
        
        Fileobj = FileData.objects.filter(FileDid=FileId).values()
        specificFileDataObj = []
        count = len(specificFileDataObj)
        for ij in Fileobj:
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
    return Response({
                    'status':200,
                    'userDetail':filterUser[0],
                    'message':'files Got successfully ',
                    'data':specificuserLoggedIn
                })

import os
import datetime
import glob
import sys
from pathlib import Path
def DeleteFiles(request):

    BASE_DIR = Path(__file__).resolve().parent.parent
    print(BASE_DIR)
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

    return Response({
                    'status':200,
                    'message':'files delete function successfully'
                })
