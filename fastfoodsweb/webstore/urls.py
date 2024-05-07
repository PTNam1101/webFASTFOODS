from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('category/<int:pk>', views.allInCategory, name = 'allInCategory'),
    path('searched/', views.searched, name = 'searched'),
    path('about/', views.about, name = 'about'),
]
