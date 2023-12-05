"""Ficher contenant les differents types d'erreurs  soulever"""
class ErreurDate(RuntimeError):
    """Classe qui en capsule le message d'erreur Erreur date"""
    def erreurdate(self):
        """Fonction qui souleve le message d'erreur Erreur date """
        raise ErreurDate