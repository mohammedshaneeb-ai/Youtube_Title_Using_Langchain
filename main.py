from dotenv import load_dotenv
import streamlit as st
import os
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain,SequentialChain

load_dotenv()

# getting OPEN AI KEY
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

# Streamlit UI
st.title('SEARCH PRESIDENT')
input_text = st.text_input('Enter the content')


# LLMs
llm = OpenAI(temperature=0.9)


# Prompt Template
first_input_prompt = PromptTemplate(
    input_variables=['content'],
    template="{content} this is my content included in Youtube Video. i want a good unique Title for that",
)

second_input_prompt = PromptTemplate(
    input_variables=['title'],
    template="give the description and hashtags for youtube video on topic {title} "
)

chain = LLMChain(
    llm=llm,
    prompt=first_input_prompt,
    verbose=True,
    output_key='title'
)

chain2 = LLMChain(
    llm = llm,
    prompt=second_input_prompt,
    verbose=True,
    output_key='description'

)

full_chain = SequentialChain(
    chains=[chain,chain2],
    input_variables=['content'],
    output_variables=['title','description'],
    verbose=True)



if input_text:
    st.write(full_chain({'content':input_text}))

