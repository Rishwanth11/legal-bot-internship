# pdf_extractor.py
import PyPDF2  # Make sure you have installed this using 'pip install pypdf2'
import os      # To handle file paths

def extract_text_from_page(pdf_path, page_number):
    """
    Opens a PDF file and extracts text from a specific page.
    Args:
        pdf_path (str): The path to the PDF file.
        page_number (int): The page number to extract text from (starting from 0).
    Returns:
        str: The extracted text, or an error message.
    """
    if not os.path.exists(pdf_path):
        return f"Error: The file '{pdf_path}' was not found."
        
    try:
        with open(pdf_path, 'rb') as pdf_file: # Open in binary read mode
            reader = PyPDF2.PdfReader(pdf_file)
            
            if 0 <= page_number < len(reader.pages):
                page = reader.pages[page_number]
                text = page.extract_text()
                if text:
                    return text.strip() # Remove leading/trailing whitespace
                else:
                    return f"Info: No text found on page {page_number}."
            else:
                return f"Error: Page number {page_number} is out of range (Total pages: {len(reader.pages)})."

    except Exception as e:
        return f"An unexpected error occurred while reading '{pdf_path}': {e}"

# --- Main execution block (runs when the script is executed directly) ---
if __name__ == "__main__":
    # Define the path to your BNS PDF within the 'data' folder
    bns_pdf_path = os.path.join("data", "bns.pdf") 
    
    # --- Example: Extract text from the first page (page index 0) ---
    target_page = 0 
    extracted_text = extract_text_from_page(bns_pdf_path, target_page)
    
    # Print the result
    print(f"--- Text from Page {target_page} of {os.path.basename(bns_pdf_path)} ---")
    print(extracted_text)
    
    print("\n" + "="*50 + "\n") # Separator
    
    # --- Example: Extract text from page 10 (page index 9) ---
    target_page_2 = 9
    extracted_text_2 = extract_text_from_page(bns_pdf_path, target_page_2)
    
    print(f"--- Text from Page {target_page_2} of {os.path.basename(bns_pdf_path)} ---")
    print(extracted_text_2)