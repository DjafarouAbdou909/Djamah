from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/create/', views.create_posts, name='create_posts'),
    path('post/<int:post_id>/like/', views.create_likes, name='create_likes'),
    path('post/<int:post_id>/comment/', views.create_comments, name='create_comments'),
    path('comment/<int:comment_id>/reply/', views.replies_comments, name='replies_comments'),
]