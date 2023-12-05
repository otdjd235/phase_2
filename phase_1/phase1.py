"""" Code permettant d'extraire des valeurs historiques pour un ou plusieurs symboles boursiers.
Les modules suivants sont esentiels pour notre programme"""
import datetime
import argparse
import json
import requests

def analyser_commande():
    """Cette fonction permet d'analyser la commande de l'usager,
    de definir les attributs possibles qu'il a le droit d'utiliser."""
    parser = argparse.ArgumentParser(description =
    'Extraction de valeurs historiques pour un,ou plusieurs symboles boursiers.')
    parser.add_argument('symboles', nargs = '+', metavar = 'symbole',
    help = '''Nom d'un symbole boursier''')
    parser.add_argument('-d', dest = 'debut', metavar= 'DATE', default = None,
    type= datetime.date.fromisoformat,
    help = 'Date recherchée la plus ancienne (format: AAAA-MM-JJ)')
    parser.add_argument('-f', dest = 'fin', metavar= 'DATE', default = None,
    type=datetime.date.fromisoformat, help = 'Date recherchée la plus récente (format: AAAA-MM-JJ)')
    parser.add_argument('-v', dest = 'valeur', default = 'fermeture',
    choices = {'fermeture', 'ouverture', 'min', 'max', 'volume'},
    help = 'La valeur désirée (par défaut: fermeture)')
    args = parser.parse_args()
    if args.fin is None:
        args.fin = datetime.date.today()
    if args.debut is None:
        args.debut = args.fin
    return args
test = analyser_commande()

def produire_historique(symbol, debut = test.debut, fin = test.fin, valeur = test.valeur):
    """"Cette fonction permet d'afficher le resume de la commande de l'usager sur une premiere ligne
    puis retourner unne liste de tuples (date, valeur) correspondant a la commande sur le serveur"""
    url = f'https://pax.ulaval.ca/action/{symbol}/historique/'
    params = {'début': debut,'fin': fin}
    reponse = requests.get(url=url, params = params, timeout=10)
    #print(f'titre={symbol}: valeur={valeur}, début={repr(debut)}, fin={repr(fin)}')
    reponse = json.loads(reponse.text)
    dates = list(reponse['historique'])
    val_names = [reponse['historique'][k] for k in reponse['historique']]
    a = ([datetime.date.fromisoformat(i) for i in dates])
    b = ([j[valeur] for j in val_names])
    return sorted(list(set(zip(a, b))))

for symb in test.symboles:
    print(produire_historique(symbol = symb))