from django.db import models

import json
class Calculator:

    @staticmethod
    def taux_remise(prix_brut, prix_achat_net):
        return round((1 - prix_achat_net / prix_brut) * 100, 2)

    @staticmethod
    def prix_achat_net(taux_remise, prix_brut):
        print(taux_remise)
        return round(prix_brut * (1 - taux_remise / 100), 2)

    @staticmethod
    def prix_vente_net(prix_achat_net, coef):
        return round(prix_achat_net * coef, 2)
    @staticmethod
    def coef(prix_vente_net, prix_achat_net):
        return round(prix_vente_net / prix_achat_net, 2)

    @staticmethod
    def compute(id, prix_brut, taux_remise, prix_achat_net, prix_vente_net, coef):

        context = {}
        if id == "prix_brut" and not taux_remise == 0:
            context['taux_remise'] = taux_remise
            context['prix_achat_net'] = Calculator.prix_achat_net(float(taux_remise), float(prix_brut))
            context['prix_vente_net'] = Calculator.prix_vente_net(context['prix_achat_net'], float(coef))
            context['coef'] = coef


        elif id == "taux_remise":
            context['taux_remise'] = taux_remise
            context['prix_achat_net'] = Calculator.prix_achat_net(float(taux_remise), float(prix_brut))
            context['prix_vente_net'] = Calculator.prix_vente_net(context['prix_achat_net'], float(coef))
            context['coef'] = coef

        elif id == "prix_achat_net":
            context['taux_remise'] = Calculator.taux_remise(float(prix_brut), float(prix_achat_net))
            context['prix_achat_net'] = prix_achat_net
            context['prix_vente_net'] = Calculator.prix_vente_net(float(prix_achat_net), float(coef))
            context['coef'] = coef

        elif id == "prix_vente_net":
            context['taux_remise'] = taux_remise
            context['prix_achat_net'] = prix_achat_net
            context['prix_vente_net'] = prix_vente_net
            context['coef'] = Calculator.coef(float(prix_vente_net), float(prix_achat_net))

        elif id == "coef":
            context['taux_remise'] = taux_remise
            context['prix_achat_net'] = prix_achat_net
            context['prix_vente_net'] = Calculator.prix_vente_net(float(prix_achat_net), float(coef))
            context['coef'] = coef

        context_json = json.dumps(context)
        return context_json