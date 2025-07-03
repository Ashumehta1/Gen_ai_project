import streamlit as st
#from PyPDF2 import PdfReader
from langchain_community.document_loaders import TextLoader, PyPDFLoader
st.header("All file reader")


with st.sidebar:
    st.title("Upload your document here")
    file_pdf=st.file_uploader("upload pdf", type="pdf")
    file_text=st.file_uploader("Upload_text", type="text")

if file_pdf or file_text is not None:
    loader=TextLoader(file_text)
    loader_pdf=PyPDFLoader(file_pdf)
    Text_document=loader.load()
    pdf_document=loader_pdf.load()
    st.write(Text_document)
    st.write(pdf_document)

    

