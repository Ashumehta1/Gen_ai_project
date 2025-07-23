from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

#Promt templet
prompt=ChatPromptTemplate.from_messages(
    [
    ("system","You are helpful assistant.Please responce user query"),
    ('user',"question {question}")
    ]
)

#function to generate response
def generate_responce(question,engine,temperature,max_token):
    llm=Ollama(model=engine)
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({"question":question})
    return answer

#side bar
engine=st.sidebar.selectbox("select llm for responce",['gemma2','llama2'])
temperature=st.sidebar.slider("select temp for model",min_value=0.0,max_value=1,value=0.7)
max_token=st.sidebar.slider("select the number of token",min_value=150,max_value=300,value=170)


st.write("Ask your questions")
user_input=st.text_input("you: ")

if user_input:
    response=generate_responce(user_input,engine,temperature,max_token)
    st.write(response)
elif user_input:
    st.warning("please provide your questions")
else:
    st.write("please provide user input")