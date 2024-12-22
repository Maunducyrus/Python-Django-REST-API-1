from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer


# Create your views here.
@api_view(['GET'])
# defining endpoint function

def get_user(request):
    return Response(UserSerializer({'name': "Cyrus", "age": 34}).data)

@api_view(['POST'])
def Create_user(request):
    # serializer is used for sending data the conditions are checked
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)