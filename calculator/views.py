from django.http import HttpResponse
from django.template import loader

from .models import Calculator

def index(request):
    template = loader.get_template('calculator/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def calculator(request, id, prix_brut,taux_remise,  prix_achat_net, prix_vente_net, coef):
    return HttpResponse(Calculator.compute(id, taux_remise, prix_brut, prix_achat_net, prix_vente_net, coef))