from pathlib import Path
from datetime import datetime
import chardet
import pandas
from readDataFrame import ReadDataFrame

class File :

    def __init__(self, path):
        self.path = path;
        self.readDataFrame = "";

    def readFile(self) :
        pathFichier = Path(self.path);
        data = pandas.read_csv(pathFichier);
        self.readDataFrame = ReadDataFrame(data);
        return data;

    def getSizeFile(self) :
        pathFichier = Path(self.path);
        tailleFichier = pathFichier.stat().st_size.__str__();
        return "Taille du fichier : " + tailleFichier + " Ko";

    def getLastModifiedDate(self) :
        pathFichier = Path(self.path);
        derniereModifTime = pathFichier.stat().st_mtime;
        derniereModifTimeFormat = datetime.fromtimestamp(derniereModifTime).__str__();
        return "Dernière modification : " + derniereModifTimeFormat;

    def getEncodingType(self) :
        pathFichier = Path(self.path);
        bytes = pathFichier.read_bytes();
        encoding = chardet.detect(bytes);
        return "Encodage : " + encoding.get("encoding");

    def toString(self):
        return self.getSizeFile() + ", "+ self.getLastModifiedDate() + ", " + self.getEncodingType();

    def getNbVariables(self):
        return self.readDataFrame.getNbVariables();

    def getNbObservations(self):
        return self.readDataFrame.getNbObservations();

    def getNbVariablesQualitatives(self):
        return "Nombres de variables qualitatives : " + self.readDataFrame.getNbVariablesQualitatives().__str__();

    def getListeNomsVariablesQualitatives(self):
        if self.readDataFrame.getNbVariablesQualitatives() != 0:
            print("Nom des variables qualitatives :");
            return self.readDataFrame.getListeVariablesQualitatives();
        else:
            return "Pas de variables qualitatives";

    def getNbVariablesQuantitatives(self):
        return "Nombres de variables quantitatives : " + self.readDataFrame.getNbVariablesQuantitatives().__str__();

    def getListeNomsVariablesQuantitatives(self):
        if self.readDataFrame.getNbVariablesQuantitatives() != 0:
            print("Nom des variables quantitaves :");
            return self.readDataFrame.getListeVariablesQuantitatives();
        else:
            return "Pas de variables quantitatives";

    def getValeurMin(self):
        return self.readDataFrame.getValeurMin();

    def getValeurMax(self):
        return self.readDataFrame.getValeurMax();

    def getMediane(self):
        return self.readDataFrame.getMediane();

    def getMoyenne(self):
        return self.readDataFrame.getMoyenne();

    def getEcartType(self):
        return self.readDataFrame.getEcartType();