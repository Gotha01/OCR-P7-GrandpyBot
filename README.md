# **GrandPy Bot**


[![](https://img.shields.io/badge/Version-1.0.3-blue)]()

[![](https://img.shields.io/badge/Dev__Languages-Python/HTML/JS-blue)]()
[![](https://img.shields.io/badge/Last_Commit-v1.0.3-blue)]()
[![](https://img.shields.io/badge/Tests-5%20passed%2C%200%20failure-green)]()

[![](https://img.shields.io/badge/Script__Languages-English-red)]()
[![](https://img.shields.io/badge/User__App__Language-French-red)]()
# **Code établi selon le cahier des charges suivant:**

## *Fonctionnalités*

    1/ Interactions en AJAX : l'utilisateur envoie sa question en appuyant sur entrée et la réponse
        s'affiche directement dans l'écran, sans recharger la page.
    2/ Vous utiliserez l'API de Google Maps et celle de Media Wiki.
    3/ Rien n'est sauvegardé. Si l'utilisateur charge de nouveau la page,
        tout l'historique est perdu.
    4/ Vous pouvez vous amuser à inventer plusieurs réponses différentes
        de la part de GrandPy mais ce n'est pas une obligation. Amusez-vous!

## *Parcours utilisateur*

    L'utilisateur ouvre son navigateur et entre l'URL que vous lui avez fournie.
    Il arrive devant une page contenant les éléments suivants :

        -Header : logo et phrase d'accroche
        
        -Zone centrale : zone vide (qui servira à afficher le dialogue) et champ de formulaire
            pour envoyer une question.

        -Footer : votre prénom & nom, lien vers votre repository Github et
            autres réseaux sociaux si vous en avez
    
    L'utilisateur tape "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
        dans le champ de formulaire puis appuie sur la touche Entrée. Le message s'affiche dans
        la zone du dessus qui affiche tous les messages échangés.
        Une icône tourne pour indiquer que GrandPy est en train de réfléchir.

    Puis un nouveau message apparaît : "Bien sûr mon poussin ! La voici : 7 cité Paradis, 75010 Paris."
    En-dessous, une carte Google Maps apparaît également avec un marqueur indiquant l'adresse demandée.

    GrandPy envoie un nouveau message : "Mais t'ai-je déjà raconté l'histoire 
    de ce quartier qui m'a vu en culottes courtes ? La cité Paradis est une voie
    publique située dans le 10e arrondissement de Paris. Elle est en forme de té,
    une branche débouche au 43 rue de Paradis, la deuxième au 57 rue d'Hauteville
    et la troisième en impasse. [En savoir plus sur Wikipedia]"

# **Lancer localement**

## *1/ Installer le pré-requis*
#

### Cloner le projet

```bash
  git clone https://github.com/Gotha01/OCR-Project7.git
```

### Allez dans le répertoire du projet

```bash
  $ cd OCR-Project7
```

### Créer un nouvel environnement virtuel et l'atteindre

```bash
  $ python -m venv new_env
```
```
  $ source new_env/Scripts/activate
```

### Installer les dépendances

```bash
  $ pip install -r requirements.txt
```

## *2/ Lancer l'application*
#

### **Démarrer le serveur**

```bash
  $ python run.py
```

### **Accéder au site**

Utiliser dans un navigateur web l'URL obtenu lors du lancée du serveur à la ligne:
```
  * Running on http://...:5400/
```
#
**`! Attention !`**

*Vouloir copier l'URL en utilisant
le raccourci Ctrl+c dans votre cmd entraine l'arrêt du serveur.*
#

# **Exécution des tests**
Pour lancer les tests, exécutez la commande suivante à la racine du projet:
```bash
  pytest -v
```


# **Auteur**

[@FaureQuentin](https://www.github.com/Gotha01) pour la formation "Développeur d'application Python" d'[OpenClassRooms.](https://openclassrooms.com/fr/)
