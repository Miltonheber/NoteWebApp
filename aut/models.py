from django.db import models
from django.contrib.auth.models import User



class UserInfo(models.Model):
    email = models.EmailField(max_length=50, null=False, unique=True)
    nome = models.CharField(null=False, max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

        
    
