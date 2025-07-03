import streamlit as st
st.header("All file reader")


with st.sidebar:
    st.title("Upload your document here")
    file_pdf=st.file_uploader("upload pdf", type="pdf")
    file_text=st.file_uploader("Upload_text", type="text")


    

