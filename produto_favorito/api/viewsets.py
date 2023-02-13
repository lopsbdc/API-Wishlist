# Viewset e Serializer
from rest_framework.viewsets import ModelViewSet
from produto_favorito.models import Produto
from .serializer import ProdutoSerializer

# Conferir a API challenge + Respostas
from rest_framework.response import Response
import rest_framework.status as status
import json
from urllib.request import urlopen

# Autenticacao
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Habilitar busca
from rest_framework.filters import SearchFilter

# Otimizar a busca dentro da API
from django_auto_prefetching import AutoPrefetchViewSetMixin




class ProdutoViewset(AutoPrefetchViewSetMixin, ModelViewSet):

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer    
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    #Habilitando a opcao de filtrar na API
    filter_backends = (SearchFilter,)
    #os dois underlines eh para buscar o email na foreign key. = eh de exato
    search_fields = ('=email__email', '=produto')

    
    #Validar diretamente na API se o produto existe, ou nao

    def create(self, request, *args, **kwargs):
        produto = request.data['produto']

        url = "http://challenge-api.luizalabs.com/api/product/" + produto + "/"

        #abrindo a API pelo ID do produto
        consulta = urlopen(url)
        dados = json.loads(consulta.read())

        #validador
        preco = dados["price"]
        serializer = ProdutoSerializer(data=request.data)
        
        #se for nulo, e porque nao existe. 
        if preco != 'null':
            
            #viu que nao e nulo, salva no banco!
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            else:
                #viu que e nulo, ou que nao foi localizado, nao salva!
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

    #Validar diretamente na API se o produto existe, ou nao, agora na hora de att um registro
    def update(self, request, *args, **kwargs):
        produto = request.data['produto']

        url = "http://challenge-api.luizalabs.com/api/product/" + produto + "/"

        #abrindo a API pelo ID do produto
        consulta = urlopen(url)
        dados = json.loads(consulta.read())

        #validador
        preco = dados["price"]

        #salvando os dados recebidos em uma variavel
        serializer = ProdutoSerializer(data=request.data)
        
        #se for nulo, e porque nao existe. 
        if preco != 'null':
            
            #viu que nao e nulo, salva no banco!
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            else:
                #viu que e nulo, ou que nao foi localizado, nao salva!
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
