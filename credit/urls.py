from django.urls import path

from . import views

urlpatterns = [
    path('client/', views.ClientList.as_view(), name='client_list'),
    path('account/', views.AccountList.as_view(), name='account_list'),
    path('credit/', views.CreditList.as_view(), name='credit_list'),
    path('client/<int:pk>/detail/', views.ClientDetail.as_view(), name='client_detail'),
    path('account/<int:pk>/detail/', views.AccountDetail.as_view(), name='account_detail'),
    path('credit/<int:pk>/detail/', views.CreditDetail.as_view(), name='credit_detail'),
]