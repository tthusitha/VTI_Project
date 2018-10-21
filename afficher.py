#Classe pour les affichages
class Afficher:

    # Constructeur
    def __init__(self, enTete, file, dataFrame):
        self.enTete = enTete;
        self.file = file;
        self.dataFrame = dataFrame;

    # Afficher et retour à la ligne
    def afficher(self, value):
        print(value + "\n");

    # Afficher en-tête
    def afficherEnTete(self):
        self.afficher(self.enTete);

    # Afficher la taille du fichier
    def afficherTailleFichier(self):
        self.afficher("Taille du fichier : " + self.file.getTailleFichier() + " Ko");

    # Afficher la date de la dernière modification
    def afficherDateDerniereModification(self):
        self.afficher("Date de derniere modification : " + self.file.getDateDerniereModification());

    # Afficher le type d'encodage
    def afficherTypeEncodage(self):
        self.afficher("Encodage : " + self.file.getTypeEncodage());

    # Afficher la taille du fichier, la date de la dernière modification, le type d'encodage
    def afficherInfosFichier(self):
        self.afficher(self.afficherTailleFichier() + ", " + self.afficherDateDerniereModification() + ", " + self.afficherTypeEncodage());

    # Afficher le nombre de variables
    def afficherNbVariables(self):
        self.afficher("Nombre de variables : " + self.dataFrame.getNbVariables().__str__());

    # Afficher le nombre d'observations
    def afficherNbObservations(self):
        self.afficher("Nombre d'observations : " + self.dataFrame.getNbObservations().__str__());

    # Afficher le nombre de variables qualitatives
    def afficherNbVariablesQualitatives(self):
        self.afficher("Nombres de variables qualitatives : " + self.dataFrame.getNbVariablesQualitatives().__str__());

    # Afficher la liste des variables qualitatives
    def afficherListeVariablesQualitatives(self):
        if self.dataFrame.getNbVariablesQualitatives() != 0:
            self.afficher("Nom des variables qualitatives :" + self.dataFrame.getListeVariablesQualitatives().__str__());
        else:
            self.afficher("Pas de variables qualitatives");

    # Afficher la liste des modalités des variables qualitatives
    def afficherModalites(self):
        self.afficher("Les modalités des variables qualitatives : " + self.dataFrame.getModalites().__str__());

    # Afficher le nombre d'effectifs des variables qualitatives
    def afficherNbEffectifs(self):
        self.afficher("Le nombre d'effectifs des variables qualitatives : " + self.dataFrame.getNbEffectifs().__str__());

    # Afficher les fréquences des variables qualitatives
    def afficherNbFrequences(self):
        self.afficher("Les fréquences des variables qualitatives : " + self.dataFrame.getNbFrequences().__str__());

    # Afficher le nombre de variables quantitatives
    def afficherNbVariablesQuantitatives(self):
        self.afficher("Nombres de variables quantitatives : " + self.dataFrame.getNbVariablesQuantitatives().__str__());

    # Afficher la liste de variables quantitatives
    def afficherListeVariablesQuantitatives(self):
        if self.dataFrame.getNbVariablesQuantitatives() != 0:
            self.afficher("Nom des variables quantitatives :" + self.dataFrame.getListeVariablesQuantitatives().__str__());
        else:
            self.afficher("Pas de variables quantitatives");

    # Afficher les valeurs minimales des variables quantitatives
    def afficherValeurMin(self):
        self.afficher("Les valeurs minimales des variables quantitatives sont : " + self.dataFrame.getValeurMin().__str__());

    # Afficher les valeurs maximales des variables quantitatives
    def afficherValeurMax(self):
        self.afficher("Les valeurs maximales des variables quantitatives sont : " + self.dataFrame.getValeurMax().__str__());

    # Afficher les médianes des variables quantitatives
    def getMediane(self):
        self.afficher("Les valeurs medianes des variables quantitatives sont : " + self.dataFrame.getMediane().__str__());

    # Afficher les moyennes des variables quantitatives
    def afficherMoyenne(self):
        self.afficher("Les moyennes des variables quantitatives sont : " + self.dataFrame.getMoyenne().__str__());

    # Afficher les écart-types des variables quantitatives
    def getEcartType(self):
        self.afficher("Les ecarts types des variables quantitatives sont : " + self.dataFrame.getEcartType().__str__());

    # Afficher le menu principal
    def afficherMenuPrincipal(self):
        self.afficher("Que voulez-vous faire ?");
        self.afficher("\u0009" + "f" + " - Afficher les informations sur le fichier");
        self.afficher("\u0009" + "d" + " - Afficher les informations sur les donnees");
        self.afficher("\u0009" + "q" + " - Quitter");

    # Afficher le menu suivant
    def afficherMenuSuivant(self):
        self.afficher("Quelle informations voulez-vous afficher ?");

    # Afficher le menu concernant les informations du fichier
    def afficherMenuFichier(self):
        self.afficher("\u0009" + "t" + " - Afficher la taille du fichier");
        self.afficher("\u0009" + "e" + " - Afficher l'encodage du fichier");
        self.afficher("\u0009" + "d" + " - Afficher la date de derniere modification du fichier");
        self.afficher("\u0009" + "a" + " - Afficher l'ensemble des informations");
        self.afficher("\u0009" + "r" + " - Retour au menu principal");

    # Afficher le menu concernant les informations des données
    def afficherMenuDonnees(self):
        self.afficher("\u0009" + "v" + " - Afficher les informations sur les variables quantitatives");
        self.afficher("\u0009" + "l" + " - Afficher les informations sur les variables qualitatives");
        self.afficher("\u0009" + "r" + " - Retour au menu principal");

    # Afficher commande invalide
    def afficherCommandeInvalide(self):
        self.afficher("Commande invalide");