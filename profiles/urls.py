from django.urls import path
from . import views

app_name = 'profiles'


urlpatterns = [
    path('home/', views.home, name='home'),
    path('myorders/', views.myorders, name='myorders'),
    path('<str:profile_name>/', views.profile, name='profile'),
]

