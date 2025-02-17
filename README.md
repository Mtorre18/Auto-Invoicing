📄 AI-Powered Invoice Verification & Processing for ERP Systems

A simple AI-driven application to verify and process invoices using Gradio & Ollama.

🚀 Features:

✅ Upload Invoices (PDF format).

✅ AI-powered invoice extraction & verification.

✅ User confirmation before posting the invoice.

✅ Integrates with ERP via API for automated invoice posting.




🔧 Installation & Setup

1️⃣ Install Dependencies

Before running the app, install the required Python packages:

pip install gradio ollama python-dotenv requests langchain-text-splitters docling


2️⃣ Set Up Ollama

If you haven’t installed Ollama, follow these steps:

Install Ollama:

curl -fsSL https://ollama.com/install.sh | sh

Download the AI model (if required):

ollama pull llama3


3️⃣ Run the Gradio App

Run the application locally:
python App.py
The app will open in your browser at:

http://127.0.0.1:7860

📂 Project Structure

📁 CHATBOT

│── App.py                # Main Gradio app

│── invoices.py           # Invoice processing logic

│── postInvoice.py        # ERP invoice posting logic

│── requirements.txt      # List of dependencies

│── README.md             # Project documentation




🎯 How It Works

1️⃣ Upload an invoice (PDF).

2️⃣ AI extracts & verifies invoice data.

3️⃣ User reviews and confirms the extracted data.

4️⃣ On confirmation, the invoice is posted to ERP.


📌 Future Enhancements

🔹 Add invoice validation checks (e.g., missing fields, duplicate detection).

🔹 Log all processed invoices for auditing.

🔹 Allow multi-user access with authentication.

🔹 Enhance AI model for better invoice understanding.


📬 Need Help?

If you have any questions, feel free to reach out to xaviert44@outlook.com! 🚀
