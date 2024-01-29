from xml.sax import parse
from xml.sax.handler import ContentHandler

class Diaris2SAXParser(ContentHandler):

    def __init__(self, htmlFileName):
        super().__init__()
        # obro el fitxer en mode escriptura
        self.file = open(htmlFileName, "w")

    def __del__(self):
        # tanco el fitxer
        self.file.close()

    def startElement(self, name, attrs):
        if (name == "diaris"):
            self.file.write("<html><head><title>Diaris v2</title></head><body>")
        elif (name == "diari"):
            id = attrs.get("id")
            self.file.write("<div>")
            self.file.write("<h1>" + id + "</h1>")
        elif (name == "nom"):
            self.file.write("<h2>")
        elif (name == "url"):
            self.file.write("<h3>")

    def endElement(self, name):
        if (name == "diaris"):
            self.file.write("</body></html>")
        elif (name == "diari"):
            self.file.write("</div>")
        elif (name == "nom"):
            self.file.write("</h2>")
        elif (name == "url"):
            self.file.write("</h3>")

    def characters(self, content):
        if content.strip() != "": # no mostro els espais en blanc innecessaris
            self.file.write(content)

parse("diaris.xml", Diaris2SAXParser("diaris.html"))
