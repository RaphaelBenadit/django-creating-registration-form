from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage URL
    path('register/', views.register, name='register'),
    path('success/', views.success, name='success'),
]
