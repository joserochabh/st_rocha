import streamlit as st
import numpy as np


#Titulo
st.title("Streamlit Titulo")
# Header/subHeader
st.header('Streamlit Header')
st.subheader('Streamlit Header')
#Texto
st.text('Sctreamlit texto')
#Markdown
st.markdown('### Streamlit *** Markdown ***')
# Error/colorfull texto
st.success('Sucesso')
st.info('Informação')
st.error('Erro')
st.warning('Atenção - warning')
st.exception("Nome do erro('Variavel especifica nao definida')")
#Help sobre comandos do python
st.help(range)
#Escreva texto com write
st.write('Texto ecrito usando write')
st.write(range(10))