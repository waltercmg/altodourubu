from django.contrib import admin
from .models import Sinal

# Register your models here.
class SinalAdmin(admin.ModelAdmin):
    list_display = ['sigla', 'nome']
    search_fields = ['nome', 'sigla']

admin.site.register(Sinal, SinalAdmin)