import argparse
from Classes import constant, file, readDataFrame, interfaceUtilisateur, log

try:
    parser = argparse.ArgumentParser();
    parser.add_argument(constant.Constant.PARAM_CHEMIN_FICHIER,"--filepath", nargs="?", help="Chemin du fichier à traiter");
    parser.add_argument(constant.Constant.PARAM_INTERACTION_UTILISATEUR,"--user", action="store_true", help="Activer l'interaction avec l'utilisateur");
    parser.add_argument(constant.Constant.PARAM_LOG,"--log", nargs="?", help="Activer l'enregistrement dans un fichier de log");
    args = parser.parse_args();

    # Récupérer le paramètre et instancier les classes File et ReadDataFrame
    path = args.filepath;
    fichier = file.File(path);
    dataFrame = readDataFrame.ReadDataFrame(path);

    # Instancier la classe InterfaceUtilisateur
    interfaceUtilisateur = interfaceUtilisateur.InterfaceUtilisateur("------------- Traitement des données -------------", fichier, dataFrame);

    # Nettoyer le terminal et afficher l'en-tête
    interfaceUtilisateur.nettoyerTerminal();
    interfaceUtilisateur.getAfficher().afficherEnTete();

    # Vérifier si l'interaction utilisateur est choisi
    if args.user:

        # Vérifier si la sauvegarde en fichier de log est choisi
        if args.log:
            fichierLog = log.Log(args.log, fichier, dataFrame);
            fichierLog.sauvegarder();

            choixDepart = "";
            choixAffichage = "";

            # Tant que l'utilisateur ne veut pas quitter on continue
            while choixDepart != constant.Constant.PARAM_QUITTER :
                interfaceUtilisateur.getAfficher().afficherMenuPrincipal();
                choixDepart = interfaceUtilisateur.reponse("Réponse: ");

                # Tant que l'utilisateur ne veut pas quitter et ne fais pas retour on continue
                while choixDepart != constant.Constant.PARAM_QUITTER and choixAffichage != constant.Constant.PARAM_RETOUR :

                    # Si l'utilisateur veut voir les informations concernant le fichier
                    if choixDepart == constant.Constant.PARAM_INFO_FICHIER :
                        interfaceUtilisateur.getAfficher().afficherMenuSuivant();
                        interfaceUtilisateur.getAfficher().afficherMenuFichier();

                    # Si l'utilisateur veut voir les informations concernant les données du fichier
                    elif choixDepart == constant.Constant.PARAM_INFO_DONNEES :
                        interfaceUtilisateur.getAfficher().afficherMenuSuivant();
                        interfaceUtilisateur.getAfficher().afficherMenuDonnees();

                    # Si l'utilisateur souhaite quitter
                    elif choixDepart == constant.Constant.PARAM_QUITTER :
                        break;

                    # Si l'utilisateur entre une commande inconnu
                    else:
                        interfaceUtilisateur.getAfficher().afficherCommandeInvalide();
                        break;

                    choixAffichage = interfaceUtilisateur.reponse("Réponse: ");

                    # Si l'utilisateur veut voir la taille du fichier
                    if choixAffichage == constant.Constant.PARAM_TAILLE_FICHIER :
                        interfaceUtilisateur.getAfficher().afficherTailleFichier();

                    # Si l'utilisateur veut voir le type d'encodage du fichier
                    elif choixAffichage == constant.Constant.PARAM_ENCODAGE_FICHIER :
                        interfaceUtilisateur.getAfficher().afficherTypeEncodage();

                    # Si l'utilisateur veut voir la date de la dernière modification
                    elif choixAffichage == constant.Constant.PARAM_DERNIERE_MODIF_FICHIER :
                        interfaceUtilisateur.getAfficher().afficherDateDerniereModification();

                    # Si l'utilisateur veut voir toutes les infos concernant le fichier
                    elif choixAffichage == constant.Constant.PARAM_TOUT_INFOS_FICHIER :
                        interfaceUtilisateur.getAfficher().afficherInfosFichier();

                    # Si l'utilisateur veut voir les informations des données de la table
                    elif choixAffichage == constant.Constant.PARAM_INFOS_TABLE :
                        interfaceUtilisateur.getAfficher().afficherInfosDonneesTable();

                    # Si l'utilisateur veut voir les informations des données quantitatives
                    elif choixAffichage == constant.Constant.PARAM_INFOS_QUANTITATIVE :
                        interfaceUtilisateur.getAfficher().afficherInfosDonneesQuantitatives();

                    # Si l'utilisateur veut voir les informations des données qualitatives
                    elif choixAffichage == constant.Constant.PARAM_INFOS_QUALITATIVE :
                        interfaceUtilisateur.getAfficher().afficherInfosDonnesQualitatives();

                    # Génerer le plot de distribution
                    elif choixAffichage == constant.Constant.PARAM_PLOT :
                        interfaceUtilisateur.getAfficher().afficherGenerationSuccesPlot();
                        dataFrame.genererGraph();

                    # Si l'utilisateur souhaite revenir en arrière
                    elif choixAffichage == constant.Constant.PARAM_RETOUR :
                        choixAffichage = False;
                        break;

                    # Si l'utilisateur entre une commande inconnu
                    else:
                        interfaceUtilisateur.getAfficher().afficherCommandeInvalide();
                        break;
    else:
        # Afficher toutes les informations
        interfaceUtilisateur.getAfficher().afficherTout();

        # Génerer le plot de distribution
        interfaceUtilisateur.getAfficher().afficherGenerationSuccesPlot();
        dataFrame.genererGraph();

        # Sauvegarder en fichier
        fichierLog = log.Log("log.txt", fichier, dataFrame);
        fichierLog.sauvegarder();

    interfaceUtilisateur.reponse("Veuillez appuyer sur un bouton pour continuer....");
    interfaceUtilisateur.nettoyerTerminal();
    interfaceUtilisateur.getAfficher().afficher("Merci d'avoir utilisé cette application :)");

except KeyboardInterrupt:
    exit();