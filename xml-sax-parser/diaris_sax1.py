from xml.sax import parse
from xml.sax.handler import ContentHandler

class Diaris1SAXParser(ContentHandler):

    def startElement(self, name, attrs):
        if (name == "diaris"):
            print("<html><head><title>Diaris v1</title></head><body>")
        elif (name == "diari"):
            id = attrs.get("id")
            print("<div>")
            print("<h1>" + id + "</h1>")
        elif (name == "nom"):
            print("<h2>")
        elif (name == "url"):
            print("<h3>")

    def endElement(self, name):
        if (name == "diaris"):
            print("</body></html>")
        elif (name == "diari"):
            print("</div>")
        elif (name == "nom"):
            print("</h2>")
        elif (name == "url"):
            print("</h3>")

    def characters(self, content):
        if content.strip() != "": # no mostro els espais en blanc innecessaris
            print(content)

parse("diaris.xml", Diaris1SAXParser())
