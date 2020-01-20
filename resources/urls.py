from django.urls import path

from . import views

urlpatterns = [
    path('', views.host),
    path('host', views.host),
]