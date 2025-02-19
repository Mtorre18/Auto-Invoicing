# 🧾 Lolcal AI-Powered Invoice Verification & Processing for ERP Systems

A simple AI-driven application to verify and process invoices using  **Docling**, **Gradio** & **Ollama**.

## Features

-  **Upload Invoices (PDF format) using Gradio UI**.
-  **Convert document to markdown using Docling**.
-  **Extract relevant data with Ollama model**.
-  **User confirmation** before posting the invoice.
-  **ERP Integration** via API for automated invoice posting.

---

## 🔧 Installation & Setup

### 1️⃣ Install Dependencies
Before running the app, install the required Python packages:

```sh
pip install gradio ollama python-dotenv requests langchain-text-splitters docling

```


### 2️⃣ Set Up Ollama

If you haven’t installed Ollama, follow these steps:

Install Ollama:

curl -fsSL https://ollama.com/install.sh | sh

Download the AI model.
I used qwen2.5:0.5b for development only.

```sh
ollama pull qwen2.5:0.5b
```


### 3️⃣ Run the Gradio App

Run the application locally:
```sh
python App.py
```
The app will open in your browser at:

http://127.0.0.1:7860


📂 Project Structure

│── App.py                # Main Gradio app

│── invoices.py           # Invoice processing logic

│── postInvoice.py        # ERP invoice posting logic

│── requirements.txt      # List of dependencies

│── README.md             # Project documentation




###  How It Works

1️⃣ Upload an invoice (PDF).

2️⃣ AI extracts & verifies invoice data.

3️⃣ User reviews and confirms the extracted data.

4️⃣ On confirmation, the invoice is posted to ERP.


###  Future Enhancements

🔹 Add invoice validation checks (e.g., missing fields, duplicate detection).

🔹 Log all processed invoices for auditing.

🔹 Allow multi-user access with authentication.



