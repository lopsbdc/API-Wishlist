from rest_framework.viewsets import ReadOnlyModelViewSet
from drf_excel.mixins import XLSXFileMixin
from drf_excel.renderers import XLSXRenderer

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from produto_favorito.models import Produto
from produto_favorito.api.serializer import ProdutoSerializer



class Relatorio_excel(XLSXFileMixin, ReadOnlyModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


    renderer_classes = [XLSXRenderer]

    filename = 'exporta_BD_produto.xlsx'