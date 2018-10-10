import argparse
import files

parser = argparse.ArgumentParser();
#TODO ajouter les arguments pour les interactions avec l'utilisateur

path = "file.csv";

mainFile = files.File(path);

print(mainFile.readFile());

print(mainFile.getSizeFile());

print(mainFile.getLastModifiedDate());

print(mainFile.getEncodingType());

print(mainFile.toString());

print(mainFile.getNbVariables());

print(mainFile.getNbObservations());

print(mainFile.getNbVariablesQualitatives());

print(mainFile.getNomVariablesQualitatives());

print(mainFile.getNbVariablesQuantitatives());

print(mainFile.getNomVariablesQuantitatives());

print(mainFile.getValeurMin());

print(mainFile.getValeurMax());

print(mainFile.getMediane());

print(mainFile.getMoyenne());

print(mainFile.getEcartType());