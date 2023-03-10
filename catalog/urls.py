from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('add', views.add_task, name='add_task'),
    path('', views.catalog, name='catalog'),
    path('task/<int:id>', views.catalog, name='task'),
]
