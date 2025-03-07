from django.urls import path


from .views import maqola

urlpatterns = [
    path('',maqola,name = 'maqola')
]