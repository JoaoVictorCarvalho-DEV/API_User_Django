from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

import json

@api_view(['GET','POST', 'PUT', 'DELETE'])
def user_get(request):

#Pegando Dados

    if request.method == 'GET':
        try:
            user = User.objects.all()

            serializer = UserSerializer(user, many=True)

            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

#Criando Dados

    if request.method == 'POST':

        new_user = request.data

        serializer = UserSerializer(data=new_user)
        
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)

#Editando Dados
   
    if request.method == 'PUT':

        name = request.data('user_name')
        try:
            updated_user = User.objects.get(pk=name)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(updated_user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)

#Deletando Dados

    if request.method == 'DELETE':
        try:
            user_to_deleted = User.objects.get(pk=request.data['user_name'])
            user_to_deleted.delete()

            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)