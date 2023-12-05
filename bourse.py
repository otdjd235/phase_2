"import des modules utiles"
from datetime import date as dt
from phase1 import produire_historique
from exceptions import ErreurDate


class Bourse:
    """Classe bourse qui encapsule le pogramme d'extraction de prix"""
    def prix(self, symbole, date):
        """Fonction retournant la valeur du prix a la fermeture, pour
        la date voulue"""
        self.symbole = symbole
        self.date = date
        a = produire_historique(self.symbole, self.date, self.date)
        if self.date != date.today():
            if self.date > date.today():
                raise ErreurDate
            if a != []:
                price = a
            if a == [] :
                if self.date.day == 1:
                    if self.date.month == 1:
                        previous_day = self.date.replace(day = 31, month = 12,
                                                          year=self.date.year-1)
                    if self.date.month != 1:
                        if self.date.month -1 == 2:
                            if self.date.year % 4 == 0 and (self.date.day % 100 != 0
                                                            or self.date.year % 400 ==0):
                                previous_day= self.date.replace(day = 29, month = 2)
                            if not(self.date.year % 4 == 0 and (self.date.day % 100 != 0
                                                                or self.date.year % 400 ==0)):
                                previous_day = self.date.replace(day=28, month = 2)
                        if self.date.month -1 != 2:
                            if self.date.month in [1, 3, 5, 7, 10, 12]:
                                previous_day = self.date.replace(day=30, month= self.date.month -1)
                            else:
                                previous_day = self.date.replace(day=31, month= self.date.month -1)
                else:
                    previous_day = self.date.replace(day = self.date.day - 1)
                    if produire_historique(self.symbole,
                                           previous_day, previous_day) == []:
                        previous_day = self.date.replace(day = previous_day.day - 1)
                price = produire_historique(self.symbole,
                                            previous_day, previous_day)
        elif self.date == date.today():
            if a == []:
                previous_day = self.date.replace(day= self.date.day - 1)
                if produire_historique(self.symbole,
                                       previous_day, previous_day) == []:
                    previous_day = self.date.replace(day = previous_day.day - 1)
                price = produire_historique(self.symbole,
                                            previous_day, previous_day)
            elif a != []:
                price = a
        return float(price[0][1])
x = Bourse()
resultat = x.prix('goog', dt(2023,12,3))
print(resultat)
