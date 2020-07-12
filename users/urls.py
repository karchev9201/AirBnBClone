from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login", views.LoginView.as_view(), name="login"),
    path("login/github", views.github_login, name="github-login"),
    path("login/github/callback", views.github_callback, name="github-callback"),
    path("logout", views.Logout.as_view(), name="logout"),
    path("sign", views.SignView.as_view(), name="sign"),
    path("verify/<str:key>", views.complete_verification, name="verify",),
]
