from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('meus-produtos/', views.MyProducts.as_view(), name='my_products'),
    path('produto/novo/', views.ProductCreate.as_view(), name='new_product' ),
    path('produto/editar/<int:pk>', views.ProductUpdate.as_view(), name='update_product' ),
    path('produto/<slug:slug>', views.ProductDetail.as_view(), name='product_detail'),
    path('produto/<slug:slug>/perguntar/', views.product_question, name='product_question'),
    path('produto/<slug:slug>/responder/<int:pk>', views.product_answer, name='question_answer'),
    path('buscar/', views.search, name='search')
]