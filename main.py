import argparse
import files
import readDataFrame

parser = argparse.ArgumentParser();
#TODO ajouter les arguments pour les interactions avec l'utilisateur

path = "file.csv";

mainFile = files.File(path);

dataFrame = readDataFrame.ReadDataFrame(path);

print(mainFile.getSizeFile());

print(mainFile.getLastModifiedDate());

print(mainFile.getEncodingType());

print(mainFile.toString());

print(dataFrame.getNbVariables());

print(dataFrame.getNbObservations());

print("Nombres de variables qualitatives : " + dataFrame.getNbVariablesQualitatives().__str__());

print("Nom des variables qualitatives :" + dataFrame.getListeVariablesQualitatives().__str__());

print("Nombres de variables quantitatives : " + dataFrame.getNbVariablesQuantitatives().__str__());

print("Nom des variables quantitatives :" + dataFrame.getListeVariablesQuantitatives().__str__());

#print(mainFile.getValeurMin());

#print(mainFile.getValeurMax());

#print(mainFile.getMediane());

#print(mainFile.getMoyenne());

#print(mainFile.getEcartType());