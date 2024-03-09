import requests
import pandas as pd
import streamlit as st
from io import StringIO
from bs4 import BeautifulSoup
from typing import List, Dict, Callable

def get_languages()-> Dict:
    response = requests.get('https://meta.wikimedia.org/wiki/Wiktionary#List_of_Wiktionaries')
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    df = pd.read_html(StringIO(str(table)))[0]
    return df.set_index('Language')['Wiki'].to_dict()

# Function to perform a specific action based on the selected option
def perform_action(selected_option):
    # Replace this with the specific action you want to perform
    st.write(f"Scaping will be performed on: {selected_option}")

def translate_keywords(lang_code):
    keywords = ['special', 'categories', 'verbs', 'nouns', 'prepositions', 'adjectives']
    
