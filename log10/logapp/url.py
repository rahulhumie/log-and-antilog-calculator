from django.urls import path
from . import views
from .views import logbase10
urlpatterns = [
     
    path('',views.logbase10 )
]
