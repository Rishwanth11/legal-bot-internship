# pdf_extractor.py
import PyPDF2
import os
import json # Import the json library

def extract_all_text_from_pdf(pdf_path):
    """
    Opens a PDF file and extracts text from all pages.
    Args:
        pdf_path (str): The path to the PDF file.
    Returns:
        list: A list where each item is the text content of a page, 
              or an error message string if failed.
    """
    if not os.path.exists(pdf_path):
        return f"Error: The file '{pdf_path}' was not found."
        
    all_pages_text = []
    try:
        with open(pdf_path, 'rb') as pdf_file: 
            reader = PyPDF2.PdfReader(pdf_file)
            num_pages = len(reader.pages)
            print(f"Reading {num_pages} pages from {os.path.basename(pdf_path)}...")
            
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                text = page.extract_text()
                if text:
                    all_pages_text.append(text.strip()) 
                else:
                    all_pages_text.append(f"Info: No text found on page {page_num}.")
            
            return all_pages_text

    except Exception as e:
        return f"An unexpected error occurred while reading '{pdf_path}': {e}"

# --- Placeholder for structuring function (We will build this) ---
def structure_text_data(pages_text, source_doc_name):
    """
    (Placeholder) Takes list of page texts and attempts to structure it 
    into sections (e.g., list of dictionaries). 
    For now, it just returns a simple combined text structure.
    """
    print("Structuring data (basic implementation)...")
    # --- Future Work: Implement logic here to split text into sections ---
    # For now, let's just create one dictionary per page as a basic structure
    structured_data = []
    for i, page_text in enumerate(pages_text):
         structured_data.append({
             "page_number": i,
             "text": page_text,
             "source_document": source_doc_name
         })
    return structured_data

# --- Main execution block ---
if __name__ == "__main__":
    bns_pdf_path = os.path.join("data", "bns.pdf") 
    
    # 1. Extract text from all pages
    raw_pages_text = extract_all_text_from_pdf(bns_pdf_path)
    
    if isinstance(raw_pages_text, str): # Check if extraction returned an error message
        print(raw_pages_text)
    else:
        # 2. Structure the extracted text (using our basic placeholder function)
        structured_legal_data = structure_text_data(raw_pages_text, os.path.basename(bns_pdf_path))
        
        # 3. (Optional but recommended) Save the structured data to a JSON file
        output_json_path = "data/bns_structured_basic.json"
        try:
            with open(output_json_path, 'w', encoding='utf-8') as f:
                json.dump(structured_legal_data, f, ensure_ascii=False, indent=4)
            print(f"Successfully saved basic structured data to {output_json_path}")
            
            # Print a small sample of the structured data
            print("\n--- Sample of Structured Data (First 2 entries) ---")
            print(json.dumps(structured_legal_data[:2], indent=4))

        except Exception as e:
            print(f"Error saving data to JSON: {e}")