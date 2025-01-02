from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.serializers import ProfileSerializer
# from .models import Users
# Create your views here.


def index(request):
    return HttpResponse("test")


class userRegistration(APIView):

    def post(self, request):
        data = request.data

        serializer = ProfileSerializer(data=data)
        
        serializer.is_valid(raise_exception=True)
        
        serializer.save()
        
        return Response("created",status=status.HTTP_201_CREATED)
