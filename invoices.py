from docling import document_converter
from langchain_text_splitters import MarkdownHeaderTextSplitter
import ollama
import os
import json
import re
import postInvoice as pi

def parseInvoice(location,file_name):


    new_file_path = os.path.splitext(file_name)[0] + ".md"

    if os.path.exists(f"markdown/{new_file_path}"):
        with open(f"markdown/{new_file_path}", "r", encoding="utf-8") as f:
            docs = f.read()
    else:
        converter = document_converter.DocumentConverter()
        result = converter.convert(location)
        docs=result.document.export_to_markdown()
        with open(f"markdown/{new_file_path}", "w", encoding="utf-8") as f:
            f.write(docs)

    splitter = MarkdownHeaderTextSplitter( #for larger documents, modify headers accordingly
                    headers_to_split_on=[
                        ("####", "Header_1"),
                        ("#####", "Header_2"),
                        ("######", "Header_3"),
                    ],
                )

    splits = splitter.split_text(docs)
    print(len(docs))



    summary = """{{

        {
        "Vendor": <POPULATE WITH VENDOR NAME>,
        "InvoiceNum": <POPULATE WITH INVOICE NUMBER>,
        "PONum": <POPULATE WITH PO NUMBER>,
        "InvoiceAmount": <POPULATE WITH TOTAL COST>,
        }

    }}"""  

    new_text_file_path = os.path.splitext(file_name)[0] + ".txt"
    output_file_path = f"debug/{new_text_file_path}"

    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write("")

    for i, chunk in enumerate(splits):
        prompt = f"""
    Instructions:
    - Extracting Vendor name, Invoice number, PO Number, Total Cost from an invoice.
    - Read the **CURRENT CHUNK** of the document.
    - Build on the **PREVIOUS RESPONSE** to progressively refine the information from the invoice.
    - Do not add more information than requested.
    - DO NOT CHANGE JSON KEY NAMES, ONLY THEIR VALUES.


    **CURRENT CHUNK:**
    {docs}

    **PREVIOUS RESPONSE:**
    {summary}

    Return only the json object.
    """
        

        response = ollama.chat(model="qwen2.5:0.5b", messages=[{"role": "user", "content": prompt}])
        previuous=summary
        summary = response['message']['content']  

        with open(output_file_path, "a", encoding="utf-8") as f:
            f.write(f"-----------Processed chunk {i+1}/{len(splits)}--------------------------------------------------------------\n")
            f.write(f"------------------------------------------------------------------------------------------------------------\n")
            f.write(f"--------------Chunk Info------------------------------------------------------------------------------------\n")
            f.write(chunk.page_content + "\n")
            f.write(f"------------------------------------------------------------------------------------------------------------\n")
            f.write(f"--------------Previous Chunk Summary------------------------------------------------------------------------\n")
            f.write(previuous + "\n")
            f.write("\n\n")  
            f.write(f"------------------------------------------------------------------------------------------------------------\n")
            f.write(f"--------------Chunk Summary---------------------------------------------------------------------------------\n")
            f.write(summary + "\n")
            f.write("\n\n")  



    json_match = re.search(r'(\{[\s\S]*?\})', summary)


    if json_match:
        json_string = json_match.group(1).strip()
        
        try:
            extracted_data = json.loads(json_string)
            

            ##Enter invoice verification logic here
            ##For example: query received not invoiced records, filtering on PO

            return extracted_data
        except json.JSONDecodeError as e:
            return f"Error decoding JSON: {e}"
    else:
        return "No JSON found in response."






