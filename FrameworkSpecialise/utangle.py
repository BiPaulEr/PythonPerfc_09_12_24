
import untangle
import os

path = os.path.join(os.path.dirname(__file__), "livres.xml")
tree = untangle.parse(path)

for livre in tree.livres.livre:
    print(f"ID : {livre['id']}")
    print(f"Titre : {livre.titre.cdata}")
    print(f"Auteur : {livre.auteur.cdata}")