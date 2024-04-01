from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama #3rd party intigration config
import streamlit as st
import os 
from dotenv import load_dotenv

load_dotenv()

 

## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true" 
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "default_value")


## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("System","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title('Langchain Demo With LLAMA2 API')
input_text=st.text_input("Search the topic you want")

# ollama, 
llm= Ollama(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
   st.write(chain.invoke({'question':input_text}))