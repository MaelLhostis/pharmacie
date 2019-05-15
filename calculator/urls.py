from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test/<str:id>/<str:taux_remise>/<str:prix_brut>/<str:prix_achat_net>/<str:prix_vente_net>/<str:coef>/', views.calculator, name='test'),
]