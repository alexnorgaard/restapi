from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import *
from .models import *
from django.contrib.auth.models import User
from django.db.models import Q


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer


class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all().order_by('user1')
    serializer_class = FriendSerializer


class FriendsList(viewsets.ModelViewSet):
    serializer_class = FriendSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Friend.objects.filter(Q(user1=user) | Q(user2=user))
        return queryset


class FriendsListWithID(generics.ListAPIView):
    serializer_class = FriendSerializer

    def get_queryset(self):
        userId = self.kwargs['userid']
        queryset = Friend.objects.filter(Q(user1_id=userId) | Q(user2_id=userId))
        return queryset

"""
class FriendsMaualList(generics.ListAPIView):
    serializer_class = FriendManualSerializer
    queryset = Friend.objects.all().order_by('user1')
"""
