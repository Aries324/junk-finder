from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.serializers import  ModelSerializer

from junkapp.models import MyUser, ItemsPost

class MyUserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = ('email', 'name', 'phone')

class ItemPostSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ItemsPost
        fields = (
            'claimed',
            'description',
            'title',
            'email',
            'address',
            'items'
        )
