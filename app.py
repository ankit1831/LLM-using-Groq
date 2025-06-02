import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
load_dotenv()

## Langsmith Tracking


groq_api_key = st.secrets["GROQ_API_KEY"]
model=ChatGroq(model="Gemma2-9b-It",groq_api_key=groq_api_key)
## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the question asked"),
        ("user","Question:{question}")
    ]
)

## streamlit framework
st.title("LLM-Chat Assistant using Groq")
input_text=st.text_input("What question you have in mind?")


## Ollama Llama2 model
#llm=Ollama(model="gemma:2b")
output_parser=StrOutputParser()
chain=prompt|model|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))


