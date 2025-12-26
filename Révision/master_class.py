import os
import sys
import json
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, ttk, scrolledtext
import threading
import webbrowser

# Nom du fichier de configuration pour sauvegarder les paramètres
CONFIG_FILE = "master_class_config.json"

class MasterClassApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎓 Master Class - Gestionnaire de Révisions")
        self.root.geometry("800x650")
        self.root.configure(bg="#f1f5f9")
        self.root.minsize(700, 600)

        # Variables d'état
        self.api_key = tk.StringVar(value=self.load_config().get("api_key", ""))
        self.source_dir = tk.StringVar(value=os.getcwd())
        self.dest_dir = tk.StringVar(value=os.path.join(os.getcwd(), "Questions"))
        self.is_running = False

        self.setup_styles()
        self.setup_ui()

    def load_config(self):
        """Charge la configuration depuis le fichier JSON."""
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, "r") as f:
                    return json.load(f)
            except:
                return {}
        return {}

    def save_config(self):
        """Sauvegarde la configuration actuelle."""
        config = {
            "api_key": self.api_key.get(),
            "source_dir": self.source_dir.get(),
            "dest_dir": self.dest_dir.get()
        }
        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f)

    def setup_styles(self):
        """Configure les styles TTK pour une interface plus moderne."""
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TFrame", background="#f1f5f9")
        style.configure("TLabel", background="#f1f5f9", font=("Segoe UI", 10))
        style.configure("Header.TLabel", font=("Segoe UI", 18, "bold"), foreground="#1e293b")
        style.configure("Action.TButton", font=("Segoe UI", 10, "bold"), padding=10)

    def setup_ui(self):
        # --- HEADER ---
        header_frame = ttk.Frame(self.root, padding=20)
        header_frame.pack(fill="x")
        
        ttk.Label(header_frame, text="🎓 Master Class Pro", style="Header.TLabel").pack(side="left")
        
        # --- PANNEAU DE CONFIGURATION ---
        config_frame = ttk.LabelFrame(self.root, text=" Configuration ", padding=15)
        config_frame.pack(fill="x", padx=20, pady=10)

        # Clé API
        ttk.Label(config_frame, text="Clé Gemini API :").grid(row=0, column=0, sticky="w", pady=5)
        api_entry = ttk.Entry(config_frame, textvariable=self.api_key, show="*", width=50)
        api_entry.grid(row=0, column=1, padx=10, sticky="we")
        ttk.Button(config_frame, text="Sauvegarder", command=self.save_config).grid(row=0, column=2)

        # Dossiers
        ttk.Label(config_frame, text="Dossier Source (PDF) :").grid(row=1, column=0, sticky="w", pady=5)
        ttk.Entry(config_frame, textvariable=self.source_dir).grid(row=1, column=1, padx=10, sticky="we")
        ttk.Button(config_frame, text="Parcourir", command=lambda: self.browse_dir(self.source_dir)).grid(row=1, column=2)

        ttk.Label(config_frame, text="Dossier Dest (JSON) :").grid(row=2, column=0, sticky="w", pady=5)
        ttk.Entry(config_frame, textvariable=self.dest_dir).grid(row=2, column=1, padx=10, sticky="we")
        ttk.Button(config_frame, text="Parcourir", command=lambda: self.browse_dir(self.dest_dir)).grid(row=2, column=2)
        
        config_frame.columnconfigure(1, weight=1)

        # --- ACTIONS ---
        actions_frame = ttk.Frame(self.root, padding=10)
        actions_frame.pack(fill="x", padx=20)

        self.btn_review = ttk.Button(
            actions_frame, text="📖 Lancer le Quiz (Navigateur)", 
            command=self.open_quiz, style="Action.TButton"
        )
        self.btn_review.pack(side="left", expand=True, fill="x", padx=5)

        self.btn_convert = ttk.Button(
            actions_frame, text="🧪 Démarrer la Conversion", 
            command=self.start_conversion, style="Action.TButton"
        )
        self.btn_convert.pack(side="left", expand=True, fill="x", padx=5)

        # --- PROGRESSION ET LOGS ---
        log_frame = ttk.LabelFrame(self.root, text=" Console de Sortie ", padding=10)
        log_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.progress = ttk.Progressbar(log_frame, orient="horizontal", mode="determinate")
        self.progress.pack(fill="x", pady=(0, 10))

        self.log_area = scrolledtext.ScrolledText(
            log_frame, height=12, font=("Consolas", 9), bg="#1e293b", fg="#f8fafc"
        )
        self.log_area.pack(fill="both", expand=True)
        self.log_area.insert("end", "[Système] Prêt.\n")
        self.log_area.configure(state="disabled")

    def browse_dir(self, var):
        directory = filedialog.askdirectory()
        if directory:
            var.set(directory)

    def log(self, message):
        """Ajoute un message à la console de log."""
        self.log_area.configure(state="normal")
        self.log_area.insert("end", f"{message}\n")
        self.log_area.see("end")
        self.log_area.configure(state="disabled")

    def open_quiz(self):
        html_file = os.path.abspath("quizz.html")
        if os.path.exists(html_file):
            self.log(f"[Info] Ouverture de {html_file}...")
            webbrowser.open(f"file://{html_file}")
        else:
            messagebox.showerror("Erreur", "Le fichier quizz.html est introuvable.")

    def start_conversion(self):
        if self.is_running:
            return
        
        # Vérifications préalables
        if not self.api_key.get():
            messagebox.showwarning("Clé Manquante", "Veuillez entrer votre clé API Gemini.")
            return
        
        if not os.path.exists("pdf_to_json.py"):
            messagebox.showerror("Script Manquant", "pdf_to_json.py est introuvable dans ce dossier.")
            return

        source = self.source_dir.get()
        if not os.path.exists(source):
            messagebox.showerror("Dossier Invalide", "Le dossier source n'existe pas.")
            return

        self.is_running = True
        self.btn_convert.config(state="disabled")
        self.log_area.configure(state="normal")
        self.log_area.delete("1.0", "end")
        self.log_area.configure(state="disabled")
        self.log("--- DÉBUT DU TRAITEMENT ---")
        
        threading.Thread(target=self.run_conversion_process, daemon=True).start()

    def run_conversion_process(self):
        try:
            source = self.source_dir.get()
            dest = self.dest_dir.get()
            os.makedirs(dest, exist_ok=True)

            # Liste des fichiers PDF
            pdf_files = [f for f in os.listdir(source) if f.lower().endswith(".pdf")]
            
            if not pdf_files:
                self.log("[Info] Aucun fichier PDF trouvé.")
                self.root.after(0, self.finish_conversion)
                return

            total = len(pdf_files)
            # On définit l'environnement pour le script enfant
            env = os.environ.copy()
            env["GEMINI_API_KEY"] = self.api_key.get()

            for i, filename in enumerate(pdf_files):
                self.root.after(0, lambda v=int(((i)/total)*100): self.progress.config(value=v))
                
                input_path = os.path.join(source, filename)
                output_path = os.path.join(dest, filename.replace(".pdf", ".json"))

                # Si déjà converti
                if os.path.exists(output_path):
                    self.log(f"[Ignoré] {filename} (Déjà présent)")
                    continue

                self.log(f"[Traitement] {filename}...")
                
                # Exécution et capture de la sortie en temps réel
                process = subprocess.Popen(
                    [sys.executable, "pdf_to_json.py", input_path, output_path],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    env=env
                )

                for line in process.stdout:
                    self.log(f"  > {line.strip()}")
                
                process.wait()
                if process.returncode == 0:
                    self.log(f"[Succès] {filename} converti.")
                else:
                    self.log(f"[Erreur] Échec pour {filename} (Code: {process.returncode})")

            self.root.after(0, lambda: self.progress.config(value=100))
            self.log("--- TRAITEMENT TERMINÉ ---")
            self.root.after(0, lambda: messagebox.showinfo("Succès", "La conversion est terminée !"))

        except Exception as e:
            self.log(f"[CRITIQUE] Une erreur est survenue : {str(e)}")
        
        self.root.after(0, self.finish_conversion)

    def finish_conversion(self):
        self.is_running = False
        self.btn_convert.config(state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    app = MasterClassApp(root)
    root.mainloop()