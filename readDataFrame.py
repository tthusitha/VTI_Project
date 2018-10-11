class ReadDataFrame :

    def __init__(self, dataFrame):
        self.dataFrame = dataFrame;
        self.listeNomsVariablesQualitatives = [];
        self.listeNomsVariablesQuantitatives = [];

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

    #def getNbVariablesQualitatives(self):
     #   result = 0;
      #  for i in range(0, len(self.getListeVariablesQualitatives())):
       #     result += 1;
        #    self.listeNomsVariablesQualitatives = self.dataFrame.columns.values;
        #return "Nombres de variables qualitatives : " + result.__str__();

    def getNbVariablesQualitatives(self):
        return len(self.getListeVariablesQualitatives());

    def getNomVariablesQualitatives(self):
        nom = [];
        if self.getNbVariablesQualitatives() != 0:
            print("Nom des variables qualitatives :");
            for i in range(0, self.getNbVariablesQualitatives()):
                nom.append(self.getListeVariablesQualitatives()[i]);
            return nom;
        else:
            return "Pas de variables qualitatives";

    def getListeVariablesQuantitatives(self):
        liste = [];
        for i in range(0, len(self.dataFrame.dtypes)):
            if self.dataFrame.dtypes[i] == "float64" or self.dataFrame.dtypes[i] == "int64":
                liste.append(self.dataFrame.columns.values[i]);
        return liste;

    #def getNbVariablesQuantitatives(self):
     #   result = 0;
     #   for i in range(0, len(self.getListeVariablesQuantitatives())):
    #        result += 1;
     #       self.listeNomsVariablesQuantitatives = self.dataFrame.columns.values;
      #  return "Nombres de variables quantitatives : " + result.__str__();

    def getNbVariablesQuantitatives(self):
        return len(self.getListeVariablesQuantitatives());

    def getNomVariablesQuantitatives(self):
        nom = [];
        if self.listeNomsVariablesQuantitatives != 0:
            print("Nom des variables quantitaves :");
            for i in range(0, self.getNbVariablesQuantitatives()):
                nom.append(self.getListeVariablesQuantitatives()[i]);
            return nom;
        else:
            return "Pas de variables quantitatives";

    def getNbModalites(self):
        print("");

    def getNbEffectifs(self):
        print("");

    def getNbFrequences(self):
        print("");

    def getValeurMin(self):
        valeurMin = "";
        print("Les valeurs minimales des variables quantitatives sont :")
        for i in range(0, len(self.listeNomsVariablesQuantitatives)):
            colonneMin = self.listeNomsVariablesQuantitatives[i] + " -> ";
            valeurMin += colonneMin + self.dataFrame[self.listeNomsVariablesQuantitatives[i]].min().__str__() + "\n";
        return valeurMin;

    def getValeurMax(self):
        valeurMax = "";
        print("Les valeurs maximales des variables quantitatives sont :")
        for i in range(0, len(self.listeNomsVariablesQuantitatives)):
            colonneMax = self.listeNomsVariablesQuantitatives[i] + " -> ";
            valeurMax += colonneMax + self.dataFrame[self.listeNomsVariablesQuantitatives[i]].max().__str__() + "\n";
        return valeurMax;

    def getMediane(self):
        valeurMediane = "";
        print("Les valeurs medianes des variables quantitatives sont :")
        for i in range(0, len(self.listeNomsVariablesQuantitatives)):
            colonneMediane = self.listeNomsVariablesQuantitatives[i] + " -> ";
            valeurMediane += colonneMediane + self.dataFrame[self.listeNomsVariablesQuantitatives[i]].median().__str__() + "\n";
        return valeurMediane;

    def getMoyenne(self):
        valeurMoyenne = "";
        print("Les moyennes des variables quantitatives sont :")
        for i in range(0, len(self.listeNomsVariablesQuantitatives)):
            colonneMoyenne = self.listeNomsVariablesQuantitatives[i] + " -> ";
            valeurMoyenne += colonneMoyenne + self.dataFrame[self.listeNomsVariablesQuantitatives[i]].mean().__str__() + "\n";
        return valeurMoyenne;

    def getEcartType(self):
        valeurEcartType = "";
        print("Les ecarts types des variables quantitatives sont :")
        for i in range(0, len(self.listeNomsVariablesQuantitatives)):
            colonneEcartType = self.listeNomsVariablesQuantitatives[i] + " -> ";
            valeurEcartType += colonneEcartType + self.dataFrame[self.listeNomsVariablesQuantitatives[i]].std().__str__() + "\n";
        return valeurEcartType;