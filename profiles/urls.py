from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('<int:profile_id>/', views.profile, name='profile'),
    # ...
]

