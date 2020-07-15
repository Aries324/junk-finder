from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from api.serializers import MyUserSerializer, ItemPostSerializer
from junkapp.models import MyUser, ItemsPost

class MyUserViewSet(ModelViewSet):
    serializer_class = MyUserSerializer
    basename = 'my_user'
    queryset = MyUser.objects.all()

class ItemPostViewSet(ModelViewSet):
    serializer_class = ItemPostSerializer
    basename = 'item_post'
    queryset = ItemsPost.objects.all()


