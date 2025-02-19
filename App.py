import gradio as gr
import invoices as inv
import postInvoice as pi
import os

invoice_data = None
file_name = None
invoice_processed = False
invoice_posted = False

def process_invoice(uploaded_file):
    global invoice_data, file_name, invoice_processed

    if uploaded_file:
        file_path = uploaded_file.name
        file_name = os.path.basename(uploaded_file.name)
        invoice_data = inv.parseInvoice(file_path, file_name)
        

        return f"✅ File '{file_name}' uploaded and processed successfully.", invoice_data

    return "Please upload a file first.", ""

def post_to_erp():
    global invoice_posted

    if invoice_data and not invoice_posted:
        action_result = pi.post_invoice(invoice_data)
        invoice_posted = action_result["success"]
        if invoice_posted:
            return "✅ Invoice posted successfully!"
    
    return "Please confirm that the data is correct before posting."

def invoice_status():
    if invoice_posted:
        return "✅ This invoice has already been posted."
    return "No invoice posted yet."

# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("## 📄 AI-Powered Invoice Verification & Processing")

    with gr.Row():
        uploaded_file = gr.File(label="Upload a PDF Invoice", file_types=[".pdf"])
        output_message = gr.Textbox(label="Message", interactive=False, show_label=False)
    
    extracted_data = gr.Textbox(label="Extracted Invoice Data", interactive=False, lines=10)

    post_button = gr.Button("🚀 Post Invoice to ERP", elem_id="post_button")

    # Bind functions to Gradio components
    uploaded_file.change(process_invoice, inputs=uploaded_file, outputs=[output_message, extracted_data])
    post_button.click(post_to_erp, outputs=output_message)


demo.launch()
