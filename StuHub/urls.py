from django.contrib import admin
from django.urls import path, include

import accounts
from accounts import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", accounts.views.index, name="index"),
    path("accounts/", include('accounts.urls')),
    path('profiles/', include('profiles.urls')),
    path('orders/', include('orders.urls'))
]
