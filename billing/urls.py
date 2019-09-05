from django.urls import path, include
from . import views
urlpatterns = [
    path('pagamento/<slug:slug>', views.payment, name='payment' ),
    path('pagamento/confirm/<int:order_id>', views.item_purchased, name='item_purchased' ),
    path('produtos/minhas-vendas/', views.UserSales.as_view(), name='users_sales'),
    path('produtos/venda/<int:pk>', views.salesUpdate, name='sales_update'),
    path('produtos/minhas-compras', views.UsersShopping.as_view(), name='users_shopping')
]