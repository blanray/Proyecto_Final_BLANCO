from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __srt__(self):
        return f'Imagen para el usuario: {self.user.username}'
    
