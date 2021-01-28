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
# imagem
from PIL import Image
img = Image.open('arquivos/bot2.jpg')
st.image(img,width=200, caption='Imagem simples')
#Video
vid = open('arquivos/sample.mp4', 'rb').read()
st.video(vid)
#Arquivo de audio
audio1 = open('arquivos/Folia.mp3', 'rb').read()
st.audio(audio1, format='audio/mp3')

######################
#       Widgets      #
######################
# checkbox
if st.checkbox('Mostra'):
    st.text('Mostrando')
if st.checkbox('Oculta'):
    st.text('Ocultando')
# Radio
status = st.radio('Escolha uma opção:', ['Bonitão', 'Feioso'])
if status == 'Bonitão':
    st.warning('Warning - Bonitão nada!')
elif status == 'Feioso':
    st.success('Sucesso!!, acertou miseravi')

#SelectBox
pag_selec = st.selectbox('Opções Disponíveis', ['Estados', 'Cidades'])
st.write('Você selecionou: ', pag_selec)

#Multiselect
cidade = st.multiselect('Cidade mais fresquinha', ('Nova Era', 'Luz', 'Birité','Játeve'))
st.write('Você selecionou: ',len(cidade),' lugares')

#Slider
idade = st.slider('Qual é a sua idade: ', 50,100)
st.warning(idade)

#Buttons
st.button('Botão Simples')

if st.button('Não Clique'):
    st.write('É incrivel, Você Clicou')
    
#Entrada de texto
texto = st.text_input('Entre com seu nome: ', 'Digite aqui..')
if st.button('Enviar'):
    resultado = texto.title()
    st.success(resultado)

# Area de texto
mensagem = st.text_area('Entre com sua mensagem: ', 'Digite..')
if st.button('Envie'):
    resultado1 = mensagem.title()
    st.success(resultado1)

# Entrando com datas
import datetime
hoje = st.date_input('Hoje é: ', datetime.datetime.now())

# Horario
agora = st.time_input('Agora é: ', datetime.time())

# Exibindo JSON
st.text('Exibindo um JSON')
st.json({'nome':'Jose Rocha', 'idade':'54 anos', 'ocupação':'analista de suporte'})

# Exibindo raw code
st.text('Exibindo linhas de código(raw code)')
st.code('import pandas as pd')

# Exibindo raw code
st.text('Exibindo linhas de código(raw code)')
with st.echo():
    #Esse é um comentário
    import numpy as np
    import pandas as pd
    df = pd.DataFrame()

# Progress bar
import time
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p + 1)

# Spining
with st.spinner('Aguarde..'):
    time.sleep(10)
st.success('Conclído')

#Balões
st.balloons()
# Side Bars
st.sidebar.header('Essa é uma SideBar')
st.sidebar.text('Esse são modelos para streamlit')

#Funções
@st.cache
def run_fxn():
    return range(100)
st.write(run_fxn())

#plot
#st.pyplot()

# Dataframe
#st.dataframe(df)

# tabela
#st.table(df)
df = pd.DataFrame(
    np.random.randn(4, 6),
    columns=('col %d' % i for i in range(6))
    )
st.table(df.style.set_precision(2))
