from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'posts'

urlpatterns = [
   path('<slug:username>/', views.PostList.as_view(), name = 'all'),
   path('new/', views.CreatePost.as_view(), name = 'create'),
   path('by/<slug:username>/', views.UserPosts.as_view(), name = 'for_user'),
   path('by/<slug:username>/<int:pk>', views.PostDetail.as_view(), name = 'single'),
   path('delete/<int:pk>/', views.DeletePost.as_view(), name = 'delete'),

]