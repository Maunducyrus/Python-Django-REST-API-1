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
    return Response(UserSerializer({'name': "Cyrus", "age": 34}))
