# 🎓 Master Class

**Master Class** est un outil intelligent de révision conçu pour transformer automatiquement des cours de mathématiques (**PDF**) en **quiz interactifs**.

En s'appuyant sur l'intelligence artificielle de **Google Gemini**, l'application extrait avec précision les **théorèmes**, **propositions** et **lemmes**. Elle génère ensuite des questions stimulantes basées sur les **hypothèses nécessaires** et conçoit des **distracteurs** (pièges) pertinents pour valider la compréhension profonde du cours.

## 🚀 Fonctionnalités Clés

* **Conversion IA :** Analyse avancée des fichiers PDF par **Gemini AI** pour extraire la structure logique et mathématique des cours.

* **Génération de Questions :** Création automatique de tests portant sur la validité des hypothèses mathématiques.

* **Interface Desktop :** Une application de bureau **intuitive** pour gérer facilement vos clés API et l'organisation de vos dossiers.

* **Quiz Interactif :** Une interface web **élégante** et moderne pour s'entraîner, incluant un suivi de progression.

* **Logs en Temps Réel :** Visualisation détaillée du processus de conversion (Upload, Analyse, Sauvegarde) directement dans l'interface.

## 🛠️ Structure du Projet

* **`master_class.py` :** Le "cerveau" de l'application de bureau (Interface Tkinter).

* **`pdf_to_json.py` :** Le script de traitement qui assure la communication avec l'API Gemini.

* **`quizz.html` :** L'interface utilisateur du quiz, dynamique et responsive.

* **`Questions/` :** Dossier de stockage des fichiers **JSON** générés.

> **Remarques :**
> Cette application utilise **Gemini**, mais le fichier `pdf_to_json.py` est conçu pour être facilement adaptable à d'autres **LLMs** ou à des **IA locales**.
> Des questions sont déjà incluses pour les cours de **Prépa**, **CentraleSupélec** et le **Magistère d'Orsay**.

## 📦 Installation & Configuration

### 1. Prérequis

* **Python 3.8** ou supérieur.

* Une **clé API Google Gemini** (obtenue sur Google AI Studio).

### 2. Installation des dépendances

Ouvrez un terminal dans le dossier du projet et exécutez :

```ip install -r requirements.txt

**`
# 📋 Utilisationon```# 📋 Utilisationon`# 📋 Utilisationon`# 📋 Utilisationon1. **Lancez l'applicztion :** Exécutez `pytpo2. **Configurez votre Clé API :** Saisissez votre clé Gemini dans le champ dédié et cliquez s3. **Sélectionnez vos PDF :** Choisissez le dossier contenant vos cours de mathématiques.4. **Lancez la conversion :** L'IA générera les fichiers JSON dans le dossier `Questions`.

5. **Révisez :** Cliquez sur **"Lancer le Quiz"** pour commencer vos révisions dans votre navigateur.

## 🧪 Détails Techniques

L'application repose sur un ensemble de technologies modernes :

* **Python :** Pour le moteur de traitement logique et l'interface native.

* **Google Generative AI :** Modèle `gemini-1.5-flash` pour l'analyse sémantique et mathématique.

* **HTML5 / Tailwind CSS :** Pour une interface de quiz fluide et esthétique.

* **MathJax :** Pour un rendu parfait des formules mathématiques en $\LaTeX$.

*Développé pour faciliter l'apprentissage et la maîtrise des mathématiques de haut niveau.*
