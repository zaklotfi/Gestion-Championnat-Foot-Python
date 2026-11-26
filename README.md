# ⚽ Gestionnaire de tournoi

Projet Python · **Zakaria Lotfi** · B3 Data et IA

### 🎬 [Voir la présentation en ligne](https://zaklotfi.github.io/Projet_python/presentation.html)

La présentation est interactive : flèches du clavier pour naviguer, touche F pour le plein écran.

Un programme en ligne de commande pour gérer un championnat complet : inscrire des équipes, saisir des matchs, afficher le classement et les statistiques, et même simuler tout un championnat automatiquement.

## Lancer le programme

```bash
python3 main.py
```

Aucune installation nécessaire : le projet utilise uniquement la bibliothèque standard de Python (`time`, `os`, `random`).

## Organisation

| Fichier | Rôle |
| --- | --- |
| `main.py` | Le menu interactif : affiche les options, lit le choix et appelle la bonne fonction |
| `functions.py` | Toutes les fonctions du programme |
| `presentation.html` | La présentation du projet, avec ses animations ([voir en ligne](https://zaklotfi.github.io/Projet_python/presentation.html)) |

## Fonctionnalités

**Obligatoires**
1. Ajouter une équipe (une seule, ou plusieurs d'un coup séparées par des virgules), sans doublon
2. Afficher toutes les équipes dans un tableau aligné
3. Saisir le résultat d'un match (victoire, nul ou défaite)
4. Rechercher une équipe (recherche linéaire)
5. Afficher le classement avec `sorted()` : par points, puis par différence de buts
6. Menu interactif

**Bonus**
- Tri manuel : tri à bulles, sans `sorted()`
- Statistiques : meilleure attaque, meilleure défense, moyenne de buts, matchs joués
- Recherche dichotomique, avec comparaison du nombre de comparaisons face à la recherche linéaire
- Génération de tous les matchs possibles, sans doublon
- Fonction récursive de calcul des points

**En plus du sujet**
- Écran d'accueil animé et couleurs dans le terminal
- Simulation automatique de tout un championnat, avec podium

## Exemple d'utilisation

1. Option `1`, puis `2`, puis taper : `Paris, Lyon, Marseille, Nice`
2. Option `11` : le championnat se joue tout seul jusqu'au champion
3. Option `5` : le classement final
