from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('fridrih_engels', views.fridrih_engels)
]
