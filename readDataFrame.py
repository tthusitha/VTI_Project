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
                liste.append(self.dataFrame.dtypes[i]);
        return liste;

    def getNbVariablesQualitatives(self):
        result = 0;
        for i in range(0, len(self.getListeVariablesQualitatives())):
            result += 1;
            self.listeNomsVariablesQualitatives = self.dataFrame.columns.values;
        return "Nombres de variables qualitatives : " + result.__str__();

    def getNomVariablesQualitatives(self):
        nom = "";
        if len(self.listeNomsVariablesQualitatives) != 0:
            print("Nom des variables qualitatives :");
            for i in range(0, len(self.listeNomsVariablesQualitatives)):
                nom += self.listeNomsVariablesQualitatives[i] + "\n";
            return nom;
        else:
            return "Pas de variables qualitatives";

    def getListeVariablesQuantitatives(self):
        liste = [];
        for i in range(0, len(self.dataFrame.dtypes)):
            if self.dataFrame.dtypes[i] == "float64" or self.dataFrame.dtypes[i] == "int64":
                liste.append(self.dataFrame.dtypes[i]);
        return liste;

    def getNbVariablesQuantitatives(self):
        result = 0;
        for i in range(0, len(self.getListeVariablesQuantitatives())):
            result += 1;
            self.listeNomsVariablesQuantitatives = self.dataFrame.columns.values;
        return "Nombres de variables quantitatives : " + result.__str__();

    def getNomVariablesQuantitatives(self):
        nom = "";
        if len(self.listeNomsVariablesQuantitatives) != 0:
            print("Nom des variables quantitaves :");
            for i in range(0, len(self.listeNomsVariablesQuantitatives)):
                nom += self.listeNomsVariablesQuantitatives[i] + "\n";
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
        print("");

    def getValeurMax(self):
        print("");

    def getMediane(self):
        print("");

    def getMoyenne(self):
        print("");

    def getEcartType(self):
        print("");