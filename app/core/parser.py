from pdfminer.high_level import extract_text
from pathlib import Path

# PDF parser function
def parse_pdf(path):
    path = Path(path)
    pdf_text = extract_text(path)

    # Save in parsed_cvs
    output_path = Path("parsed_cvs") / (path.stem + ".txt")
    output_path.write_text(pdf_text, encoding="utf-8")

def parse_all_pdf(folder):
    pdf_folder = Path(folder)
    pdf_files = pdf_folder.glob("*.pdf")
    
    for pdf_path in pdf_files:
        parse_pdf(pdf_path)
        print(pdf_path)
