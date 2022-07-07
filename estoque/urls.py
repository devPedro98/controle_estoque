from django.urls import path

from estoque import views as v

app_name = 'estoque'

urlpatterns = [
    path('', v.EstoqueEntradaList.as_view(), name='url_estoque_entrada_list'),
    path('<int:pk>/', v.EstoqueDetail.as_view(), name='url_estoque_detail'), # noqa
    path('add/', v.estoque_entrada_add, name='url_estoque_entrada_add'),
    path('saida/', v.EstoqueSaidaList.as_view(), name='url_estoque_saida_list'), # noqa
    path('saida/add/', v.estoque_saida_add, name='url_estoque_saida_add'),
]
