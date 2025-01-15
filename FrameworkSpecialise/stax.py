import os
import xml.etree.ElementTree as ET

path = os.path.join(os.path.dirname(__file__), "livres.xml")

tree = ET.parse(path)
root = tree.getroot()

for livre in root.iter('livre'):

    attrib = livre.attrib["id"]
    print(f"Attribut {attrib}")

    titre = livre.find("titre")
    print(titre.text)

    auteur = livre.find("auteur")
    print(auteur.text)


