from django.urls import include, path

from estoque import views as v

app_name = 'estoque'

entrada_patterns = [
    path('', v.EstoqueEntradaList.as_view(), name='url_estoque_entrada_list'),
    path('<int:pk>/', v.EstoqueDetail.as_view(), name='url_estoque_detail'), # noqa
    path('add/', v.estoque_entrada_add, name='url_estoque_entrada_add'),
]

saida_patterns = [
    path('', v.EstoqueSaidaList.as_view(), name='url_estoque_saida_list'), # noqa
    path('add/', v.estoque_saida_add, name='url_estoque_saida_add'),
]

urlpatterns = [
    path('<int:pk>/', v.EstoqueDetail.as_view(), name='url_estoque_detail'), # noqa
    path('entrada/', include(entrada_patterns)),
    path('saida/', include(saida_patterns)),

]
