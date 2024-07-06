
from rest_framework import serializers
from BuddyHome.models import Buddy_S_User

class webuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buddy_S_User
        fields = '__all__'