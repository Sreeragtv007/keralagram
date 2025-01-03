from django.urls import path,include
from .views import index,userRegistration

urlpatterns = [
    path('index/',index.as_view()),
    path('register/',userRegistration.as_view()),
]