from django.contrib import admin
from .models import Servico,Cargo,Funcionario,Recurso


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo','ativo','modificado')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico','descricao','icone','ativo','modificado')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome','cargo','bio','ativo','modificado')

@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('recurso','descricao','modificado')
