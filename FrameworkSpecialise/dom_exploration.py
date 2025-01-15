import os

from xml.dom.minidom import parse

path = os.path.join(os.path.dirname(__file__), "livres.xml")
document = parse(path)
root = document.documentElement

nouveau_livre_element = document.createElement("livre")
nouveau_livre_element.setAttribute("id", str(3))

titre_element = document.createElement("titre")
titre_text = document.createTextNode("Livre C")
titre_element.appendChild(titre_text)
nouveau_livre_element.appendChild(titre_element)

auteur_element = document.createElement("auteur")
auteur_text = document.createTextNode("Auteur C")
auteur_element.appendChild(auteur_text)
nouveau_livre_element.appendChild(auteur_element)

root.appendChild(nouveau_livre_element)

with open(os.path.join(os.path.dirname(__file__), "livres_modified.xml"), "a") as file:
    document.writexml(file)