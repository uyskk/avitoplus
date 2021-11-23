from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import register_view
from .forms import LoginForm


urlpatterns = [
    path('register/', register_view, name="register"),
    path('login/', LoginView.as_view(template_name="registration/login.html", authentication_form=LoginForm), name="login"),
    path('logout/', LogoutView.as_view(), name="logout")
]
