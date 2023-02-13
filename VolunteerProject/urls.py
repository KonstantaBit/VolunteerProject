from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('users/', include('users.urls')),
    path('catalog', include('catalog.urls')),
    path('', include('django.contrib.auth.urls')),
]
