from usuarios import models
from rest_framework import viewsets
from usuarios.api import serializers

class UsuariosViewset(viewsets.ModelViewSet):
    serializer_class = serializers.UsuariosSerializer
    queryset = models.Usuarios.objects.all()