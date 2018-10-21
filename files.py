from pathlib import Path
from datetime import datetime
import chardet

# Classe Fichier
class File :

    # Constructeur
    def __init__(self, path):
        self.path = path;
        self.pathFichier = Path(self.path);

    # Retourner la taille du fichier
    def getTailleFichier(self) :
        tailleFichier = self.pathFichier.stat().st_size.__str__();
        return tailleFichier;

    # Retourner la date de la dernière modification
    def getDateDerniereModification(self) :
        derniereModifTime = self.pathFichier.stat().st_mtime;
        derniereModifTimeFormat = datetime.fromtimestamp(derniereModifTime).__str__();
        return derniereModifTimeFormat;

    # Retourner le type d'encodage
    def getTypeEncodage(self) :
        bytes = self.pathFichier.read_bytes();
        encoding = chardet.detect(bytes);
        return encoding.get("encoding");