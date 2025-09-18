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
]