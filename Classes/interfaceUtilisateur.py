from Classes import afficher
import os

# Classe Interface Graphique
class InterfaceUtilisateur:

    # Constructeur
    def __init__(self, enTete, fichier, dataFrame):
        self.afficher = afficher.Afficher(enTete, fichier, dataFrame);

    # Attendre que l'utilisateur appuie sur une touche
    def debut(self):
        try:
            input("Appuyez sur une touche pour continuer ...");
            self.getAfficher().afficherEnTete();
        except SyntaxError:
            pass;

    # Retourner la classe Afficher
    def getAfficher(self):
        return self.afficher;

    # Retourner la valeur de la réponse
    def reponse(self, texte):
        value = input(texte);
        self.nettoyerTerminal();
        self.getAfficher().afficherEnTete();
        return value;

    # Nettoyer le terminal
    def nettoyerTerminal(self):
        # windows
        if os.name == 'nt':
            _ = os.system('cls');
        # mac & linux
        else:
            _ = os.system('clear');