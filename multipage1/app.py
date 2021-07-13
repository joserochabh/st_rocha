import streamlit as st

# Custom imports 
from multipage import MultiPage
from pages import home, page1, page2 # import your pages here

# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.title("Streamlit multipages")

# Add all your applications (pages) here
app.add_page("Home", home.app)
app.add_page("Pagina1", page1.app)
app.add_page("Pagina2", page2.app)


# The main app
app.run()