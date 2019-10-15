from django.urls import path

from . import views

urlpatterns = [
    path('', views.LoginFormView.as_view(), name='index'),
    path('login', views.LoginFormView.as_view(), name='login'),
    path('addUser', views.AddUserFormView.as_view(), name='addUser')
]
