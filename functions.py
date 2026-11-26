import time
import os
import random

# Codes couleur pour le terminal
CYAN = "\033[96m"
VERT = "\033[92m"
ROUGE = "\033[91m"
JAUNE = "\033[93m"
GRAS = "\033[1m"
RESET = "\033[0m"

# ============================================================
# Affichage et animations
# ============================================================
 
def effacer_ecran():
    
    """
    Efface le terminal (cls sur Windows, clear sur Mac et Linux).
    """

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def ecrire_lentement(texte, vitesse=0.03):
    
    """
    Affiche un texte lettre par lettre, comme une machine à écrire.
    """

    for lettre in texte:
        print(lettre, end="", flush=True)
        time.sleep(vitesse)
    print()


def ecran_accueil():
    
    """
    Affiche l'écran d'accueil animé au lancement du programme.
    """

    effacer_ecran()
    print(CYAN + GRAS + "=" * 40 + RESET)
    ecrire_lentement(CYAN + GRAS + "     ⚽  GESTIONNAIRE DE TOURNOI  ⚽" + RESET, 0.05)
    print(CYAN + GRAS + "=" * 40 + RESET)
    ecrire_lentement("Bienvenue ! Préparez vos équipes...")
    time.sleep(1)

# ============================================================
# Fonctionnalités obligatoires
# ============================================================

def ajouter_equipe(equipes):
    """
    Ajoute une ou plusieurs équipes. Pour plusieurs, l'utilisateur
    tape les noms séparés par des virgules. Les doublons sont refusés.
    """
    print("1. Ajouter une équipe")
    print("2. Ajouter plusieurs équipes d'un coup")
    mode = input("Votre choix : ")

    if mode == "1":
        noms = [input("Nom de l'équipe : ")]
    elif mode == "2":
        texte = input("Noms séparés par des virgules (ex : Paris, Lyon, Nice) : ")
        noms = texte.split(",")
    else:
        print(ROUGE + "Choix invalide" + RESET)
        return

    for nom in noms:
        nom = nom.strip()
        # On ignore les cases vides (par exemple deux virgules d'affilée)
        if nom == "":
            continue
        # On refuse les doublons
        if recherche_lineaire(equipes, nom) is not None:
            print(ROUGE + "L'équipe " + nom + " existe déjà !" + RESET)
            continue
        nouvelle_equipe = {
            "nom": nom,
            "victoires": 0,
            "nuls": 0,
            "defaites": 0,
            "buts_marques": 0,
            "buts_encaisses": 0,
            "points": 0
        }
        equipes.append(nouvelle_equipe)
        print(VERT + "Équipe " + nom + " ajoutée avec succès !" + RESET)

def afficher_equipes(equipes):
    """
    Affiche les équipes sous forme de tableau aligné, numérotées,
    avec la différence de buts en vert (positive) ou en rouge (négative).
    """
    if equipes == []:
        print("Aucune équipe enregistrée")
        return

    print(CYAN + GRAS + f"{'#':<4}{'Équipe':<16}{'Pts':>5}{'V':>4}{'N':>4}{'D':>4}{'Buts':>9}{'Diff':>7}" + RESET)
    print("-" * 53)

    numero = 1
    for equipe in equipes:
        diff = equipe["buts_marques"] - equipe["buts_encaisses"]
        buts = f"{equipe['buts_marques']}-{equipe['buts_encaisses']}"
        if diff > 0:
            couleur = VERT
        elif diff < 0:
            couleur = ROUGE
        else:
            couleur = RESET
        print(f"{numero:<4}{equipe['nom']:<16}{equipe['points']:>5}{equipe['victoires']:>4}"
              f"{equipe['nuls']:>4}{equipe['defaites']:>4}{buts:>9}" + couleur + f"{diff:>+7}" + RESET)
        numero = numero + 1

def recherche_lineaire(equipes, nom_recherche):

  """
  Parcourt la liste du début à la fin et compare chaque nom
  avec le nom recherché. Retourne la fiche si elle est trouvée, None sinon.
  """

  for equipe in equipes:
    if nom_recherche == equipe["nom"]:
     return equipe
  return None

def saisir_match(equipes):

  """
  Demande les deux équipes et leurs scores, vérifie qu'elles existent,
  puis met à jour les buts, victoires, nuls, défaites et points.
  """
  
  nom_equipe = input("nom de la première équipe : ")
  equipe1 = recherche_lineaire(equipes, nom_equipe)
  if equipe1 is None:
          print("Cette équipe n'existe pas !")
          return
  nom_equipe = input("nom de la deuxième équipe : ")
  equipe2 = recherche_lineaire(equipes, nom_equipe)
  if equipe2 is None:
          print("Cette équipe n'existe pas !")
          return
  if equipe1 is equipe2:
          print("Une équipe ne peut pas jouer contre elle-même !")
          return
  score1 = int(input("le score de l'equipe 1 : "))
  score2 = int(input("le score de l'equipe 2 : "))

  equipe1["buts_marques"] = equipe1["buts_marques"] + score1
  equipe2["buts_marques"] = equipe2["buts_marques"] + score2
  equipe1["buts_encaisses"] = equipe1["buts_encaisses"] + score2
  equipe2["buts_encaisses"] = equipe2["buts_encaisses"] + score1

  if score1 > score2 :
     
     print("L'équipe gagnante est : ", equipe1["nom"])
     print("L'équipe perdante est : ", equipe2["nom"])
     equipe1["victoires"] = equipe1["victoires"] + 1
     equipe1["points"] = equipe1["points"] + 3
     equipe2["defaites"] = equipe2["defaites"] + 1

  elif score1 < score2 :
     
     print("L'équipe gagnante est : ", equipe2["nom"])
     print("L'équipe perdante est : ", equipe1["nom"])
     equipe2["victoires"] = equipe2["victoires"] + 1
     equipe2["points"] = equipe2["points"] + 3
     equipe1["defaites"] = equipe1["defaites"] + 1

  else:
     
     print("match nul")
     equipe1["nuls"] = equipe1["nuls"] + 1
     equipe2["nuls"] = equipe2["nuls"] + 1
     equipe1["points"] = equipe1["points"] + 1
     equipe2["points"] = equipe2["points"] + 1

def afficher_classement(equipes):

    """
    Trie les équipes avec sorted() par points (décroissant),
    puis par différence de buts en cas d'égalité, et affiche le classement.
    """
    equipes_triees = sorted(equipes, key=lambda e: (e["points"], e["buts_marques"] - e["buts_encaisses"]), reverse=True)
    print("=== CLASSEMENT ===")
    afficher_equipes(equipes_triees)

def calculer_points_recursif(victoires, nuls, defaites):

   """
   Calcule les points de manière récursive : 3 par victoire, 1 par nul.
   La fonction s'appelle elle-même avec une victoire ou un nul de moins,
   jusqu'au cas de base : plus de victoires ni de nuls.
   """

   if victoires == 0 and nuls == 0:
    return 0
   elif  victoires > 0:
        return 3 + calculer_points_recursif(victoires - 1, nuls, defaites)
   else: 
    return 1 + calculer_points_recursif(victoires, nuls - 1, defaites)

def generer_matchs(equipes):

   """
   Génère tous les matchs possibles : chaque équipe joue contre
   les équipes placées après elle, sans doublon.
   Retourne une liste de tuples (equipe1, equipe2).
   """
   matchs = []
   for i in range(len(equipes)):
    for j in range(i + 1, len(equipes)):
       matchs.append((equipes[i]["nom"], equipes[j]["nom"]))
   return matchs
def ligne_stat(label, valeur):
    """
    Affiche une ligne du tableau des statistiques.
    """
    print(f"| {label:<32}| {str(valeur):<28}|")


def afficher_statistiques(equipes):
    """
    Affiche dans un tableau l'équipe avec le plus de points, la meilleure
    attaque, la meilleure défense, les buts, les matchs joués, et vérifie
    les points du leader avec la fonction récursive.
    """
    if equipes == []:
        print("Aucune équipe enregistrée")
        return

    plus_de_points = max(equipes, key=lambda e: e["points"])
    meilleure_attaque = max(equipes, key=lambda e: e["buts_marques"])
    meilleure_defense = min(equipes, key=lambda e: e["buts_encaisses"])
    total_buts = sum(e["buts_marques"] for e in equipes)
    moyenne = round(total_buts / len(equipes), 2)
    total_matchs = sum(e["victoires"] + e["nuls"] + e["defaites"] for e in equipes) // 2
    points_verifies = calculer_points_recursif(plus_de_points["victoires"], plus_de_points["nuls"], plus_de_points["defaites"])

    print(CYAN + GRAS + "=== STATISTIQUES ===" + RESET)
    print("+" + "-" * 33 + "+" + "-" * 29 + "+")
    ligne_stat("Plus de points", plus_de_points["nom"] + " (" + str(plus_de_points["points"]) + " pts)")
    ligne_stat("Meilleure attaque", meilleure_attaque["nom"] + " (" + str(meilleure_attaque["buts_marques"]) + " buts)")
    ligne_stat("Meilleure défense", meilleure_defense["nom"] + " (" + str(meilleure_defense["buts_encaisses"]) + " encaissés)")
    ligne_stat("Total de buts", total_buts)
    ligne_stat("Moyenne de buts par équipe", moyenne)
    ligne_stat("Matchs joués", total_matchs)
    ligne_stat("Vérification récursive (leader)", str(points_verifies) + " pts")
    print("+" + "-" * 33 + "+" + "-" * 29 + "+")

def tri(equipes):
    """
    Trie les équipes par points (décroissant), puis par différence de buts
    en cas d'égalité, avec un tri à bulles. Retourne une nouvelle liste.
    """
    liste = equipes[:]
    n = len(liste)
    for passage in range(n):
        for j in range(n - 1):
            gauche = liste[j]
            droite = liste[j + 1]
            cle_gauche = (gauche["points"], gauche["buts_marques"] - gauche["buts_encaisses"])
            cle_droite = (droite["points"], droite["buts_marques"] - droite["buts_encaisses"])
            if cle_gauche < cle_droite:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    return liste

def recherche_dichotomique(equipes_triees, nom_recherche):
    """
    Recherche une équipe par nom dans une liste triée par ordre alphabétique,
    en coupant la zone de recherche en deux à chaque étape.
    Affiche le nombre de comparaisons. Retourne la fiche, ou None.
    """
    debut = 0
    fin = len(equipes_triees) - 1
    comparaisons = 0
    while debut <= fin:
        milieu = (debut + fin) // 2
        nom_milieu = equipes_triees[milieu]["nom"]
        comparaisons = comparaisons + 1
        if nom_milieu == nom_recherche:
            print("Recherche dichotomique :", comparaisons, "comparaison(s)")
            return equipes_triees[milieu]
        elif nom_milieu < nom_recherche:
            debut = milieu + 1
        else:
            fin = milieu - 1
    print("Recherche dichotomique :", comparaisons, "comparaison(s)")
    return None

def comparer_recherches(equipes):
    """
    Cherche une équipe avec les deux méthodes et affiche
    le nombre de comparaisons de chacune.
    """
    nom = input("Nom de l'équipe : ")

    # Recherche linéaire : on compte les comparaisons une par une
    comparaisons_lineaire = 0
    for equipe in equipes:
        comparaisons_lineaire = comparaisons_lineaire + 1
        if equipe["nom"] == nom:
            break
    print("Recherche linéaire :", comparaisons_lineaire, "comparaison(s)")

    # Recherche dichotomique : la liste doit d'abord être triée par nom
    equipes_par_nom = sorted(equipes, key=lambda e: e["nom"])
    resultat = recherche_dichotomique(equipes_par_nom, nom)

    if resultat is None:
        print("Équipe introuvable")
    else:
        print("Équipe trouvée :", resultat["nom"])

def enregistrer_resultat(equipe1, equipe2, score1, score2):
    """
    Met à jour les fiches des deux équipes après un match,
    sans rien demander à l'utilisateur.
    """
    # Les buts, dans tous les cas
    equipe1["buts_marques"] = equipe1["buts_marques"] + score1
    equipe2["buts_marques"] = equipe2["buts_marques"] + score2
    equipe1["buts_encaisses"] = equipe1["buts_encaisses"] + score2
    equipe2["buts_encaisses"] = equipe2["buts_encaisses"] + score1

    # Victoire de l'équipe 1
    if score1 > score2:
        equipe1["victoires"] = equipe1["victoires"] + 1
        equipe1["points"] = equipe1["points"] + 3
        equipe2["defaites"] = equipe2["defaites"] + 1
    # Victoire de l'équipe 2
    elif score1 < score2:
        equipe2["victoires"] = equipe2["victoires"] + 1
        equipe2["points"] = equipe2["points"] + 3
        equipe1["defaites"] = equipe1["defaites"] + 1
    # Match nul
    else:
        equipe1["nuls"] = equipe1["nuls"] + 1
        equipe2["nuls"] = equipe2["nuls"] + 1
        equipe1["points"] = equipe1["points"] + 1
        equipe2["points"] = equipe2["points"] + 1


def simuler_championnat(equipes):
    """
    Joue automatiquement tous les matchs possibles avec des scores
    aléatoires, les affiche en direct, puis annonce le podium.
    """
    if len(equipes) < 2:
        print(ROUGE + "Il faut au moins 2 équipes pour lancer un championnat." + RESET)
        return

    matchs = generer_matchs(equipes)
    print()
    print(JAUNE + GRAS + "🏟️  COUP D'ENVOI DU CHAMPIONNAT : " + str(len(matchs)) + " matchs" + RESET)
    print()

    numero = 1
    for match in matchs:
        # On retrouve les deux fiches grâce à la recherche linéaire
        equipe1 = recherche_lineaire(equipes, match[0])
        equipe2 = recherche_lineaire(equipes, match[1])

        # Des scores au hasard entre 0 et 4
        score1 = random.randint(0, 4)
        score2 = random.randint(0, 4)

        # Un peu de suspense avant le score
        ecrire_lentement("Match " + str(numero) + " : " + equipe1["nom"] + " vs " + equipe2["nom"] + " ...", 0.02)
        time.sleep(0.4)
        print("   " + VERT + GRAS + str(score1) + " - " + str(score2) + RESET)

        enregistrer_resultat(equipe1, equipe2, score1, score2)
        numero = numero + 1

    # Le podium, avec ton tri à bulles
    classement = tri(equipes)
    medailles = ["🥇", "🥈", "🥉"]
    print()
    print(JAUNE + GRAS + "🏆 PODIUM 🏆" + RESET)
    for i in range(min(3, len(classement))):
        print(medailles[i], classement[i]["nom"], "-", classement[i]["points"], "pts")
    print()
    ecrire_lentement(CYAN + GRAS + "Champion : " + classement[0]["nom"] + " ! 🎉" + RESET, 0.06)