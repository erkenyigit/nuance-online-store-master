"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path

from django.urls import include
from first_app.views import user_login, index, user_logout
from product_app.views import ProductDetailView, product_detail_view, ProductListView, ProductDetailSlugView, \
    BodyCareListView, SkinCareListView, TonicListView, CreamListView, FaceSetListView, HairCareListView
from shopcart.views import shopping_cart, update

urlpatterns = [
    path('', index, name='index'),
    # path('product_app/',include('product_app.urls')),
    path('product_app/<int:id>', ProductDetailView.as_view()),
    # path('products/<slug:slug>/',ProductDetailSlugView.as_view(),name='slugview'),
    # path('register/',register,name='register'),
    path('products/', ProductListView.as_view(), name='products'),
    # path('products/<int:pk>',ProductDetailView.as_view()),
    path('login/', user_login, name='user_login'),
    path('admin/', admin.site.urls),
    path('logout/', user_logout, name='logout'),
    path('search/', include("search.urls"), name='search'),
    # path('special/',views.special,name='special'),
    path('products/skincare/', SkinCareListView.as_view(), name='skincare'),
    path('products/bodycare/', BodyCareListView.as_view(), name='bodycare'),
    path('products/tonic/', TonicListView.as_view(), name='tonic'),
    path('products/cream/', CreamListView.as_view(), name='cream'),
    path('products/faceset/', FaceSetListView.as_view(), name='faceset'),
    path('products/haircare/', HairCareListView.as_view(), name='haircare'),
    path('shopping_cart/', include("shopcart.urls"), name='shopcart'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
