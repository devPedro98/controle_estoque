from django.urls import path

from estoque import views as v

app_name = 'estoque'

urlpatterns = [
    path('', v.EstoqueEntradaList.as_view(), name='url_estoque_entrada_list'),
    path('<int:pk>/', v.estoque_entrada_detail, name='url_estoque_entrada_detail'), # noqa
    path('add/', v.estoque_entrada_add, name='url_estoque_entrada_add'),
    path('saida/', v.EstoqueSaidaList.as_view(), name='url_estoque_saida_list'), # noqa
    path('saida/<int:pk>/', v.estoque_saida_detail, name='url_estoque_saida_detail'), # noqa
    path('saida/add/', v.estoque_saida_add, name='url_estoque_saida_add'),
]
