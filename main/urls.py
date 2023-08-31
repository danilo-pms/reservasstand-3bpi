"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from reservas import views

urlpatterns = [
    path('cadastrar/', views.cadastro, name='cadastrar_reserva'), 
    path('listar/', views.listar, name='listar_reservas'), 
    path('detalhes/<int:id>/', views.detalhes_reserva, name='detalhes_reserva'),  
    path('excluir/<int:id>/', views.excluir_reserva, name='excluir_reserva'),  
    path('atualizar/<int:id>/', views.atualizar, name='atualizar_reserva'), 
]

