from django.urls import path, include
from rest_framework import routers
from . import views


app_name = 'ep04'

router = routers.DefaultRouter()
router.register('post', views.PostViewSet) # 2개의 URL을 처리하는 뷰함수를 만들어서 등록

urlpatterns = [
    path('', include(router.urls)),
    # path('post/', views.post_list),
    # path('post/<int:pk>/', views.post_detail),
]