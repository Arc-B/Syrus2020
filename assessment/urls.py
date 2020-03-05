from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='test-home'),
    path('index/',views.index, name= 'test-index'),
    path('about/', views.about, name='test-about'),
]
