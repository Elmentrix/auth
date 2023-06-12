from django.urls import path
from . import views

# creating the urls for the templates
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('forget_password/', views.forget_password, name='forget_password')
]