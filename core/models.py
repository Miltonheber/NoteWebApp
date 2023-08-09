from django.db import models
from django.contrib.auth.models import User
class Nota(models.Model):
    titulo = models.CharField('título', max_length=50, null=False)
    corpo = models.TextField('título', null=False)
    data = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    
