
from django.urls import path,include
from .views import *
urlpatterns = [
  
    path('order/new/',new_order,name="neworder"),
    path('order/<int:pk>/',get_order,name="order"),
    path('orders/',get_orders,name="getorders"),
    path('order/process/<int:pk>/',update_order,name="processorder"),
    path('order/delete/<int:pk>/',delete_order,name="deleteorder"),

]

