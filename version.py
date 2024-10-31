# Initialisation d'une liste pour stocker les notes
notes = []

print("Entrez vos notes. Tapez 'q' pour arrêter la saisie et calculer la moyenne.")

# Boucle pour entrer les notes
while True:
    # Demande une note à l'utilisateur
    entree = input("Entrez une note (ou 'q' pour terminer) : ")
    
    # Condition pour arrêter la saisie
    if entree.lower() == 'q':
        break
    
    try:
        # Conversion de l'entrée en flottant (nombre décimal)
        note = float(entree)
        
        # Vérification que la note est valide (entre 0 et 20)
        if 0 <= note <= 20:
            notes.append(note)
        else:
            print("La note doit être comprise entre 0 et 20.")
    
    except ValueError:
        print("Veuillez entrer un nombre valide ou 'q' pour quitter.")

# Calcul de la moyenne
if notes:
    moyenne = sum(notes) / len(notes)
    print(f"La moyenne générale est : {moyenne:.2f}")
else:
    print("Aucune note n'a été saisie.")