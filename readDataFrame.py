from pathlib import Path
import pandas

class ReadDataFrame :

    def __init__(self, file):
        pathFichier = Path(file);
        self.dataFrame = pandas.read_csv(pathFichier);

    def getNbVariables(self):
        return self.dataFrame.shape[1];

    def getNbObservations(self):
        return self.dataFrame.shape[0];

    def getListeVariablesQualitatives(self):
        liste = [];
        for i in range(0, len(self.dataFrame.dtypes)):
            if self.dataFrame.dtypes[i] == "object":
                liste.append(self.dataFrame.columns.values[i]);
        return liste;

    def getNbVariablesQualitatives(self):
        return len(self.getListeVariablesQualitatives());

    def getListeVariablesQuantitatives(self):
        liste = [];
        for i in range(0, len(self.dataFrame.dtypes)):
            if self.dataFrame.dtypes[i] == "float64" or self.dataFrame.dtypes[i] == "int64":
                liste.append(self.dataFrame.columns.values[i]);
        return liste;

    def getNbVariablesQuantitatives(self):
        return len(self.getListeVariablesQuantitatives());

    def getModalites(self):
        val = "";
        for i in range(1, self.getNbVariablesQualitatives()):
            val += self.dataFrame.columns.values[i].__str__() + " -> "+ self.dataFrame[self.getListeVariablesQualitatives()[i]].nunique().__str__() + "\n";
        return val;

    def getNbFrequences(self):
        print("");

    def getNbEffectifs(self):
        val = "";
        for i in range(0, self.getNbVariablesQualitatives()):
            val += self.dataFrame[self.getListeVariablesQualitatives()[i]].value_counts().__str__() + "\n";
        return val;

    def getValeurMin(self):
        valeurMin = "";
        for i in range(0, self.getNbVariablesQuantitatives()):
            colonneMin = self.getListeVariablesQuantitatives()[i] + " -> ";
            valeurMin += colonneMin + self.dataFrame[self.getListeVariablesQuantitatives()[i]].min().__str__() + "\n";
        return valeurMin;

    def getValeurMax(self):
        valeurMax = "";
        for i in range(0, self.getNbVariablesQuantitatives()):
            colonneMax = self.getListeVariablesQuantitatives()[i] + " -> ";
            valeurMax += colonneMax + self.dataFrame[self.getListeVariablesQuantitatives()[i]].max().__str__() + "\n";
        return valeurMax;

    def getMediane(self):
        valeurMediane = "";
        for i in range(0, self.getNbVariablesQuantitatives()):
            colonneMediane = self.getListeVariablesQuantitatives()[i] + " -> ";
            valeurMediane += colonneMediane + self.dataFrame[self.getListeVariablesQuantitatives()[i]].median().__str__() + "\n";
        return valeurMediane;

    def getMoyenne(self):
        valeurMoyenne = "";
        for i in range(0, self.getNbVariablesQuantitatives()):
            colonneMoyenne = self.getListeVariablesQuantitatives()[i] + " -> ";
            valeurMoyenne += colonneMoyenne + self.dataFrame[self.getListeVariablesQuantitatives()[i]].mean().__str__() + "\n";
        return valeurMoyenne;

    def getEcartType(self):
        valeurEcartType = "";
        for i in range(0, self.getNbVariablesQuantitatives()):
            colonneEcartType = self.getListeVariablesQuantitatives()[i] + " -> ";
            valeurEcartType += colonneEcartType + self.dataFrame[self.getListeVariablesQuantitatives()[i]].std().__str__() + "\n";
        return valeurEcartType;