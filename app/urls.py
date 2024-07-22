from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot, name='chatbot'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('chat-history/', views.chat_history, name='chat_history'),
    path('chat-history/delete/', views.delete_history, name='delete_history'),
    path('logout', views.logout, name='logout'),
]