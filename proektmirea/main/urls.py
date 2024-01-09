from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "home"),
    path('fridrih_engels', views.fridrih_engels, name = "f_eng"),
    path('karl_marks', views.karl_marks, name = "k_mar"),
    path('ilych_lenin', views.ilych_lenin, name = "i_len"),
]
