from django.contrib import admin
from django.urls import path

import accounts
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", accounts.views.index, name="index"),
    path("accounts/login", views.login, name="login"),
    path("accounts/logout", views.logout, name="logout"),
    path("accounts/callback", views.callback, name="callback"),
]
