from django.urls import path

from . import views as v

app_name='produto'

urlpatterns = [
    path('', v.produto_list, name='url_produto_list'),
    path('<int:pk>/', v.produto_detail, name='url_produto_detail'),
]
