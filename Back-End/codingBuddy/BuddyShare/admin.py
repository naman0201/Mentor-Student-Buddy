import imp
from django.contrib import admin

# from .models import FilesShare,jointable
from .models import *
# Register your models here.
admin.site.register(Files)
admin.site.register(Folder)
admin.site.register(FileData)
