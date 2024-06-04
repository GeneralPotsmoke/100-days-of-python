import PyPDF2
import pyttsx3

def pdf_to_audiobook(pdf_path):
    pdf_reader = PyPDF2.PdfFileReader(open(pdf_path, 'rb'))
    speaker = pyttsx3.init()
    for page_num in range(pdf_reader.numPages):
        text = pdf_reader.getPage(page_num).extract_text()
        speaker.say(text)
        speaker.runAndWait()

pdf_path = 'sample.pdf'
pdf_to_audiobook(pdf_path)
