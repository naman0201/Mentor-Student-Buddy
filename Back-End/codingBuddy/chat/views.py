from django.shortcuts import render

# Create your views here.
def messagepage(request):

    return render(request,'message.html')