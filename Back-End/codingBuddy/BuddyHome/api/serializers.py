from rest_framework import serializers
from BuddyHome.models import Buddy_S_User,Contact
from random import randint
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class RegistrationwebuserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = Buddy_S_User,User
        fields = ['email','name','password','password2']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def random_with_N_digits(self,n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return randint(range_start, range_end)

    def save(self):
        username = 'U'+ self.validated_data['email']+str(self.random_with_N_digits((len(self.validated_data['email'])%5)+1))
        password1 = self.validated_data['password']
        password2 = self.validated_data['password2']
        if self.validated_data['email'] > 150:
            raise serializers.ValidationError({'Email':'Your email name must be under 150 characters'})            

        if password1 != password2:
            raise serializers.ValidationError({'passsowrd':'Passsword must match.'})

        loguser = User.objects.create_user(username, self.validated_data['email'], password1)
        loguser.save()

        webus = Buddy_S_User(
            user = loguser,
            Susername = username,
            name = self.validated_data['name'],
            email = self.validated_data['email'],
            password = password1
        )
        webus.save()
        return webus

class RegisterSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model = Buddy_S_User
        fields = ['u_ID','email','name','password','password2','usertype']

class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields = ['email','password']




# {
# "email" : "rrr10701@gmail.com",
# "name" : "Riti",
# "password" : "1234",
# "password2" : "1234",
# }


class ContactSerializer(serializers.Serializer):
    email =       serializers.EmailField()
    name =        serializers.CharField(max_length=50)
    phone_regex = RegexValidator(regex = r'^\+?1?\d{10}$',message = "The format should be exactly be of 10 digits"   )
    contactno =   serializers.CharField(max_length=25,validators=[phone_regex])
    query =       serializers.CharField(max_length=10000)

    def create(self,validated_data):
        return Contact.objects.create(**validated_data)