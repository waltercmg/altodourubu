from django.conf.urls import url, patterns, include


urlpatterns = [
    url(r'^$', 'nucleo.views.home', name='home'),
    url(r'^contato/$', 'nucleo.views.contact', name='contact'),
    url(r'^afericao/$', 'nucleo.views.afericao', name='afericao'),
    url(r'^historico/$', 'nucleo.views.historico', name='historico'),
    #url(r'^admin/', teste_django.nucleo.views.home),
]
