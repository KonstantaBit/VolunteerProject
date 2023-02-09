from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('singup/', views.register, name='register'),
]
