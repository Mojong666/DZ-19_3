from django.contrib import admin
from django.urls import path
from task1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page, name='main_page'),
    path('store/', views.store_page, name='store_page'),
    path('cart/', views.cart_page, name='cart_page'),
    path('register/', views.registration_page, name='registration_page'),
]
