from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.create_order, name='create_order'),
    path('execute_order/<int:order_id>/', views.execute_order, name='execute_order'),
    path('make_chat/<int:order_id>/', views.make_chat, name='make_chat'),
    path('delete_order/<int:order_id>/', views.delete_order, name='delete_order'),
]

