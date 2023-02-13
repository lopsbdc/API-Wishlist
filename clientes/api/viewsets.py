from rest_framework.viewsets import ModelViewSet
from clientes.models import Clientes
from .serializer import ClientesSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Otimizar a busca dentro da API
from django_auto_prefetching import AutoPrefetchViewSetMixin


class ClientesViewset(AutoPrefetchViewSetMixin, ModelViewSet):

    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)