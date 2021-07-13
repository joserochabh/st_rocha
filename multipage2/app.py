
import streamlit as st
from pages import home, page1, page2

PAGES = {
    "Home": home,
    "Pagina 1": page1,
    "Pagina 2": page2,
}

st.sidebar.title('Aplicações')
selection = st.sidebar.selectbox("Selecione :", list(PAGES.keys()))
page = PAGES[selection]
page.app()
