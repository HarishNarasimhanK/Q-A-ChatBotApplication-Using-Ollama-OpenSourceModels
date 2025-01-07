import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import os
from dotenv import load_dotenv
load_dotenv()

## Langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "QnA CHATBOT APP"

prompt = ChatPromptTemplate.from_messages([
    ("system","you are an helpful assistant. Answer the question raised by the user in atmost 5 sentences"),
    ("user","{question}")
])

output_parser = StrOutputParser()

def generate_response(question,model,temperature): # temperature value: 0 to 1 [0-> not creative 1-> very creative]
    llm = Ollama(
        model = model,
        temperature = temperature
        )
    chain = prompt | llm | output_parser
    answer = chain.invoke({"question":question})
    return answer

st.title("QnA ChatBot")
with st.form("question_form"):
    model_name = st.sidebar.selectbox("Select the model",["gemma2:2b","llama3.2"])
    temperature = st.sidebar.slider("select creativity level - temperature", 0.0, 1.0, 0.5,step = 0.1)
    question = st.text_input("Ask your question..")
    submitted = st.form_submit_button("ask")

if submitted and question:
    st.write("Generating response . . .")
    try:
        response = generate_response(question, model_name, temperature)
        st.write('**Response :**')
        st.write(response)
    except Exception as e:
        st.error(f"AN ERROR OCCURED {e}")
elif submitted and not question:
    st.warning("please type a question before asking the chat bot")

