from django.shortcuts import render
from django.views import generic

from .models import Client, Account, Credit


class ClientList(generic.ListView):
    model = Client
    template_name = 'credit/client_list.html'


class AccountList(generic.ListView):
    model = Account
    template_name = 'credit/account_list.html'


class CreditList(generic.ListView):
    model = Credit
    template_name = 'credit/credit_list.html'


class ClientDetail(generic.DetailView):
    model = Client


class AccountDetail(generic.DetailView):
    model = Account


class CreditDetail(generic.DetailView):
    model = Credit
