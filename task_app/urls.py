from django.urls import path
from .views import create,show_task,update_task,delete_task

urlpatterns = [
    path('create/',create, name='create_task'),
    path('show/', show_task, name='list'),
    path('update/<int:pk>/', update_task, name='update_task'),
    path('delete/<int:pk>/', delete_task, name='delete_task'),
]