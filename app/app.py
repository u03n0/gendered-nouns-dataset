import streamlit as st
from utils import get_languages, perform_action

# Main Streamlit app
def main():
    st.title("Wiktionary.org Scraper")
    st.subheader('Select which language version of Wiktionary to use')
        
    languages = get_languages()

    # Display the options for the user to click
    selected_option = st.multiselect("Select a language(s):", languages)

    # Perform the action when the user clicks on an option
    if st.button("Scape"):
        perform_action(selected_option)

# Run the Streamlit app
if __name__ == "__main__":
    main()


