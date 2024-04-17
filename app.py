from libretranslatepy import LibreTranslateAPI
from fpdf import FPDF
from PyPDF2 import PdfReader

def translate_pdf():
    translator = LibreTranslateAPI()

    pdfFileObj = open('bbb.pdf','rb')
    pdfreader = PdfReader(pdfFileObj)
    pdf = FPDF()
    pages = len(pdfreader.pages)
    for n in range(pages):
        pageObj = pdfreader.pages[n]
        extracted_text = pageObj.extract_text()
        paragraphs = extracted_text.split('\n')
        pdf.add_page()
        pdf.set_font("Arial", size= 11)
        for p in paragraphs:
            translated_text = translator.translate(p, "en", "fr")  # Translate to French
            pdf.multi_cell(0, 5, translated_text)
            pdf.ln()
    pdf.output("out1.pdf")

if __name__ == '__main__':
    translate_pdf()
