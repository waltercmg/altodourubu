from django import forms
from pessoas.models import Paciente, Cuidador
from ssvv.models import Sinal
from django.forms.widgets import TextInput

TAG_SINAL = "sinal_"

class AcompanhamentoForm(forms.Form):
    paciente = forms.ModelChoiceField(queryset=Paciente.objects.all())
    cuidador = forms.ModelChoiceField(queryset=Cuidador.objects.all())
    
    for s in Sinal.objects.all().order_by('sigla'):
        exec(TAG_SINAL + "%s = forms.FloatField(label=s)" % str(s.id))
        #exec(TAG_SINAL + "%s = forms.FloatField(label=s, max_value=10, min_value=3 )" % str(s.id))

class HistoricoForm(forms.Form):
    paciente = forms.ModelChoiceField(queryset=Paciente.objects.all(),widget=forms.Select(attrs={"onChange":'submit()'}))
        
class NumberInput(TextInput):
    input_type = 'number'