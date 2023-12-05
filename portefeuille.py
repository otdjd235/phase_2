"import"
from datetime import date as dt
from bourse import Bourse
from exceptions import ErreurDate, ErreurQuantite, LiquiditeInsuffisante


bourse_fictive = Bourse()
class Portefeuille:
    "portefeuille"
    def __init__(self, bourse):
        self.bourse = bourse
        self.transactions = []
    def deposer(self, montant, date=dt.today()):
        "depot"
        if date > date.today():
            raise ErreurDate("La date de dépôt ne peut pas être dans le futur.")
        self.transactions.append({'type': 'depot', 'montant': montant, 'date': date})
    def solde(self, date=dt.today()):
        "solde"
        if date > date.today():
            raise ErreurDate

        solde = 0
        for transaction in self.transactions:
            if transaction['date'] <= date:
                if transaction['type'] in ('depot', 'vente'):
                    solde += transaction['montant']
                elif transaction['type'] == 'achat':
                    solde -= transaction['montant']

        return solde
    def acheter(self, symbole, quantite, date=dt.today()):
        "achat"
        if date > date.today():
            raise ErreurDate

        prix_achat = self.bourse.prix(symbole, date) * quantite
        if self.solde(date) < prix_achat:
            raise LiquiditeInsuffisante

        self.transactions.append({'type': 'achat', 'symbole': symbole,
                                  'quantite': quantite, 'date': date})

    def vendre(self, symbole, quantite, date=dt.today()):
        "vente"
        if date > date.today():
            raise ErreurDate
        if self.titres(date).get(symbole, 0) < quantite:
            raise ErreurQuantite
        prix_vente = self.bourse.prix(symbole, date) * quantite
        self.transactions.append({'type': 'vente', 'symbole': symbole,
        'quantite': quantite, 'montant': prix_vente, 'date': date})
    def valeur_totale(self, date=dt.today()):
        "valeur totale"
        if date > date.today():
            raise ErreurDate

        valeur_liquidites = self.solde(date)
        valeur_titres = sum([self.bourse.prix(symbole, date) * quantite for symbole,
                              quantite in self.titres(date).items()])
        return valeur_liquidites + valeur_titres
    def valeur_des_titres(self, symboles, date=dt.today()):
        "valeur des titres"
        if date > date.today():
            raise ErreurDate

        valeur_titres = sum([self.bourse.prix(symbole, date) * self.titres(date).get(symbole, 0)
                              for symbole in symboles])
        return valeur_titres
    def titres(self, date=dt.today()):
        "titres"
        if date > date.today():
            raise ErreurDate

        titres = {}
        for transaction in self.transactions:
            if transaction['date'] <= date:
                if transaction['type'] == 'achat':
                    titres[transaction['symbole']] = titres.get(transaction['symbole'],
                                                                 0) + transaction['quantite']
                elif transaction['type'] == 'vente':
                    titres[transaction['symbole']] = titres.get(transaction['symbole'],
                                                                 0) - transaction['quantite']
        return {symbole: quantite for symbole, quantite in titres.items() if quantite > 0}
    def valeur_projetee(self, date_proj, rendement):
        "valeur projetee"
        if date_proj <= dt.today():
            raise ErreurDate

        valeur_totale = self.valeur_totale()
        years = date_proj.year - dt.today().year
        future_value = valeur_totale * (1 + rendement / 100) ** years
        return future_value
portefeuille = Portefeuille(bourse_fictive)

portefeuille.deposer(1000)

portefeuille.acheter("goog", 8)

portefeuille.vendre("goog", 10)

titres_actuels = portefeuille.titres()
print("Titres actuels :", titres_actuels)

solde_actuel = portefeuille.solde()
print("Solde actuel :", solde_actuel)

valeur_totale_actuelle = portefeuille.valeur_totale()
print("Valeur totale actuelle :", valeur_totale_actuelle)

symboles_titres = ["goog", "goog"]
valeur_titres_specifiques = portefeuille.valeur_des_titres(symboles_titres)
print(f"Valeur des titres spécifiques ({symboles_titres}) actuelle :", valeur_titres_specifiques)

date_projetee = dt.today().replace(year=dt.today().year + 2)

valeur_projetee = portefeuille.valeur_projetee(date_projetee, 8)
print(f"Valeur projetée dans deux ans avec un rendement de {8}%: {valeur_projetee}")

