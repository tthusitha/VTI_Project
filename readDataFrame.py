from pathlib import Path
import pandas

#Lecture de DataFrame
class ReadDataFrame :

    #Constructeur
    def __init__(self, file):
        pathFichier = Path(file);
        self.dataFrame = pandas.read_csv(pathFichier);

    #Récupérer le nombre de variable du DataFrame
    def getNbVariables(self):
        return self.dataFrame.shape[1];

    #Récupérer le nombre d'observation du DataFrame
    def getNbObservations(self):
        return self.dataFrame.shape[0];

    #Récupérer la liste des variables qualitatives
    def getListeVariablesQualitatives(self):
        liste = [];
        for i in range(0, len(self.dataFrame.dtypes)):
            if self.dataFrame.dtypes[i] == "object":
                liste.append(self.dataFrame.columns.values[i]);
        return liste;

    #Récupérer le nombre de variable qualitative
    def getNbVariablesQualitatives(self):
        return len(self.getListeVariablesQualitatives());

    #Récupérer la modalité des variables qualitatives
    def getModalites(self):
        val = "";
        for i in range(0, self.getNbVariablesQualitatives()):
            colonne = self.getListeVariablesQualitatives()[i] + " -> ";
            val += colonne + self.dataFrame[self.getListeVariablesQualitatives()[i]].nunique().__str__() + "\n";
        return val;

    #Récupérer le nombre d'effectif des variables qualitatives
    def getNbEffectifs(self):
        val = "";
        for i in range(0, self.getNbVariablesQualitatives()):
            val += self.dataFrame[self.getListeVariablesQualitatives()[i]].value_counts().__str__() + "\n";
        return val;

    #Récupérer la fréquence d'apparition d'une variable qualitative
    def getNbFrequences(self):
        val = "";
        for i in range(0, self.getNbVariablesQualitatives()):
            effectif = self.dataFrame[self.getListeVariablesQualitatives()[i]].value_counts()
            effectifTotal = self.dataFrame[self.getListeVariablesQualitatives()[i]].count()
            val += (effectif/effectifTotal).__str__() + "\n";
        return val;

    #Récupérer la liste des variables quantitatives
    def getListeVariablesQuantitatives(self):
        liste = [];
        for i in range(0, len(self.dataFrame.dtypes)):
            if self.dataFrame.dtypes[i] == "float64" or self.dataFrame.dtypes[i] == "int64":
                liste.append(self.dataFrame.columns.values[i]);
        return liste;

    #Récupérer le nombre des variables quantitatives
    def getNbVariablesQuantitatives(self):
        return len(self.getListeVariablesQuantitatives());

    #Récupérer la valeur minimale des variables quantitatives
    def getValeurMin(self):
        valeurMin = "";
        for i in range(0, self.getNbVariablesQuantitatives()):
            colonneMin = self.getListeVariablesQuantitatives()[i] + " -> ";
            valeurMin += colonneMin + self.dataFrame[self.getListeVariablesQuantitatives()[i]].min().__str__() + "\n";
        return valeurMin;

    #Récupérer la valeur maximale des variables quantitatives
    def getValeurMax(self):
        valeurMax = "";
        for i in range(0, self.getNbVariablesQuantitatives()):
            colonneMax = self.getListeVariablesQuantitatives()[i] + " -> ";
            valeurMax += colonneMax + self.dataFrame[self.getListeVariablesQuantitatives()[i]].max().__str__() + "\n";
        return valeurMax;

    #Récupérer la médiane des variables quantitatives
    def getMediane(self):
        valeurMediane = "";
        for i in range(0, self.getNbVariablesQuantitatives()):
            colonneMediane = self.getListeVariablesQuantitatives()[i] + " -> ";
            valeurMediane += colonneMediane + self.dataFrame[self.getListeVariablesQuantitatives()[i]].median().__str__() + "\n";
        return valeurMediane;

    #Récupérer la moyenne des variables quantitatives
    def getMoyenne(self):
        valeurMoyenne = "";
        for i in range(0, self.getNbVariablesQuantitatives()):
            colonneMoyenne = self.getListeVariablesQuantitatives()[i] + " -> ";
            valeurMoyenne += colonneMoyenne + self.dataFrame[self.getListeVariablesQuantitatives()[i]].mean().__str__() + "\n";
        return valeurMoyenne;

    #Récupérer l'écartType des variables quantitatives
    def getEcartType(self):
        valeurEcartType = "";
        for i in range(0, self.getNbVariablesQuantitatives()):
            colonneEcartType = self.getListeVariablesQuantitatives()[i] + " -> ";
            valeurEcartType += colonneEcartType + self.dataFrame[self.getListeVariablesQuantitatives()[i]].std().__str__() + "\n";
        return valeurEcartType;