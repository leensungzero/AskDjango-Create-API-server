from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'ep08'

router = routers.DefaultRouter()
router.register('post', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
