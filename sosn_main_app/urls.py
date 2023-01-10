
from django.urls import path, include
from sosn_main_app import views

urlpatterns = [
    # programs path
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact')

]
