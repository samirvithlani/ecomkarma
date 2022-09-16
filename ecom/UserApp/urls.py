from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth.views import LogoutView
app_name = 'user'
urlpatterns = [
 
 path('register/',views.UserRegisterView.as_view(),name='register'),
 path('login/',views.UserLogin.as_view(),name='userlogin'),
 #path('logout/',LogoutView.as_view(template_name="products/productlist.html"),name='logout'),
 path('logout/',views.UserLogoutView.as_view(),name='logout'),
]