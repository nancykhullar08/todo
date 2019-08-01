from rest_framework import serializers
from rest_framework.serializers import ValidationError
from rest_framework.response import Response
from .models import User
from django.contrib.auth import authenticate


class Signupserializer(serializers.ModelSerializer):
    """
    Serializer used for Sign Up
    """
    

    class Meta:
        model= User
        fields= ('email','username','password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, email):

        """
        Method used for validating email address.
        """
        email=email.lower()
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email already registered.')
        return email

    def password_len(self,password):
        
        """
        Method used for checking password length.
        """
     
        #confirm_password = self.context.get('confirm_password')
        if len(password) < 8 :
            raise serializers.ValidationError('length should be greater than 8.')
        return password

       
    
    def validate(self,attr):
        """
        Method used for confirm password.
        """
        confirm_password = self.context.get('confirm_password')
        if attr['password'] != confirm_password:
            raise ValidationError("password and confirm_password does not match")
        
        return attr
    
   

class Loginserializer(serializers.Serializer):
    """
    Serializer used for LogIn User data.
    """

    password=serializers.CharField()
    username=serializers.CharField()
    
   

    
    def validate(self,attrs):  
        #attrs is a dictionary
        """
        Method used for validating User data.
        
        param : attrs is a dictionary that contains user data.
        return : attrs
        """
        
        username=attrs.get("username")
        password = attrs.get("password")

        #using django authenticate method for validating user credentials
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
