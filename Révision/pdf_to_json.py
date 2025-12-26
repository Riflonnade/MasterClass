import sys
import os
import json
import google.generativeai as genai

# Configuration du modèle
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("Erreur: Clé API manquante dans le script Python.")
    sys.exit(1)

genai.configure(api_key=api_key)

# Modèle conservé selon votre demande
model = genai.GenerativeModel('gemini-3-flash-preview')

def process_pdf(input_path, output_path):
    try:
        # 1. Upload du fichier vers Gemini
        print(f"   ... Upload de {os.path.basename(input_path)} vers Gemini...")
        sample_file = genai.upload_file(path=input_path, display_name="Cours PDF")

        # 2. Le Prompt (Utilisation de r""" pour protéger le texte source)
        prompt = r"""
        Agis comme un professeur de mathématiques. Analyse le

cours ci-dessous. Extrais tout les théorèmes, propositions et lemmes. Pour chacun, identifie les hypothèses nécessaires (strictes)

 et invente des pièges (hypothèses plausibles mais fausses ou inutiles) ou alors selon une hypothèses identifie les propriétés qui en découle et invente des pièges si il y a plus de propositions qui en decoule que d'hypothèses ou à partir d'une définition donne l'ensemble de ses caractérisations 

 

 Formate la réponse uniquement en JSON suivant cette structure, sans texte avant ni après :"{ 

     "title": "Titre du Cours", 

     "color": "blue",  

     "questions": [ 

       { 

         "name": "Nom du Théorème", 

         "statement": "Énoncé mathématique en LaTeX (ex: $a^2=b$)", 

         "correct": ["Hypothèse vraie 1", "Hypothèse vraie 2"], 

         "distractors": ["Hypothèse fausse 1", "Hypothèse fausse 2"] 

       } 

     ] 

 }  
        """

        # 3. Génération
        print("   ... Génération de l'analyse...")
        response = model.generate_content([sample_file, prompt])

        # 4. Nettoyage de la réponse
        text_response = response.text.strip()
        if text_response.startswith("```json"):
            text_response = text_response[7:]
        if text_response.endswith("```"):
            text_response = text_response[:-3]
        
        # --- PROTECTION CONTRE LES BACKSLASHES LATEX ---
        # Si Gemini renvoie \int au lieu de \\int, json.loads va planter.
        # Cette ligne remplace les backslashes simples par des doubles pour le JSON.
        text_response = text_response.replace('\\', '\\\\')
        # On remet les doubles backslashes qui auraient pu devenir quadruples
        text_response = text_response.replace('\\\\\\\\', '\\\\')

        # 5. Parsing et Sauvegarde
        json_content = json.loads(text_response)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(json_content, f, ensure_ascii=False, indent=4)

        # Nettoyage
        sample_file.delete()
        
    except Exception as e:
        print(f"   Erreur Python : {e}")
        # Note : On ne fait pas sys.exit(1) ici pour que le bash continue sur le fichier suivant
        return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(1)
        
    input_pdf = sys.argv[1]
    output_json = sys.argv[2]
    
    process_pdf(input_pdf, output_json)