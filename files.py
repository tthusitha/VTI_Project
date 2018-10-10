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
        return self.readDataFrame.getNbVariablesQualitatives();

    def getNomVariablesQualitatives(self):
        return self.readDataFrame.getNomVariablesQualitatives();

    def getNbVariablesQuantitatives(self):
        return self.readDataFrame.getNbVariablesQuantitatives();

    def getNomVariablesQuantitatives(self):
        return self.readDataFrame.getNomVariablesQuantitatives();

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