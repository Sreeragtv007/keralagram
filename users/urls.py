from django.urls import path,include
from .views import index,userRegistration

urlpatterns = [
    path('',index),
    path('register/',userRegistration.as_view()),
]