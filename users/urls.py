from django.urls import path,include
from .views import uploadPost,userRegistration,postComment,post,likePost

urlpatterns = [
    path("",post.as_view()),
    path('upload/',uploadPost.as_view()),
    path('register/',userRegistration.as_view()),
    path('addcomment/<str:pk>/',postComment.as_view()),
    path('addcomment/<str:pk>/',postComment.as_view()),
    path('likepost/<str:pk>/',likePost.as_view()),
]