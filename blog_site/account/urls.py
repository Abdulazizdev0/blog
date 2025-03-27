from .views import register,log_in,log_out
from django.urls import path

urlpatterns = [
    path('register/',register,name = 'register'),
    path('login/',log_in,name = 'login'),
    path('logout/',log_out,name = 'logout')
]