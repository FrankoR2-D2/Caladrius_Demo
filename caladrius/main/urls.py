from django.urls import path 

from . import views 

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("<int:id>", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("signout/", views.signout, name="signout"),
    path("signedIn/", views.signedIn, name="signedIn"),
    path('showtodo/', views.showtodo, name="showtodo"),
    path('rqst_appment/<int:id>', views.rqst_appment, name="request_appointment"),
    path('display_apm/', views.display_apm, name="display_apm"),
]
