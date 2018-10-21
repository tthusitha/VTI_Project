from pathlib import Path
from datetime import datetime
import chardet

class File :

    def __init__(self, path):
        self.path = path;
        self.pathFichier = Path(self.path);

    def getSizeFile(self) :
        tailleFichier = self.pathFichier.stat().st_size.__str__();
        return tailleFichier;

    def getLastModifiedDate(self) :
        derniereModifTime = self.pathFichier.stat().st_mtime;
        derniereModifTimeFormat = datetime.fromtimestamp(derniereModifTime).__str__();
        return derniereModifTimeFormat;

    def getEncodingType(self) :
        bytes = self.pathFichier.read_bytes();
        encoding = chardet.detect(bytes);
        return encoding.get("encoding");

    def toString(self):
        return self.getSizeFile() + ", "+ self.getLastModifiedDate() + ", " + self.getEncodingType();