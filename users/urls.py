from django.urls import path,include
from .views import uploadPost,userRegistration

urlpatterns = [
    path('upload/',uploadPost.as_view()),
    path('register/',userRegistration.as_view()),
]