from django.core import serializers as core_serializers
from rest_framework import serializers
from produto_favorito.models import Produto
from clientes.models import Clientes

class ProdutoSerializer(serializers.ModelSerializer):

    #Mostrar os emails na consulta da API, bem como ignorar o POST por ID e tratar somente pelo 'email'
    email = serializers.SlugRelatedField(slug_field='email', read_only=False, queryset=Clientes.objects.all())

    class Meta:
        model = Produto
        fields = ('id', 'email', 'produto')

