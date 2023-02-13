from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

app_name = 'users'

urlpatterns = [
    path('singup/volunteer', views.reg_volunteer, name='reg_vol'),
    path('singup/validator', views.reg_validator, name='reg_val'),
    path('singup/organization', views.reg_organization, name='reg_org'),
    path('login', LoginView.as_view(template_name='users/login.html'), name='login'),
]
