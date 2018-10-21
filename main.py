import argparse
import files
import readDataFrame

parser = argparse.ArgumentParser();
parser.add_argument("-f","--filepath", nargs="?", help="Chemin du fichier de donnees");
parser.add_argument("-u","--user", action="store_true", help="Activer l'interaction utilisateur");
parser.add_argument("-l","--log", action="store_true", help="Activer l'enregistrement dans un fichier de log");
args=parser.parse_args();

path = args.filepath;

mainFile = files.File(path);

dataFrame = readDataFrame.ReadDataFrame(path);

print("Taille du fichier : " + mainFile.getTailleFichier() + " Ko");

print("Dernière modification : " + mainFile.getDateDerniereModification());

print("Encodage : " + mainFile.getTypeEncodage());

#print(mainFile.getInfosFichier());

print("Nombre de variables : " + dataFrame.getNbVariables().__str__());

print("Nombre d'observations : " + dataFrame.getNbObservations().__str__());

print("Nombres de variables qualitatives : " + dataFrame.getNbVariablesQualitatives().__str__());

if dataFrame.getNbVariablesQualitatives() != 0:
    print("Nom des variables qualitatives :" + dataFrame.getListeVariablesQualitatives().__str__());
else:
   print("Pas de variables qualitatives");

print("Nombres de variables quantitatives : " + dataFrame.getNbVariablesQuantitatives().__str__());

if dataFrame.getNbVariablesQuantitatives() != 0:
    print("Nom des variables quantitatives :" + dataFrame.getListeVariablesQuantitatives().__str__());
else:
   print("Pas de variables quantitatives");

print("Les valeurs minimales des variables quantitatives sont :\n" + dataFrame.getValeurMin());

print("Les valeurs maximales des variables quantitatives sont :\n" + dataFrame.getValeurMax());

print("Les valeurs medianes des variables quantitatives sont :\n" + dataFrame.getMediane());

print("Les moyennes des variables quantitatives sont :\n" + dataFrame.getMoyenne());

print("Les ecarts types des variables quantitatives sont :\n" + dataFrame.getEcartType());

print("Le nombre d'effectifs des variables qualitatives : \n" + dataFrame.getNbEffectifs());

print("Les modalités des variables qualitatives : \n" + dataFrame.getModalites());

print("Les fréquences des variables qualitatives : \n" + dataFrame.getNbFrequences());