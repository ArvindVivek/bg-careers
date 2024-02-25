import PyPDF2

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        return text
    
if __name__ == "__main__":
    file_path = "data/www.paulawrzecionowska.com/resume/resume.pdf"
    print(extract_text_from_pdf(file_path))