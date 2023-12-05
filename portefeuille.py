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