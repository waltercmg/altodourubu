from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from acompanhamento.forms import AcompanhamentoForm, HistoricoForm, TAG_SINAL
from acompanhamento.models import Afericao, Dado
from pessoas.models import Paciente
from ssvv.models import Sinal

# Create your views here.
def home(request):
    return render(request, 'home.html')
    
def contact(request):
    return render(request, 'contact.html')
    
def afericao(request):
    context = {}
    sinais = {}
    if request.method == "POST":
        form = AcompanhamentoForm(request.POST)
        if form.is_valid():
            p = form.cleaned_data['paciente']
            c = form.cleaned_data['cuidador']
            afer = Afericao(paciente = p, cuidador = c)
            afer.save()
            for campo in form.cleaned_data:
                if TAG_SINAL in campo:
                    s = Sinal.objects.get(pk=campo.replace(TAG_SINAL,''))
                    v = form.cleaned_data[campo]
                    sinais[str(s.sigla)]=v
                    dado = Dado(afericao = afer, sinal = s, valor=v)
                    dado.save()
            context['is_valid'] = True
            return enviarMsg(p, c, sinais, afer.dt_criacao)
    else:
        form = AcompanhamentoForm()
    context['form'] = form
    return render(request, 'afericao.html', context)
    
def enviarMsg(paciente, cuidador, sinais, data):
    texto = "Segue SSV de *" + str(paciente) + "*:\n\n" 
    pa = {}
    for sinal, valor in sinais.items():
        if sinal != "PAMAX" and sinal != "PAMIN":
            texto += str(sinal) + ": *" + str(valor) + "*\n"
        else:
            pa[sinal] = valor
    if len(pa) == 2:
        texto += "PA: *" + str(pa["PAMAX"]) + "* x *" + str(pa["PAMIN"]) + "*\n"
    texto += "\nData: *" + str(data.strftime('%d/%m/%Y %H:%M:%S')) + "*\n"
    texto += "Cuidador(a): *" + str(cuidador) + "*\n\n"
    texto += "https://teste-django-waltercmg.c9users.io/historico?paciente="+str(paciente.id)
    return HttpResponseRedirect('https://api.whatsapp.com/send?phone=5581996780000&text=' + texto)


def historico_old(request):
    context = {}
    if request.method == "GET":
        p_id = request.GET.get('paciente', str(Paciente.objects.filter(nome__startswith="Walter")[0].id))
        p = Paciente.objects.get(pk=p_id)
        afericoes = Afericao.objects.filter(paciente=p).order_by('-dt_criacao')[:6]
        datas, valores, sinais, sinais_pa = {}, {}, {}, {}
        valores["PAMAX"], valores["PAMIN"] = [],[]
        for a in reversed(afericoes):
            for d in a.dado_set.all():
                sinal = d.sinal.sigla
                sinal_nm = d.sinal.nome
                if sinal not in datas:
                    datas[sinal] = []
                if sinal not in valores:
                    valores[sinal] = []
                datas[sinal].append( d.afericao.dt_criacao.strftime('%d/%m (%H:%M)'))
                valores[sinal].append(d.valor)
                if sinal != "PAMAX" and sinal != "PAMIN":
                    sinais.update({sinal_nm:{'datas':datas[sinal],'valores':valores[sinal]}})
                else:
                    sinais_pa.update({"PA":{'datas':datas[sinal],'valores_pamax':valores["PAMAX"],'valores_pamin':valores["PAMIN"] }})
        #form = AcompanhamentoForm(request.POST)            
        if HistoricoForm(request.GET):
            form = HistoricoForm(request.GET)
        else:
            form = HistoricoForm()
        context['form'] = form            
        context['sinais'] = sinais
        context['sinais_pa'] = sinais_pa
        context['paciente'] = p.nome
        
    return render(request, 'historico.html', context)
    
def historico(request):
    context = {}
    if request.method == "GET":
        p_id = request.GET.get('paciente', str(Paciente.objects.filter(nome__startswith="Walter")[0].id))
        p = Paciente.objects.get(pk=p_id)
        afericoes = Afericao.objects.filter(paciente=p).order_by('-dt_criacao')[:6]
        datas, valores, sinais, sinais_pa = {}, {}, {}, {}
        valores["PAMAX"], valores["PAMIN"] = [],[]
        for a in reversed(afericoes):
            for d in a.dado_set.all():
                sinal = d.sinal.sigla
                sinal_nm = d.sinal.nome
                if sinal not in datas:
                    datas[sinal] = []
                if sinal not in valores:
                    valores[sinal] = []
                datas[sinal].append( d.afericao.dt_criacao.strftime('%d/%m (%H:%M)'))
                valores[sinal].append(d.valor)
                if sinal != "PAMAX" and sinal != "PAMIN":
                    sinais.update({sinal_nm:{'datas':datas[sinal],'valores':valores[sinal]}})
                else:
                    sinais_pa.update({"PA":{'datas':datas[sinal],'valores_pamax':valores["PAMAX"],'valores_pamin':valores["PAMIN"] }})
        form = HistoricoForm(initial={'paciente': p.id})
        context['form'] = form            
        context['sinais'] = sinais
        context['sinais_pa'] = sinais_pa
        context['paciente'] = p.nome
        
        
    return render(request, 'historico.html', context)