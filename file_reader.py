import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader, PyPDFLoader
st.header("All file reader")


with st.sidebar:
    st.title("Upload your document here")
    file_pdf=st.file_uploader("upload pdf", type="pdf")
    # file_text=st.file_uploader("Upload_text", type="text")

if file_pdf is not None:
    # loader=TextLoader(file_text)
    loader_pdf=PdfReader(file_pdf)
    text =""
    for page in loader_pdf.pages:
        text +=page.extract_text()
        #st.write(text)
  
text_spliter=RecursiveCharacterTextSplitter(separators="\n", chunk_size=1000, chunk_overlap=100,length_function=len)
chunks=text_spliter.split_text(text)
st.write(chunks)
    

