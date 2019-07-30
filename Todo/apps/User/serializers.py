from rest_framework import serializers
from rest_framework.serializers import ValidationError


from rest_framework.response import Response
from .models import User
from django.contrib.auth import authenticate

class Signupserializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, min_length=3, max_length=70)
    password = serializers.CharField(required=True, min_length=8, max_length=20)

    class Meta:
        model= User
        fields= ['email','username','password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, email):
        email.lower()
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email already registered.')
        return email

    def password_length(self, password):
        #pwd = User.objects.filter(password=password)
        if len(password) < 8 :
            raise serializers.ValidationError('length should be greater than 8.')
        return password

class Loginserializer(serializers.ModelSerializer):
    password=serializers.CharField()
    username=serializers.CharField()
   

    class Meta:
        model = User
        fields=['username','password']
    
    def validate(self,attrs):  #attrs is a dictionary
        # import pdb;pdb.set_trace()
        username=attrs.get("username")
        password = attrs.get("password")
        user= authenticate(username=username, password = password)

        if user is not None:
            attrs['user'] = user
            
        
        else:
            raise serializers.ValidationError('Wrong credentials')
            
        return attrs



    
























"""class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        """
