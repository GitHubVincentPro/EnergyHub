# Installation

## Pre-requis

- Python 3.6 ou superieur
- Une base de donnees PostgreSQL

## Clonez le depot

```
git clone https://github.com/energyhub/energyhub
```

## Creez un environnement virtuel Python

```
python3 -m venv venv
source venv/bin/activate
```

## Installez les dependances

```
pip install -r requirements.txt
```

## Configurer la base de donnees

Creer la base, modifier les variables dans .env

## Executez les migrations

```
python manage.py migrate
```

## Lancer l'application

```
python manage.py runserver
```

L'API sera disponible a l'adresse http://localhost:8000

## Tests

```
python manage.py test
```

## Deploiement