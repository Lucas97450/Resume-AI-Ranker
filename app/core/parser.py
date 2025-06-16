from pdfminer.high_level import extract_text
from pathlib import Path

# PDF parser function
def parse_pdf(input_path, output_path):
    path = Path(input_path)
    pdf_text = extract_text(input_path)

    # Save in parsed_cvs
    output_file = Path(output_path) / (path.stem + ".txt")
    output_file.write_text(pdf_text, encoding="utf-8")

def parse_all_pdf(input_folder, output_folder):
    pdf_folder = Path(input_folder)
    pdf_files = pdf_folder.glob("*.pdf")
    
    for pdf_path in pdf_files:
        parse_pdf(pdf_path, output_folder)
        print(pdf_path, output_folder)
