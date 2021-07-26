from django.db import models
from uuid import uuid4

# Create your models here.


class Usuarios(models.Model):
    id_usuario = models.UUIDField( primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
       
