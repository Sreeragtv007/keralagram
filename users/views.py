from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from users.serializers import ProfileSerializer, postSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
# from .models import Users
# Create your views here.


class userRegistration(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data

        serializer = ProfileSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response("created", status=status.HTTP_201_CREATED)


class uploadPost(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        
        serializer = postSerializer(data=data,context={'request': request})
        
        serializer.is_valid(raise_exception=True)
        
        serializer.save()
        
       
        return Response(serializer.data, status=status.HTTP_201_CREATED)
