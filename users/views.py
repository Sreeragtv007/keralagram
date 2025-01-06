from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from users.serializers import ProfileSerializer, commentSerializer, postSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .models import Profile, Post, likePost
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
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data

        serializer = postSerializer(data=data, context={'request': request})

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response({"message": "post uploaded"}, status=status.HTTP_201_CREATED)


class post(APIView):

    def get(self, request):
        serializer = postSerializer(Post.objects.all(), many=True)
        return Response(serializer.data)


class postComment(APIView):

    def post(self, request, pk):

        post = Post.objects.get(id=pk)

        data = request.data

        serializer = commentSerializer(data=data, context={"post": post})

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class likePost(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        print(post)
        
        like = likePost.objectts.create
        
        print(like)

        
        return Response("liked", status=status.HTTP_201_CREATED)
