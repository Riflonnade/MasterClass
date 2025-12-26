🎓 Master Class

Master Class est un outil intelligent de révision conçu pour transformer automatiquement des cours de mathématiques (PDF) en quiz interactifs. En utilisant l'intelligence artificielle de Google Gemini, l'application extrait les théorèmes, lemmes et définitions pour générer des questions basées sur les hypothèses nécessaires et des distracteurs (pièges).

🚀 Fonctionnalités

Conversion IA : Analyse de fichiers PDF par Gemini AI pour extraire la structure logique des cours.

Génération de Questions : Création automatique de questions sur les hypothèses mathématiques.

Interface Desktop : Une application de bureau intuitive pour gérer vos clés API et vos dossiers.

Quiz Interactif : Une interface web moderne et élégante pour s'entraîner et qui garde la trace de votre progression.

Logs en Temps Réel : Suivi détaillé du processus de conversion directement dans l'application.

🛠️ Structure du Projet

master_class.py : Le cerveau de l'application de bureau.

pdf_to_json.py : Le script de traitement qui communique avec l'API Gemini.

quizz.html : L'interface de quiz dynamique.

Questions/ : Dossier contenant les fichiers JSON générés.

--- Remarques ---

Cette application utilise Gemini mais quelques petites manipulations du fichier pdf_to_json permettent de l'adapter à n'importe quelle API d'autres LLMs ou même à des IA locales.
Des questions déjà préparées sur mes cours en Prepa, à CentraleSupélec et au Magistère d'Orsay sont disponibles dans le dossier Questions.

📦 Installation

1. Prérequis

Python 3.8 ou supérieur.

Une clé API Google Gemini

2. Installation des dépendances

Ouvrez un terminal dans le dossier du projet et exécutez :

pip install -r requirements.txt

--- Bibliothèques externes ---

google-generativeai

--- Note sur les autres imports ---

os, sys, json, subprocess, threading, webbrowser : Déjà inclus dans Python

tkinter : Inclus par défaut sur Windows/Mac.

(Sur Linux, peut nécessiter : sudo apt install python3-tk)


📋 Utilisation

Lancez l'application :

python master_class.py (ou python3 master_class.py)


Configurez votre Clé API Gemini dans le champ prévu à cet effet et cliquez sur "Sauvegarder".

Sélectionnez votre dossier contenant les cours PDF.

Cliquez sur "Démarrer la Conversion". L'IA va générer les fichiers JSON dans le dossier Questions.

Une fois terminé, cliquez sur "Lancer le Quiz" pour commencer vos révisions dans votre navigateur.

🧪 Détails Techniques

L'application utilise :

Python : Pour le moteur de traitement et l'interface desktop.

Google Generative AI : Modèle gemini-3-flash-preview pour l'analyse sémantique des mathématiques.

HTML5/Tailwind CSS : Pour l'interface de quiz.

MathJax : Pour l'affichage parfait des formules mathématiques $\LaTeX$.

Développé pour faciliter l'apprentissage des mathématiques de haut niveau.
