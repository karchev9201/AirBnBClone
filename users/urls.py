from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.Logout.as_view(), name="logout"),
    path("sign", views.SignView.as_view(), name="sign"),
]
