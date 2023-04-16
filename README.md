# importRepo
Scripts pour rechercher des répertoires sur github

## Description des scripts

- scriptFind.py: script de base qui cherche des répertoires de projets typescripts qui ont au minimum 500 étoiles
- scriptFindBugLabel.py: script qui cherche des répertoires typescript avec plus de 500 étoiles, mais qui vérifie également si le répertoire utilise le label "bug"
- scriptFindKeywordCommit.py: script qui cherche des répertoire typescript avec plus de 500 étoiles, mais qui permet de vérifier si une certaine nomenclature est utilisée dans les titres de commit ou les messages de commit

## Utilisation

- scriptFind.py: python scriptFind number_of_repo Outputfile.json 
  - number_of_repo => maximum 30
- scriptFindBugLabel.py: python scriptFindBugLabel.py Outputfile.json
- scriptFindKeywordCommit.py: python scriptFindKeywordCommit.py Outputfile.json keyword minOccurrence

## Dépendances
### GitHub Token

- Pour utiliser ces scripts un fichier token.env contenant un token d'accès github valide doit être présent
- Il doit prendre la Forme:GITHUB_TOKEN=<github_access_token>


### Dépendances Python

- json
- dotenv
- os
- requests
- sys
