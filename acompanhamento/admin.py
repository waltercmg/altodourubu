from django.contrib import admin
from .models import Afericao, Dado

# Register your models here.
class AfericaoAdmin(admin.ModelAdmin):
    list_display = ['id', 'paciente', 'cuidador', 'dt_criacao']

admin.site.register(Afericao, AfericaoAdmin)

class DadoAdmin(admin.ModelAdmin):
    list_display = ['afericao', 'sinal', 'valor']
    search_fields = ['afericao']

admin.site.register(Dado, DadoAdmin)