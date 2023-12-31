🔋 Notre mission: Optimiser la gestion de l'énergie grâce à l'IA

EnergyHub a pour objectif de faciliter la transition énergétique en rendant les réseaux électriques plus flexibles et résilients.

🌞 Notre solution permet d'intégrer massivement les énergies renouvelables intermittentes comme le solaire et l'éolien.

🔮 Nos algorithmes d'apprentissage automatique analysent en temps réel des données météo, de consommation et de production sur des zones géographiques.

🔮 Cela permet de prédire avec précision la production et la demande énergétique à court et moyen terme, même avec des conditions changeantes.

🔋 Grâce à ces prévisions fines, notre système décide de manière autonome comment stocker l'énergie renouvelable produite dans des batteries ou autres moyens.

⛽ Il peut aussi analyser les cours de l'électricité sur le marché en temps réel et décider de vendre l'énergie lorsque les prix sont élevés.

💰 L'objectif final est de générer des revenus en optimisant le stockage et en lissant les pics de production/demande. Cela réduit aussi les coûts des infrastructures de réseau.

🤝 EnergyHub a déjà fait ses preuves sur plusieurs projets tests, avec des économies de +15% sur les coûts énergétiques.

👨‍👩‍👧‍👦 Notre solution rend les territoires plus résilients face aux fluctuations des marchés et aux aléas climatiques.

🔑 Rejoignez notre communauté et accédez gratuitement à notre code source pour accélérer la transition énergétique partout dans le monde!


GitHub EnergyHub:

### Dossiers et fichiers

- `data/`: Contient les jeux de données d'entraînement et de tests
- `models/`: Code sources des modèles de prévision et de gestion du stockage
- `notebooks/`: Cahiers Jupyter pour l'exploration de données et le développement
- `app/`: Code Flask pour l'API et le dashbord web
- `tests/`: Scénarios et tests unitaires / d'intégration
- `docs/`: Documentation utilisateur et d'installation
- `config/`: Exemples de fichiers de configuration

### Gestion de versions

- `CHANGELOG.md`: Liste des modifications pour chaque version
- `version.py`: Définit le numéro de version du package

### Démarrage rapide

- `README.md`: Présentation du projet et instructions d'installation
- `requirements.txt`: Dépendances Python nécessaires
- `Makefile`: Raccourcis pour les tâches communes (test, build, deploy...)

### Qualité

- `.github/workflows/ci.yml`: Définit le build continu
- `.github/linters`: Règles de qualité du code (format, pep8, mypy...)
- `.github/issue_templates`: Modèles standard pour issues/bugs

### Intégration continue

- Mettre en place des tests automatisés GitHub Actions ou Travis pour vérifier le code à chaque push

- Evaluer la qualité du code, la documentation et respect des bonnes pratiques

- Déployer automatiquement de nouvelles versions si les tests passent

### Documentation

- Compléter la doc d'installation (pré-requis, install du projet...)

- Expliquer en détail chaque composant du système (data, modèles, API...)

- Fournir des tutoriels d'utilisation (prévisions, gestion du stockage...)

- Générer le site de doc à partir du code avec Sphinx

### Ergonomie

- Développer une interface web intuitive avec Dash/Flask

- Permettre la configuration simplifiée via fichier YAML

- Intégrer une authentification/autorisation des utilisateurs

- Internationaliser l'interface (traductions multiples)

### Modèles avancés

- Expérimenter des RNN/CNN pour la prédiction court-terme

- Entrainer un Q-learning pour l'optimisation du stockage

- Utiliser l'apprentissage par renforcement pour l'équilibrage offre/demande

- Publier les résultats dans des conférences/journaux

- ### Modèles de prévision

- Implémenter un modèle ARIMA en Python pour prédire la consommation
- Entraîner un RNN sur Keras pour la production solaire à court-terme
- Comparer les performances de différents algorithmes (SVM, Tree, etc.)

### Stockage de l'énergie

- Modéliser les capacités de stockage disponibles (batteries, véhicules électriques)
- Développer un Q-Learning pour optimiser les stratégies de charge/décharge
- Intégrer la valorisation des flexibilités auprès des gestionnaires de réseaux

### Orchestration des flux

- Concevoir l'API RESTful du système de gestion de l'énergie avec Flask
- Développer le système multi-agents pour la négociation entre prosumer
- Simuler le fonctionnement sur differents scénarios

### Interfaces utilisateur

- Construire le dashboard métier avec Plotly/Dash pour la visualisation
- Ajouter des modes d'analyse des données et de simulation
- Déployer l'interface sous forme d'application web/mobile

### Ingénierie de déploiement

- Appliquer les principes du DevOps avec des outils comme Docker
- Déployer automatiquement de nouvelles versions du système
- Prévoir des capacités d'évolutivité et de haute disponibilité

### Rajouter des modèles de prévision

- Créer un nouveau notebook dans le dossier notebooks pour entraîner un modèle LSTM sur les données solaires
- Ajouter le code du modèle dans models/forecasting_models.py
- Documenter la méthode dans docs/models.md

### Améliorer la gestion du stockage

- Implémenter un algorithme Q-Learning dans storage/battery_manager.py
- Simuler son fonctionnement dans notebooks/storage_simulation.ipynb
- Comparer les performances avec l'algorithme existant

### Développer l'API REST

- Concevoir les spécifications OpenAPI dans docs/api_specs.yml
- Créer les routes Flask dans app/api.py pour exposer les prévisions et le stockage
- Écrire les tests d'intégration API dans tests/api_test.py

### Mettre en place le pipeline CI/CD

- Configurer GitHub Actions dans .github/workflows/ci.yml pour les tests automatiques
- Déployer automatiquement une version de démo sur Heroku à chaque merge
- Documenter le workflow de développement dans CONTRIBUTING.md

### Publier la documentation

- Générer le site de documentation avec Sphinx
- Héberger le site sur GitHub Pages
- Promouvoir la documentation sur le référentiel

### DATA

Pour le dossier data, voici quelques éléments de données clés à récolter et à y stocker:

- Données météo historiques (ensoleillement, température, vent...) au format CSV par exemple. Cela servira à l'entraînement des modèles de prévision.

- Courbes de charge réelles de foyers/bâtiments sur différentes périodes (jour, semaine, mois). Utile pour prédire la consommation.

- Production d'énergie renouvelable d'installations solaires et éoliennes existantes.

- Informations techniques sur les capacités et performance des batteries et véhicules électriques utilisables pour le stockage.

- Données open data des gestionnaires de réseaux sur l'offre et la demande énergétique globale.

- Prix horaires/journaliers de gros du marché de l'électricité.

Le but est de disposer rapidement de jeux de données réelles ou simulées pour tester et valider les premiers algorithmes. N'hésite pas à me demander comment formater, nettoyer ou enrichir ces données.

Ensuite il faudra penser à organiser ce dossier data, par exemple avec des sous-dossiers par type/source de données ou par zone géographique.


### DEV

# CONFIG

On pourrait aussi:

- Ajouter un fichier de variables d'environnement .env
- Créer une classe de configuration Config
- Charger lesconfigs à partir d'un fichier YAML
- Créer des profiles de config (dev, test, prod)


### DEV 1.1

- Compléter les jeux de données météorologiques, de charges et de production d'énergie renouvelable. C'est important pour bien entraîner les algorithmes de prédiction.

- Développer davantage de modèles prédictifs en testant de nouveaux algorithmes d'apprentissage comme les RNN ou CNN. Cela permettra d'affiner les prévisions.

- Modéliser plus en détails les flexibilités énergétiques à pilotter comme le stockage ou le load shifting.

- Concevoir une API RESTful complète avec Flask pour interconnecter facilement le système aux autres applications.

- Automatiser les tests unitaires et d'intégration continue, par exemple avec GitHub Actions, pour s'assurer de la qualité à chaque mise à jour.

- Finaliser le développement du dashboard web intuitif pour visualiser et simuler les scénarios de gestion de l'énergie.

- Publier des articles scientifiques pour faire connaître le projet et recueillir les retours de la communauté de recherche.

- Appliquer des techniques d'intelligence artificielle plus avancées comme le deep learning ou le reinforcement learning.

### DEV 1.2

- Ajouter de nouvelles sources de données réelles plus complètes et à jour, notamment des données météorologiques précises et des courbes de charges de consommateurs/producteurs.

* Implémenter de nouveaux algorithmes d'apprentissage automatique comme des RNN ou CNN dans le dossier "models" pour affiner les prévisions court-terme.

- Développer dans le dossier "app" de nouvelles routes API et fonctionnalités comme la gestion automatisée du stockage grâce à des algorithmes de reinforcement learning.

- Compléter les notebooks de test et formation des modèles, en implémentant notamment la validation croisée.

- Mettre en place des pipelines CI/CD automatisés dans GitHub Actions pour tester et déployer les nouvelles fonctionnalités de manière continue.

- Finaliser la documentation technique dans le dossier "docs" et déployer un site de documentation utilisateur.

- Créer une interface web intuitive avec Flask/Plotly pour visualiser les prévisions et commander le stockage.

- Simuler sur des scénarios réels le fonctionnement global du système de gestion énergétique.

- Publier les résultats scientifiques dans des conférences pour faire progresser la recherche sur le sujet.

### DEV 1.3

1. Compléter les jeux de données dans le dossier data/
- Ajouter des données météo, de consommation et de production réelles
- Formater les données pour l'entraînement des modèles

2. Développer les modèles de prévision
- Implémenter un premier modèle de prévision court-terme dans models/forecasting_models.py
- Entraîner et valider le modèle dans des notebooks Jupyter

3. Implémenter la gestion basique du stockage
- Créer un algorithme simple de charge/décharge dans models/storage_manager.py
- Simuler son fonctionnement dans des notebooks

4. Configurer l'API REST avec Flask
- Définir les spécifications OpenAPI dans docs/api_specs.yml
- Implémenter les routes principales dans app/api.py

5. Mettre en place l'application Flask
- Créer le point d'entrée dans app/run.py
- Ajouter des routes et templates de base dans app/

6. Automatiser les tests unitaires
- Écrire les premiers tests dans tests/test_models.py
- Configurer Github Actions pour les exécuter

7. Déployer la version bêta
- Déployer l'application sur Serveur
- Tester les fonctionnalités de base

8. Documenter l'installation
- Expliquer dans docs/comment installer et lancer le projet

9. Récolter un premier retour utilisateur
- Faire tester la bêta et corriger les bugs trouvés



#### Checklist version bêta 


## Données

- [ ] Les jeux de données de base sont complétés et propres
- [ ] Ils couvrent les besoins minimum des modèles

## Modèles

- [ ] Les algorithmes de prévision sont implémentés et testés
- [ ] Le module de gestion de stockage fonctionne sur des cas simples

## API

- [ ] Les spécifications OpenAPI sont définies
- [ ] Les routes de base répondent sans erreur

## Interface

- [ ] Un dashboard sommaire est fonctionnel
- [ ] Il permet de piloter le stockage

## Tests

- [ ] Il existe des tests unitaires de couverture minimum
- [ ] Les tests d'intégration API passent

## Déploiement

- [ ] Le package s'installe proprement
- [ ] Une démo fonctionne sur un Serveur linux Debian

## Documentation

- [ ] Le README est complet et le fonctionnement expliqué
- [ ] La documentation technique est en cours

## Qualité

- [ ] Le code respecte les bonnes pratiques
- [ ] Une analyse de sécurité sommaire a été faite



#######################################################################################



lancer le projet EnergyHub sur un simple serveur Linux Debian. Voici les étapes à suivre:


#### Lancer le Projet sur un serveur linux Debian

1. Installer Python et les dépendances nécessaires sur le serveur:

```
sudo apt update
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib
```

2. Cloner le dépôt Git du projet:

```
git clone https://github.com/GitHubVincentPro/EnergyHub
```

3. Installer les dépendances Python avec pip:

```
pip3 install -r requirements.txt
```

4. Créer un utilisateur dédié pour le serveur Flask:

```
sudo adduser energyhub
```

5. Démarrer l'application Flask:

```
sudo su - energyhub
export FLASK_APP=run.py
flask run --host=0.0.0.0
```

6. Ouvrir le firewall pour exposer le port 5000:

```
sudo ufw allow 5000
```

7. L'API sera alors accessible depuis l'IP publique du serveur au port 5000.

### Copyright (c) 2023 VincentPro

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Cette licence MIT est l'une des plus permissives et simples à comprendre. Elle permet de garantir la liberté d'utilisation, de modification et de redistribution du code. N'hésitez pas à l'adapter ou choisir une autre licence Open Source si vous le souhaitez (LGPL, Apache...). L'essentiel est de clarifier les droits pour tous les contributeurs. N'hésitez pas si vous avez d'autres questions!
