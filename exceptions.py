"""Ficher contenant les differents types d'erreurs  soulever"""
class ErreurDate(RuntimeError):
    """Classe qui en capsule le message d'erreur Erreur date"""
    def erreurdate(self):
        """Fonction qui souleve le message d'erreur Erreur date """
        raise ErreurDate
class ErreurQuantite(RuntimeError):
    """Classe qui en capsule le message d'erreur ErreurQuantité"""
    def erreurquantite(self):
        """Fonction qui souleve le message d'erreur ErreurQuantité """
        raise ErreurQuantite
class LiquiditeInsuffisante(RuntimeError):
    """Classe qui en capsule le message d'erreur LiquiditéInsuffisante"""
    def liquiditeinsuffisante(self):
        """Fonction qui souleve le message d'erreur LiquiditéInsuffisante """
        raise LiquiditeInsuffisante
    