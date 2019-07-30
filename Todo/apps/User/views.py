from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from .serializers import Signupserializer, Loginserializer
from rest_framework.permissions import IsAuthenticated

class SignupView(APIView):

    
        
    """
    #list all objects
    def get(self,request):
        signup= User.objects.all()
        serializer = Signupserializer(signup)
        return Response(serializer.data)
     """   
    
    # create objects
     
    def post(self, request):
        print(request.data )
        #
        # import pdb;pdb.set_trace()
        serializer = Signupserializer(data=request.data)
        print(serializer.is_valid(raise_exception = True))
        user = serializer.save()
        user.set_password(serializer.validated_data.get('password'))
        user.save()
        token, created= Token.objects.get_or_create(user=user)
        data= serializer.data
        data['token'] = token.key
        
        return Response({"data" :data})

class LoginView(APIView):


    def post(self,request):
        
        serializer = Loginserializer(data= request.data)
        serializer.is_valid(raise_exception = True)
        #accessing deserialized data
        user = serializer.validated_data['user'] 
        token,created = Token.objects.get_or_create(user=user)
        
        data= serializer.data  # data saved in a dictionary named data
        data['token'] = token.key  # appending token to dictionary
        return Response({"data" :data})


