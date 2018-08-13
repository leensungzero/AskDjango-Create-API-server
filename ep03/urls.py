from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', views.UserViewSet)
router.register('post', views.PostViewSet)

app_name = 'ep03'

urlpatterns = [
    # path('post/', views.PostListAPIView.as_view()),
    # path('post/<int:pk>/', views.PostDetailAPIView.as_view()),

    # path('user/', views.user_list),
    # path('user/<int:pk>', views.user_detail),
    path('', include(router.urls)),
]