from django.contrib import admin
from .models import Profile,Post,postCommets,likePost
# Register your models here.


admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(postCommets)
admin.site.register(likePost)