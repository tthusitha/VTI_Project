class ReadDataFrame :

    def __init__(self, dataFrame):
        self.dataFrame = dataFrame;

    def getNbVariables(self):
        return "Nombre de variable : " + self.dataFrame.shape[1].__str__();

    def getNbObservations(self):
        return "Nombre d'observations : " + self.dataFrame.shape[0].__str__();

    def getListeVariablesQualitatives(self):
        liste = [];
        for i in range(0, len(self.dataFrame.dtypes)):
            if self.dataFrame.dtypes[i] == "object":
                liste.append(self.dataFrame.columns.values[i]);
        return liste;

    def getNbVariablesQualitatives(self):
        return len(self.getListeVariablesQualitatives());

    def getListeNomsVariablesQualitatives(self):
        nom = [];
        for i in range(0, self.getNbVariablesQualitatives()):
            nom.append(self.getListeVariablesQualitatives()[i]);
        return nom;

    def getListeVariablesQuantitatives(self):
        liste = [];
        for i in range(0, len(self.dataFrame.dtypes)):
            if self.dataFrame.dtypes[i] == "float64" or self.dataFrame.dtypes[i] == "int64":
                liste.append(self.dataFrame.columns.values[i]);
        return liste;

    def getNbVariablesQuantitatives(self):
        return len(self.getListeVariablesQuantitatives());

    def getListeNomsVariablesQuantitatives(self):
        nom = [];
        for i in range(0, self.getNbVariablesQuantitatives()):
            nom.append(self.getListeVariablesQuantitatives()[i]);
        return nom;

    def getNbModalites(self):
        print("");

    def getNbEffectifs(self):
        print("");

    def getNbFrequences(self):
        print("");

    def getValeurMin(self):
        valeurMin = "";
        print("Les valeurs minimales des variables quantitatives sont :")
        for i in range(0, self.getNbVariablesQuantitatives()):
            colonneMin = self.getListeNomsVariablesQuantitatives()[i] + " -> ";
            valeurMin += colonneMin + self.dataFrame[self.getListeNomsVariablesQuantitatives()[i]].min().__str__() + "\n";
        return valeurMin;

    def getValeurMax(self):
        valeurMax = "";
        print("Les valeurs maximales des variables quantitatives sont :")
        for i in range(0, self.getNbVariablesQuantitatives()):
            colonneMax = self.getListeNomsVariablesQuantitatives()[i] + " -> ";
            valeurMax += colonneMax + self.dataFrame[self.getListeNomsVariablesQuantitatives()[i]].max().__str__() + "\n";
        return valeurMax;

    def getMediane(self):
        valeurMediane = "";
        print("Les valeurs medianes des variables quantitatives sont :")
        for i in range(0, self.getNbVariablesQuantitatives()):
            colonneMediane = self.getListeNomsVariablesQuantitatives()[i] + " -> ";
            valeurMediane += colonneMediane + self.dataFrame[self.getListeNomsVariablesQuantitatives()[i]].median().__str__() + "\n";
        return valeurMediane;

    def getMoyenne(self):
        valeurMoyenne = "";
        print("Les moyennes des variables quantitatives sont :")
        for i in range(0, self.getNbVariablesQuantitatives()):
            colonneMoyenne = self.getListeNomsVariablesQuantitatives()[i] + " -> ";
            valeurMoyenne += colonneMoyenne + self.dataFrame[self.getListeNomsVariablesQuantitatives()[i]].mean().__str__() + "\n";
        return valeurMoyenne;

    def getEcartType(self):
        valeurEcartType = "";
        print("Les ecarts types des variables quantitatives sont :")
        for i in range(0, self.getNbVariablesQuantitatives()):
            colonneEcartType = self.getListeNomsVariablesQuantitatives()[i] + " -> ";
            valeurEcartType += colonneEcartType + self.dataFrame[self.getListeNomsVariablesQuantitatives()[i]].std().__str__() + "\n";
        return valeurEcartType;