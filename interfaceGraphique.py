import afficher;

# Classe Interface Graphique
class InterfaceGraphique:

    # Constructeur
    def __init__(self, enTete, file, dataFrame):
        self.afficher = afficher.Afficher(enTete, file, dataFrame);

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
        self.getAfficher().afficherEnTete();
        return value;