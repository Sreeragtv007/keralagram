from rest_framework import serializers
from .models import Post, Profile, likePost, postCommets
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['user',]
        

    def validate(self, attrs):

        return super().validate(attrs)

    def create(self, validated_data):

        user_data = validated_data.pop('user')

        user = User.objects.create_user(**user_data)

        profile = Profile.objects.create(user=user, **validated_data)
        return profile
    
    
    

class commentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = postCommets
        fields = ['comment']
        
    def create(self, validated_data):
        validated_data['post'] = self.context['post']
        return super().create(validated_data)

class likeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = likePost
        fields = ['like']
        depth = 1
        
        

class postSerializer(serializers.ModelSerializer):
    comments = commentSerializer(many=True, read_only=True)
    profile = ProfileSerializer(read_only = True)
    likes = likeSerializer(many=True, read_only=True)    
    class Meta:
        model = Post
        fields = "__all__"
    
    
    
    def to_representation(self, instance):
        repre = super().to_representation(instance)
        
        repre['test'] = f"{instance.title}"
        
        return repre    

    def create(self, validated_data):

        user = self.context['request'].user
        profile = Profile.objects.get(user=user)
        validated_data['profile'] = profile

        return super().create(validated_data)
    
    


