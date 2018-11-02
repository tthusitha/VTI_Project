import argparse
from Classes import constant, files, readDataFrame, interfaceUtilisateur, log

parser = argparse.ArgumentParser();
parser.add_argument(constant.Constant.PARAM_CHEMIN_FICHIER,"--filepath", nargs="?", help="Chemin du fichier de donnees");
parser.add_argument(constant.Constant.PARAM_INTERACTION_UTILISATEUR,"--user", action="store_true", help="Activer l'interaction utilisateur");
parser.add_argument(constant.Constant.PARAM_LOG,"--log", action="store_true", help="Activer l'enregistrement dans un fichier de log");
args=parser.parse_args();

path = args.filepath;

fichier = files.File(path);

dataFrame = readDataFrame.ReadDataFrame(path);

interfaceUtilisateur = interfaceUtilisateur.InterfaceUtilisateur("------------- Traitement des données -------------", fichier, dataFrame);

interfaceUtilisateur.nettoyerTerminal();
interfaceUtilisateur.getAfficher().afficherEnTete();

if args.user:
    if args.log:
        fichierLog = log.Log("log.txt", fichier, dataFrame);
        fichierLog.sauvegarder();

        mainAnswer = secondAnswer = "";

        while mainAnswer != constant.Constant.PARAM_QUITTER :
            interfaceUtilisateur.getAfficher().afficherMenuPrincipal();
            mainAnswer = interfaceUtilisateur.reponse("Réponse: ");
            while mainAnswer != constant.Constant.PARAM_QUITTER and secondAnswer != constant.Constant.PARAM_RETOUR :
                if mainAnswer == constant.Constant.PARAM_INFO_FICHIER :
                    interfaceUtilisateur.getAfficher().afficherMenuSuivant();
                    interfaceUtilisateur.getAfficher().afficherMenuFichier();
                elif mainAnswer == constant.Constant.PARAM_INFO_DONNEES :
                    interfaceUtilisateur.getAfficher().afficherMenuSuivant();
                    interfaceUtilisateur.getAfficher().afficherMenuDonnees();
                elif mainAnswer == constant.Constant.PARAM_QUITTER :
                    break;
                else:
                    interfaceUtilisateur.getAfficher().afficherCommandeInvalide();
                    break;
                secondAnswer = interfaceUtilisateur.reponse("Réponse: ");
                if secondAnswer == constant.Constant.PARAM_TAILLE_FICHIER :
                    interfaceUtilisateur.getAfficher().afficherTailleFichier();
                elif secondAnswer == constant.Constant.PARAM_ENCODAGE_FICHIER :
                    interfaceUtilisateur.getAfficher().afficherTypeEncodage();
                elif secondAnswer == constant.Constant.PARAM_DERNIERE_MODIF_FICHIER :
                    interfaceUtilisateur.getAfficher().afficherDateDerniereModification();
                elif secondAnswer == constant.Constant.PARAM_TOUT_INFOS_FICHIER :
                    interfaceUtilisateur.getAfficher().afficherInfosFichier();
                elif secondAnswer == constant.Constant.PARAM_INFOS_TABLE :
                    interfaceUtilisateur.getAfficher().afficherDonneesTable();
                elif secondAnswer == constant.Constant.PARAM_INFOS_QUANTITATIVE :
                    interfaceUtilisateur.getAfficher().afficherDonneesQuantitatives();
                elif secondAnswer == constant.Constant.PARAM_INFOS_QUALITATIVE :
                    interfaceUtilisateur.getAfficher().afficherDonnesQualitatives();
                #elif secondAnswer == gui.getDisplayer().DATA_INFORMATION_PLOT :
                    #interfaceUtilisateur.getAfficher().displayCreatePlotSuccess();
                    #dataFrame.createPlotBox();
                elif secondAnswer == constant.Constant.PARAM_RETOUR :
                    secondAnswer = False;
                    break;
                else:
                    interfaceUtilisateur.getAfficher().afficherCommandeInvalide();
                    break;
    else:
        #Afficher toutes les informations concernant le fichier
        interfaceUtilisateur.getAfficher().afficherInfosFichier();

        #Afficher toutes les informations concernant les données
        interfaceUtilisateur.getAfficher().afficherDonneesTable();

        #Afficher toutes les informations concernant les variables quantitatives
        interfaceUtilisateur.getAfficher().afficherDonneesQuantitatives();

        # Afficher toutes les informations concernant les variables qualitatives
        interfaceUtilisateur.getAfficher().afficherDonnesQualitatives();

        # interfaceUtilisateur.getAfficher().displayCreatePlotSuccess();
        # dataFrame.createPlotBox();

        # Sauvegarder en fichier
        if args.log:
            fichierLog = log.Log("log.txt", fichier, dataFrame);
            fichierLog.sauvegarder();

interfaceUtilisateur.nettoyerTerminal();
interfaceUtilisateur.getAfficher().afficher("Merci d'avoir utilisé cette application :)");