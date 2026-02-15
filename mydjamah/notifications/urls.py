from django.urls import path
from . import views
from .views import  redirect_notification



app_name = 'notifications'

urlpatterns = [
    path('', views.notification_list, name='list'),
    path('read/<int:pk>/', views.mark_as_read, name='mark_as_read'),
    path('redirect/<int:pk>/', redirect_notification, name='redirect'),
    path('redirect/<int:pk>/', redirect_notification, name='redirect'),



    
]