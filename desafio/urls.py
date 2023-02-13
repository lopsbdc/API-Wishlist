"""desafio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from rest_framework.authtoken import views
from clientes.api.viewsets import ClientesViewset
from produto_favorito.api.viewsets import ProdutoViewset
from produto_favorito.api.Excel import Relatorio_excel
from frontend.api.viewsets import Produto_ClienteViewset

router = routers.DefaultRouter()
router.register(r'clientes', ClientesViewset)
router.register(r'produto', ProdutoViewset)
router.register(r'excel', Relatorio_excel)
router.register(r'produto_cliente', Produto_ClienteViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
]
