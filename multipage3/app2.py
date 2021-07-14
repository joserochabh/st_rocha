import streamlit as st
#import Lbs001
from pages import home, page1, page2


   
menu1 = ["Home", "Pagina1", "Pagina2",]
escolha = st.sidebar.selectbox("Escolha", menu1)
if escolha == "Home":
    home.app()
elif escolha == "Pagina1":
    page1.app()
elif escolha == "Pagina2":
    page2.app()
