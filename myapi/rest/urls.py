from django.urls import include, path, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'friends', views.FriendViewSet)
router.register(r'friendslist', views.FriendsList, basename='friendslist')

urlpatterns = [
    # path('manualFriends/', views.FriendsMaualList.as_view()),
    path('friendslist/<userid>/', views.FriendsListWithID.as_view()),  # Show all friends for user with provided userID
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
