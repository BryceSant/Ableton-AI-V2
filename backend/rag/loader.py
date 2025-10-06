from pypdf import PdfReader
import os 

def load_pdfs(pdf_folder_path):
    #Load empty list for pdf's
    pdf_list = []
    #print(os.getcwd())

    #get the path to pdf's
    for pdf in os.listdir(pdf_folder_path):
        print(pdf)
        if pdf.endswith(".pdf"):
            reader = PdfReader(os.path.join(pdf_folder_path, pdf))
            num_pages = len(reader.pages)
            print(num_pages)
        


