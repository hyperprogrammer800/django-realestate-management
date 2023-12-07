from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tenant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50, null=True)
    documents =  models.FileField(upload_to='document_files', null=True)

    def __str__(self):
        return f'Tenant {self.user.username}'