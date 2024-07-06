from django.contrib import admin

from BuddyHome.models import Buddy_S_User,Contact

# Register your models here.
@admin.register(Contact)
class ContactAll(admin.ModelAdmin):
    list_display = ['email','name','contactno','query']

@admin.register(Buddy_S_User)
class CustomProjects(admin.ModelAdmin):
    model = Buddy_S_User
    list_display = ('B_Userid','u_ID','usertype')
    list_filter = ('usertype',)
    