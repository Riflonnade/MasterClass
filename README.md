# 🎓 Master Class

**Master Class** is an intelligent revision tool designed to automatically transform mathematics courses (**PDF**) into **interactive quizzes**.

By leveraging **Google Gemini** artificial intelligence, the application accurately extracts **theorems**, **propositions**, and **lemmas**. It then generates stimulating questions based on **necessary hypotheses** and designs relevant **distractors** (traps) to validate deep understanding of the course.

## 🚀 Key Features

* **AI Conversion:** Advanced analysis of PDF files by **Gemini AI** to extract the logical and mathematical structure of courses.

* **Question Generation:** Automatic creation of tests focusing on the validity of mathematical hypotheses.

* **Desktop Interface:** An **intuitive** desktop application to easily manage your API keys and folder organization.

* **Interactive Quiz:** An **elegant** and modern web interface for training, including progress tracking.

* **Real-Time Logs:** Detailed visualization of the conversion process (Upload, Analysis, Saving) directly in the interface.

## 🛠️ Project Structure

* **`master_class.py`:** The "brain" of the desktop application (Tkinter Interface).

* **`pdf_to_json.py`:** The processing script that ensures communication with the Gemini API.

* **`quizz.html`:** The quiz user interface, dynamic and responsive.

* **`Questions/`:** Storage folder for the generated **JSON** files.

> **Notes:**
> This application uses **Gemini**, but the `pdf_to_json.py` file is designed to be easily adaptable to other LLMs or local AIs.
> Questions are already included for courses from **Prépa**, **CentraleSupélec**, and the **Magistère d'Orsay**.

## 📦 Installation & Configuration

### 1. Prerequisites

* **Python 3.8** or higher.

* A **Google Gemini API key**.

### 2. Installing dependencies

Open a terminal in the project folder and run:

`pip install -r requirements.txt`

## 📋 Usage

1. **Launch the application:** Run `python master_class.py` (or `python3`).

2. **Configure your API Key:** Enter your Gemini key in the dedicated field and click **Save**.

3. **Select your PDFs:** Choose the folder containing your mathematics courses.

4. **Launch the conversion:** The AI will generate JSON files in the `Questions` folder.

5. **Review:** Click **"Launch Quiz"** to start your revisions in your browser.

## 🧪 Technical Details

The application relies on a set of modern technologies:

* **Python:** For the logic processing engine and the native interface.

* **Google Generative AI:** `gemini-3-flash-preview` model for semantic and mathematical analysis.

* **HTML5 / Tailwind CSS:** For the quiz interface.

* **MathJax:** For rendering mathematical formulas in $\LaTeX$.
