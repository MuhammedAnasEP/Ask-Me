from django.urls import path
from . import views

urlpatterns = [   
    path("login", views.signin, name="loginPage"),
    path("signup", views.signup, name="signupPage"),
    path("signout", views.signout, name="signout"),
    path("profile",views.profile,name="profile"),
]