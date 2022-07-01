from django.urls import path

from . import views as v

app_name='produto'

urlpatterns = [
    path('', v.produto_list, name='url_produto_list'),
    path('<int:pk>/', v.produto_detail, name='url_produto_detail'),
    path('add/', v.ProdutoCreate.as_view(), name='url_produto_add'),
    path('<int:pk>/edit', v.ProdutoUpdate.as_view(), name='url_produto_edit'),
    path('<int:pk>/json/', v.produto_json, name='url_produto_json'),
]
