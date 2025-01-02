from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    
    name = models.CharField(max_length=50)
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    phone_number = models.IntegerField(blank=True, null=True)
    
    email = models.EmailField(max_length=254,blank=True, null=True)
    
    profile_image = models.ImageField(upload_to='profile_image',blank=True, null=True)
    
    created = models.DateField(auto_now_add=True,blank=True, null=True)
    
    updated = models.DateTimeField(auto_now=True,blank=True, null=True)
    
    
    def __str__(self):
        return self.name
    
    
    