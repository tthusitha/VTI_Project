import os, io

# Classe sauvegarde en fichier
class Log :

    # Constructeur
    def __init__(self, fichier, dataFrame):
        self.fichier = fichier;
        self.dataFrame = dataFrame;

    # Sauvegarder en fichier
    def sauvegarder(self, filepath):

        try:
            os.remove(filepath);
        except OSError:
            pass;
        try:
            fichierLog = io.open(filepath, mode="a", encoding="utf-8")
            liste = [];

            # Sauvegarder les informations concernant le fichier
            liste.append("Taille du fichier: " + self.fichier.getTailleFichier().__str__());
            liste.append("Date de dernière modification: " + self.fichier.getDateDerniereModification().__str__());
            liste.append("Encodage: " + self.fichier.getTypeEncodage().__str__());

            # Sauvegarder les informations concernant les données
            liste.append("Nombre d'observations : " + self.dataFrame.getNbObservations().__str__());
            liste.append("Nombre de variables : " + self.dataFrame.getNbVariables().__str__());
            liste.append("Nombre des variables qualitatives: " + self.dataFrame.getNbVariablesQualitatives().__str__());
            if self.dataFrame.getNbVariablesQualitatives() != 0:
                liste.append("Noms des variables qualitatives :\n" + self.dataFrame.getListeVariablesQualitatives().__str__());
            else:
                liste.append("Pas de variables qualitatives");
            liste.append("Nombre des variables qantitatives: " + self.dataFrame.getNbVariablesQuantitatives().__str__());
            if self.dataFrame.getNbVariablesQuantitatives() != 0:
                liste.append("Noms des variables quantitatives :\n" + self.dataFrame.getListeVariablesQuantitatives().__str__());
            else:
                liste.append("Pas de variables quantitatives");

            # Sauvegarder les informations concernant les variables qualitatives variables
            liste.append("Les modalités des variables qualitatives sont: \n" + self.dataFrame.getModalites().__str__());
            liste.append("Les effectifs des variables qualitatives sont: \n" + self.dataFrame.getNbEffectifs().__str__());
            liste.append("Les fréquences des variables qualitatives sont: \n" + self.dataFrame.getNbFrequences().__str__());

            # Sauvegarder les informations concernant les variables quantitatives variables
            liste.append("Les valeurs minimales des variables quantitatives sont: \n" + self.dataFrame.getValeurMin().__str__());
            liste.append("Les valeurs maximales des variables quantitatives sont: \n" + self.dataFrame.getValeurMax().__str__());
            liste.append("Les valeurs médianes des variables quantitatives sont: \n" + self.dataFrame.getMediane().__str__());
            liste.append("Les moyennes des variables quantitatives sont: \n" + self.dataFrame.getMoyenne().__str__());
            liste.append("Les écarts-types des variables quantitatives sont: \n" + self.dataFrame.getEcartType().__str__());

            for i in range(0, len(liste)):
                fichierLog.write(liste[i]);
        except FileNotFoundError:
            print("Chemin du fichier de log invalide");
            exit();