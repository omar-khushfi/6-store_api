
from django.urls import path,include
from .views import *
urlpatterns = [
   path('products/',get_all_products,name='products'),
   path('product/<int:pk>/',get_product,name='product'),
   path('update/product/<int:pk>/',update_product,name='update'),
    path('delete/product/<int:pk>/',delete_product,name='delete'),
   path('new/product/',new_product,name='newproduct'),
       path('add/review/<int:pk>/',add_review,name='review'),
         path('review/delete/<int:pk>/',delete_review,name='delete_review'),


]

