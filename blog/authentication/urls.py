from django.urls import path
from rest_framework import routers

from blog.authentication import views

router = routers.SimpleRouter()

urlpatterns = [
    path("register/", views.RegisterUserView.as_view()),
    path("login/", views.login_view),
    path("logout/", views.logout_view),
    path("set-csrf/", views.set_csrf_token),
]
