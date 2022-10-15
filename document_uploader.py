from PyPDF2 import PdfFileReader


class DocumentUploader:
    # creating a pdf file object
    def __init__(self, path):
        self.pdfObject = open(path, 'rb')
        self.pdfReader = PdfFileReader(self.pdfObject)  # creating a pdf reader object
        self.text = None
        self.pageObject = None

    def extract(self):
        # Extract and concatenate each page's content
        self.text = ''
        for i in range(0, self.pdfReader.numPages):
            self.pageObject = self.pdfReader.getPage(i)  # creating a page object
            self.text += self.pageObject.extractText()  # extracting text from page
        return self.text


document_path = "Insurance_act_18.pdf"

raw_document = DocumentUploader(document_path)

document = raw_document.extract()

print(document)
with open('Insurance_act_18.txt', 'w') as file:
    file.write(document)
