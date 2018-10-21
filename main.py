import argparse
import files
import readDataFrame

parser = argparse.ArgumentParser();
#TODO ajouter les arguments pour les interactions avec l'utilisateur

path = "file.csv";

mainFile = files.File(path);

dataFrame = readDataFrame.ReadDataFrame(path);

print("Taille du fichier : " + mainFile.getSizeFile() + " Ko");

print("Dernière modification : " + mainFile.getLastModifiedDate());

print("Encodage : " + mainFile.getEncodingType());

print(mainFile.toString());

print("Nombre de variables : " + dataFrame.getNbVariables().__str__());

print("Nombre d'observations : " + dataFrame.getNbObservations().__str__());

print("Nombres de variables qualitatives : " + dataFrame.getNbVariablesQualitatives().__str__());

print("Nom des variables qualitatives :" + dataFrame.getListeVariablesQualitatives().__str__());

print("Nombres de variables quantitatives : " + dataFrame.getNbVariablesQuantitatives().__str__());

print("Nom des variables quantitatives :" + dataFrame.getListeVariablesQuantitatives().__str__());

print(dataFrame.getValeurMin());

print(dataFrame.getValeurMax());

print(dataFrame.getMediane());

print(dataFrame.getMoyenne());

print(dataFrame.getEcartType());