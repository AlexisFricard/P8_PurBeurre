""" URL Configuration for web app """

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('selection', views.selection, name='selection'),
    path('result', views.result, name='result'),
    path('save', views.save, name='save'),
    path('legal_notices', views.legal_notices, name='legal_notices'),
]
