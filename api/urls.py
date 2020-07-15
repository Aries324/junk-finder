from django.conf.urls import include, url

from api.views import MyUserViewSet, ItemPostViewSet

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'my_user', MyUserViewSet)
router.register(r'item_post', ItemPostViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls))
]