import functions
# Liste qui contient toutes les équipes du tournoi

equipes = []

# Écran d'accueil animé, affiché une seule fois au lancement

functions.ecran_accueil()

# Boucle principale : le menu revient tant qu'on ne choisit pas de quitter


while True:
    print()
    print(functions.JAUNE + functions.GRAS + "=== MENU TOURNOI ===" + functions.RESET)
    print("1. Ajouter une équipe")
    print("2. Afficher toutes les équipes")
    print("3. Saisir résultat d'un match")
    print("4. Rechercher une équipe")
    print("5. Afficher le classement")
    print("6. Quitter")
    print("7. Afficher les statistiques")
    print("8. Classement (tri manuel)")
    print("9. Comparer les recherches")
    print("10. Générer tous les matchs")
    print("11. Simuler tout le championnat")

# input() renvoie du texte, d'où les guillemets dans les comparaisons

    choix = input("Votre choix : ")

    if choix == "1":
        functions.ajouter_equipe(equipes)
    elif choix == "2":
        functions.afficher_equipes(equipes)
        print(functions.generer_matchs(equipes))
    elif choix == "3":
        functions.saisir_match(equipes)
    elif choix == "4":
        nom = input("Nom de l'équipe : ")
        resultat = functions.recherche_lineaire(equipes, nom)
        if resultat is None:
            print("Équipe introuvable")
        else:
            print("Resultat :", resultat["points"], "pts | V:", resultat["victoires"], "N:", resultat["nuls"], "D:", resultat["defaites"], "| Buts:", resultat["buts_marques"], "-", resultat["buts_encaisses"])
    elif choix == "5":
        functions.afficher_classement(equipes)
    elif choix == "6":
        print("Au revoir !")
        break
    elif choix == "7":
        functions.afficher_statistiques(equipes)
    elif choix == "8":
        print("=== CLASSEMENT (TRI MANUEL) ===")
        functions.afficher_equipes(functions.tri(equipes))
    elif choix == "9":
        functions.comparer_recherches(equipes)
    elif choix == "10":
        print("=== TOUS LES MATCHS POSSIBLES ===")
        for match in functions.generer_matchs(equipes):
         print(match[0], "vs", match[1])
    elif choix == "11":
        functions.simuler_championnat(equipes)
    else:
        print("Choix invalide")

        