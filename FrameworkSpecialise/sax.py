import os
import xml.sax

path = os.path.join(os.path.dirname(__file__), "livres.xml")

class Handler(xml.sax.ContentHandler):
    def startDocument(self):
        print("Entree dans le document")
        return super().startDocument()
    
    def endDocument(self):
        print("Sortie du document")
        return super().endDocument()
    def startElement(self, name, attrs):
        if name == "livre":
            print(f"DEBUT {name} {attrs["id"]}")
        return super().startElement(name, attrs)
    
    def endElement(self, name):
        if name == "livre":
            print(f"END {name}")
        return super().endElement(name)
    
    def characters(self, content):
        content = content.strip()
        if (content):
            print(f"Text found : {content}")
        return super().characters(content)

parser = xml.sax.make_parser()
handler = Handler()
parser.setContentHandler(handler)

with open(path) as file:
    parser.parse(file)