from django.shortcuts import render
from .models import musico, tipo_de_musica, instrumentos
def index(request):
    return render(request, 'bases1/index.html', {
        'musicos': musico.objects.all(),
        'tipos': tipo_de_musica.objects.all(),
        'instrumentos': instrumentos.objects.all(),
    })

