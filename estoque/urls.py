from django.urls import path

from estoque import views as v

app_name = 'estoque'

urlpatterns = [
    path('', v.estoque_entrada_list, name='url_estoque_entrada_list'),
    path('<int:pk>/', v.estoque_entrada_detail, name='url_estoque_entrada_detail'),
    path('add/', v.estoque_entrada_add, name='url_estoque_entrada_add'),
]
