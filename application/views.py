from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import Serializer

from .models import User
from .serializer import UserSerializer


# Create your views here.
@api_view(['GET'])
# defining endpoint function

def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(users, safe=False)
    # return Response(Serializer.data)

@api_view(['POST'])
def create_user(request):
    # serializer is used for sending data the conditions are checked
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)