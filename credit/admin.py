from django.contrib import admin

from .models import Client, Account, Credit


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'citizenship', 'birth_year', 'work_place']
    search_fields = ['name', ]


@admin.register(Account)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['number', 'account_type', 'client']
    search_fields = ['number', ]


@admin.register(Credit)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['sum', 'date', 'account']
    search_fields = ['date', ]
