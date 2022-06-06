from apps.clients.views import login_view, register_user
# from clients import views

from django.urls import path
#from .views import login_view, register_user
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),
]
