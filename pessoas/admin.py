from django.contrib import admin
from .models import Paciente, Cuidador

# Register your models here.
class PacienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'dt_nascimento']
    search_fields = ['nome']

admin.site.register(Paciente, PacienteAdmin)

class CuidadorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone']
    search_fields = ['nome']

admin.site.register(Cuidador, CuidadorAdmin)