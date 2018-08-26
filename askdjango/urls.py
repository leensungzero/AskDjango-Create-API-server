from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
    
    path('sample/', include('sample.urls')),
    path('ep03/', include('ep03.urls')),
    path('ep04/', include('ep04.urls')),
    path('ep06/', include('ep06.urls')),
    path('ep08/', include('ep08.urls')),

    path('api/', include('api.urls')),
]
