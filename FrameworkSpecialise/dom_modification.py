import os

from xml.dom.minidom import parse
path = os.path.join(os.path.dirname(__file__), "livres.xml")
document = parse(path)
root = document.documentElement

livres = root.getElementsByTagName("livre")

for livre in livres:
    livre_id = livre.getAttribute("id")
    print(f"livre id {livre_id}")
    titre_element = livre.getElementsByTagName("titre")[0]
    print(f"titre {titre_element.firstChild.nodeValue}")
    auteur_element = livre.getElementsByTagName("auteur")[0]
    print(f"auteur {auteur_element.firstChild.nodeValue}")