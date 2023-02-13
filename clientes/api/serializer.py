from rest_framework.serializers import ModelSerializer
from clientes.models import Clientes

class ClientesSerializer(ModelSerializer):
    class Meta:
        model = Clientes
        fields = ('id', 'email', 'nome')