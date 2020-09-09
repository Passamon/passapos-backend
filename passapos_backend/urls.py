from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.product), 
    path('product', views.product), 

    path('user/', views.user),
    path('user', views.user),

    path('transaction/', views.transaction),
    path('transaction', views.transaction)
]
