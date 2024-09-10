from django.contrib import admin
from .models import Tabela

class TabelaAdmin(admin.ModelAdmin):
    list_display = ('email', 'estilo','nome')

admin.site.register(Tabela, TabelaAdmin)