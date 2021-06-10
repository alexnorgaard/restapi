from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.db import transaction


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'id', 'url')


class FriendSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Friend
        fields = ('user1', 'user2', 'url')

"""
class FriendManualSerializer(serializers.Serializer):
    user1 = serializers.CharField(max_length=50)
    user2 = serializers.CharField(max_length=50)
    url = serializers.CharField(max_length=200)

    @transaction.atomic
    def update(self, instance, validated_data):
        instance.user1 = validated_data.get('user1', instance.user1)
        instance.user2 = validated_data.get('user2', instance.user2)
        # Not changing url as it is from primary key, which is not manually set, but auto-incremented
        instance.save()

        return instance

    @transaction.atomic
    def create(self, validated_data):

        return Friend.objects.create(**validated_data)
"""




