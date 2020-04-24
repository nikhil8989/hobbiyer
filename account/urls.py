from django.urls import path
from account import views

app_name = 'account'

urlpatterns = [
    path("signup/",views.register,name="signup"),
]