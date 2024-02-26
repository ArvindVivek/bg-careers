import PyPDF2
import requests

def extract_text_from_pdf(file_path):
    if file_path.startswith("http"):
        response = requests.get(file_path)
        file_path = "data/temp.pdf"
        with open(file_path, 'wb+') as file:
            file.write(response.content)

    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        return text
    
if __name__ == "__main__":
    file_path = "https://careerdocs.charlotte.edu/resumes/AMD/Graphic%20Designer%20Resume%20Example.pdf"
    print(extract_text_from_pdf(file_path))