from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('entries/', views.view_entries, name='view_entries'),
    path('dashboard/', views.mood_dashboard, name='mood_dashboard'), 
    path('register/', views.register, name='register'),
    path('home/', views.home_view, name='home'),
    path('entries/<int:pk>/', views.entry_detail, name='entry_detail'),
    path('deleteentry/<int:pk>/', views.delete_entry, name='delete_entry'),
    # Parent routes
    path("redirect/",views.role_redirect, name="role_redirect"),
    path("parent/", views.parent_dashboard, name="parent_dashboard"),
    path("parent/chat/", views.parent_chat, name="parent_chat"),
    path("parent/chat/delete/", views.delete_parent_chats, name="delete_parent_chats"),


]