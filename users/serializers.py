from rest_framework import serializers
from .models import Post, Profile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = "__all__"

    def validate(self, attrs):

        return super().validate(attrs)

    def create(self, validated_data):

        user_data = validated_data.pop('user')

        user = User.objects.create_user(**user_data)

        profile = Profile.objects.create(user=user, **validated_data)
        return profile


class postSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

    def create(self, validated_data):

        user = self.context['request'].user
        profile = Profile.objects.get(user=user)
        validated_data['profile'] = profile

        return super().create(validated_data)
