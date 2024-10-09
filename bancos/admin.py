from django.contrib import admin
from .models import Banco, ContaBancaria

@admin.register(Banco)
class BancoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'status')
    search_fields = ('nome',)
    list_filter = ('status',)

@admin.register(ContaBancaria)
class ContaBancariaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'saldo_atual', 'status')
    search_fields = ('nome',)
    list_filter = ('status',)
# Register your models here.
