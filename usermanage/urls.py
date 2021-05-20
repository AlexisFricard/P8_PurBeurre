from django.urls import path

from . import views

urlpatterns = [
    path("account", views.account, name='account'),
    path("signup", views.signup, name='signup'),
    path("signin", views.signin, name='signin'),
    path("log_out", views.log_out, name='log_out'),
    path("myfood", views.myfood, name='myfood'),
]
