import random

# Demander le nom et le prénom à l'utilisateur
nom = input("Entrez votre nom : ")
prenom = input("Entrez votre prénom : ")

# Affichage du premier texte
print(f"Bonjour {nom}, vous êtes reconnu dans notre système.")
# Lecture du contenu du fichier database.txt
with open("database.txt", "r") as file:
    pseudo_list = file.read().split(",")

# Calcul de la quantité de pseudos déjà générés
quantite = len(pseudo_list)

# Affichage du deuxième texte
print(f"Nous avons déjà généré des pseudos pour {quantite} personne(s) déjà.")

# Génération des trois pseudos
initials = "".join([word[0] for word in (nom + " " + prenom).split()])
character_count = len(initials.replace(" ", ""))
pseudo1 = initials + str(character_count)
pseudo2 = (nom + prenom).replace(" ", "").title()
shortest_name = nom if len(nom) < len(prenom) else prenom
pseudo3 = shortest_name[::-1] + str(random.randint(100, 1000))

# Liste des pseudos générés
pseudos = [pseudo1, pseudo2, pseudo3]

# Choix aléatoire d'un pseudo favorable
pseudos_favorables = [pseudo for pseudo in pseudos if len(pseudo) <= 7]
pseudo_favori = random.choice(pseudos_favorables)

# Affichage des pseudos et du pseudo favori
print("\nPseudos générés :")
for i, pseudo in enumerate(pseudos, start=1):
    print(f"Pseudo {i}: {pseudo}")
print("\nLe pseudo le plus favorable est :", pseudo_favori)

# Enregistrement du pseudo favori dans le fichier database.txt
with open("database.txt", "a") as file:
    file.write(pseudo_favori + ",")

print("Le pseudo favori a été enregistré dans le fichier database.txt.")
