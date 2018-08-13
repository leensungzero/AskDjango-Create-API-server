from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


app_name = "sample"


# router = DefaultRouter()
# router.register('posts', views.PostViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('post/', views.PostListAPIView.as_view())
]
