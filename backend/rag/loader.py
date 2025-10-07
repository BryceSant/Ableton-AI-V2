from pypdf import PdfReader
from langchain_core.documents import Document
import os 
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_pdfs(pdf_folder_path):
    #Load empty list for pdf's
    pdf_list = []
    #print(os.getcwd())

    #get the path to pdf's
    for pdf in os.listdir(pdf_folder_path):
        print(pdf) 
        if pdf.lower().endswith(".pdf"):
            pdf_reader = PdfReader(os.path.join(pdf_folder_path, pdf)) #loads pdf individually
            pdf_len = len(pdf_reader.pages) #gives number of pages
            #pdf_meta = pdf_reader.metadata #gives possible metadata

            for x in range(pdf_len):
                page = pdf_reader.pages[x]
                page_text = page.extract_text()
                #print(page_text)

                page_metadata = {
                    "source": pdf,
                    "page_number": x + 1,
                    "file_path": pdf_folder_path,
                }

                #print(page_metadata)

                pdf_list.append(Document(page_content = page_text, metadata = page_metadata))
                #print(pdf_list)
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 300, 
        chunk_overlap = 30,
    )

    split_docs = splitter.split_documents(pdf_list)
    
    return split_docs





        


