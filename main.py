from dotenv import load_dotenv
import streamlit as st
import os
load_dotenv()


OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
