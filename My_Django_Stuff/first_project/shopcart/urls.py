from django.urls import path

from .views import shopping_cart,update,delitem


urlpatterns = [
    path('',shopping_cart,name='shopcart'),
    path('update/',update,name='update'),
    path('delitem/',delitem,name='delitem'),
]
