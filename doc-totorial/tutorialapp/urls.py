from django.urls import path,include
from rest_framework import routers
from . import views
# create router 
router = routers.DefaultRouter()
router.register(r"users",views.UserViewSet)
router.register(r"groups",views.GroupViewSet)

urlpatterns = [
    path('',include(router.urls)),
]