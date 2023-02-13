# Viewset e Serializer
from rest_framework.viewsets import ModelViewSet
from produto_favorito.models import Produto
from produto_favorito.api.serializer import ProdutoSerializer

# Conferir a API challenge + Respostas
from rest_framework.response import Response
import json
from urllib.request import urlopen

# Autenticacao
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Habilitar busca
from rest_framework.filters import SearchFilter

# Otimizar a busca dentro da API
from django_auto_prefetching import AutoPrefetchViewSetMixin




class Produto_ClienteViewset(AutoPrefetchViewSetMixin, ModelViewSet):

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer    
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    http_method_names = ['get']

    #Habilitando a opcao de filtrar na API
    filter_backends = (SearchFilter,)
    #os dois underlines eh para buscar o email na foreign key. = eh de exato
    search_fields = ('=email__email', '=produto')

    
    def list(self, request):
        i = 0
        valor = str(request)
        email1 =  valor.replace("<rest_framework.request.Request: GET '/produto_cliente/?search=","")
        email = email1.replace("'>","")

        total = []
        queryset = Produto.objects.filter(email__email=email)
        tamanho = len(queryset)


        while i < tamanho:
            
            produto = queryset[i]
            url = "http://challenge-api.luizalabs.com/api/product/" + str(produto) + "/"

            #abrindo a API pelo ID do produto
            consulta = urlopen(url)
            dados = json.loads(consulta.read())

            #validador
            preco = str(dados["price"])
            titulo = str(dados['title'])
            imagem = str(dados['image'])
            try:
                review = str(dados['reviewScore'])
            except:
                review = "null"
            
            
            if review != "null":
                total.append("Produto: " + titulo + "; Preco: " + preco + "; Imagem: " + imagem + "; Avaliacao: " + review)
            
            else:
                total.append("Produto: " + titulo + "; Preco: " + preco + "; Imagem: " + imagem)

            i = i + 1

        return Response(total)
    
