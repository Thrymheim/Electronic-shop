from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('contact-us', views.conatact_page, name='conatact-us'),
    ]
