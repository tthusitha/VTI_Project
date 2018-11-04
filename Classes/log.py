import os, io

# Classe sauvegarde en fichier
class Log :

    # Constructeur
    def __init__(self, filepath, fichier, dataFrame):
        try:
            os.remove(filepath);
        except OSError:
            pass;
        self.fichierLog = io.open(filepath, mode="a", encoding="utf-8");
        self.fichier = fichier;
        self.dataFrame = dataFrame;

    # Ecrire en fichier
    def ecrire(self, texte):
        self.fichierLog.write(texte + "\n\n");

    # Sauvegarder en fichier
    def sauvegarder(self):
        liste = [];

        # Sauvegarder les informations concernant le fichier
        liste.append("Taille du fichier: " + self.fichier.getTailleFichier().__str__());
        liste.append("Date de dernière modification: " + self.fichier.getDateDerniereModification().__str__());
        liste.append("Encodage: " + self.fichier.getTypeEncodage().__str__());

        # Sauvegarder les informations concernant les données
        liste.append("Nombre d'observations : " + self.dataFrame.getNbObservations().__str__());
        liste.append("Nombre de variables : " + self.dataFrame.getNbVariables().__str__());
        liste.append("Nombre des variables qualitatives: " + self.dataFrame.getNbVariablesQualitatives().__str__());
        liste.append("Noms des variables qualitatives: " + self.dataFrame.getListeVariablesQualitatives().__str__());
        liste.append("Nombre des variables qantitatives: " + self.dataFrame.getNbVariablesQuantitatives().__str__());
        liste.append("Noms des variables qantitatives: " + self.dataFrame.getListeVariablesQuantitatives().__str__());

        # Sauvegarder les informations concernant les variables qualitatives variables
        liste.append("Les modalités des variables qualitatives sont: " + self.dataFrame.getModalites().__str__());
        liste.append("Les effectifs des variables qualitatives sont: " + self.dataFrame.getNbEffectifs().__str__());
        liste.append("Les fréquences des variables qualitatives sont: " + self.dataFrame.getNbFrequences().__str__());

        # Sauvegarder les informations concernant les variables quantitatives variables
        liste.append("Les valeurs minimales des variables quantitatives sont: " + self.dataFrame.getValeurMin().__str__());
        liste.append("Les valeurs maximales des variables quantitatives sont: " + self.dataFrame.getValeurMax().__str__());
        liste.append("Les valeurs médianes des variables quantitatives sont: " + self.dataFrame.getMediane().__str__());
        liste.append("Les moyennes des variables quantitatives sont: " + self.dataFrame.getMoyenne().__str__());
        liste.append("Les écarts-types des variables quantitatives sont: " + self.dataFrame.getEcartType().__str__());

        for i in range(0, len(liste)):
            self.ecrire(liste[i]);