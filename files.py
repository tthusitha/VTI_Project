from pathlib import Path
from datetime import datetime
import chardet

class File :

    def __init__(self, path):
        self.path = path;
        self.pathFichier = Path(self.path);

    def getTailleFichier(self) :
        tailleFichier = self.pathFichier.stat().st_size.__str__();
        return tailleFichier;

    def getDateDerniereModification(self) :
        derniereModifTime = self.pathFichier.stat().st_mtime;
        derniereModifTimeFormat = datetime.fromtimestamp(derniereModifTime).__str__();
        return derniereModifTimeFormat;

    def getTypeEncodage(self) :
        bytes = self.pathFichier.read_bytes();
        encoding = chardet.detect(bytes);
        return encoding.get("encoding");

    def toString(self):
        return self.getTailleFichier() + ", " + self.getDateDerniereModification() + ", " + self.getTypeEncodage();