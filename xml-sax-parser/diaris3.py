from xml.sax import parse
from xml.sax.handler import ContentHandler

class Diaris3SAXParser(ContentHandler):

    def __init__(self, htmlFileName):
        super().__init__()
        # obro el fitxer en mode escriptura
        self.file = open(htmlFileName, "w")

        # escric la capçalera del document HTML
        self.file.write("<html><head><title>Diaris v3</title></head><body>")

        # variables on guardaré el contingut dels elements actuals
        self.currentId = None
        self.currentNom = None
        self.currentUrl = None

        # variable per saber si estic dins de una etiqueta
        self.insideNom = False
        self.insideUrl = False

    def __del__(self):
        # escric el final del document HTML
        self.file.write("</body></html>")

        # tanco el fitxer
        self.file.close()

    def startElement(self, name, attrs):
        if (name == "diari"):
            self.currentId = attrs.get("id")
        elif (name == "nom"):
            self.insideNom = True
        elif (name == "url"):
            self.insideUrl = True

    def endElement(self, name):
        if (name == "diari"):
            self.writeHTML()

    def characters(self, content):
        if content.strip() != "": # no mostro els espais en blanc innecessaris
            if(self.insideNom):
                self.currentNom = content
                self.insideNom = False
            elif(self.insideUrl):
                self.currentUrl = content
                self.insideUrl = False

    def writeHTML(self):
        self.file.write("<p>")
        self.file.write(f"<a id='{self.currentId}' href='{self.currentUrl}'>#{self.currentId} {self.currentNom}</a>")
        self.file.write("</p>")

parse("diaris.xml", Diaris3SAXParser("diaris.html"))
