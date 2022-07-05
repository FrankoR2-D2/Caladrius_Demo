from django.urls import path 
from . import views 


urlpatterns = [
    path("register/", views.register, name="register"),
    path('loginPage/', views.user_login, name="login"),
    path('addPatient/', views.addPatient, name="addPatient"),  
      
]
