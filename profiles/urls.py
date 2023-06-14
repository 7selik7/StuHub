from django.urls import path
from . import views

app_name = 'profiles'


urlpatterns = [
    path('home/', views.home, name='home'),
    path('myorders/', views.myorders, name='myorders'),
    path('mytasks/', views.mytasks, name='mytasks'),
    path('chat/', views.chat, name='mychat'),
    path('<str:profile_name>/', views.profile, name='profile'),
]

