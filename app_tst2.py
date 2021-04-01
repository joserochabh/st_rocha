import pandas as pd
import streamlit as st
import numpy as np
import time
from streamlit_agraph import agraph, Node, Edge, Config
import streamlit_theme as stt



st.sidebar.title('Dashboard Menu XXX:')
pag_selec = st.sidebar.selectbox('Opções Disponíveis', ['Estados', 'Cidades', 'Widgets', 'Graph', 'Mais Elementos'])


if pag_selec == 'Estados':
    st.title('Testes com StreamLit')
    st.selectbox('Escolha um estado:', ['Minas gerais', 'Goias', 'Paraná'])
    
    
elif pag_selec == 'Cidades':
    st.title('Testes com StreamLit')
    st.selectbox('Escolha uma cidade:', ['Belo Horizonte', 'Goiania', 'Curitiba'])
    
    
elif pag_selec == 'Widgets':
    st.title('Componentes StreamLit')
        
    # Add a selectbox to the sidebar:
    add_selectbox = st.selectbox(
        'Como você gostaria de ser contactado?',
        ('Email', 'Home phone', 'Mobile phone'))

    # Add a slider to the sidebar:
    add_slider = st.slider(
        'Selecione um range of valores',
        0.0, 100.0, (25.0, 75.0))
    
        # Add a slider to the sidebar:
    Faixa_num = st.slider(
        'Selecione um range of valores inteiros',
        0, 100, (25, 75))
    st.write(f"Escolheu entre {Faixa_num} como range numerico!")

    chosen = st.radio(
        'Escolha uma Cidade',
        ("Belo Horizonte", "Contagem", "Luz", "Nova Era"))
    st.write(f"Escolheu {chosen} como a sua cidade preferida!")
    
        # Get some data.
    data = np.random.randn(10, 2)
    # Show the data as a chart.
    chart = st.line_chart(data)
    # Wait 1 second, so the change is clearer.
    time.sleep(1)
    # Grab some more data.
    data2 = np.random.randn(10, 2)
    # Append the new data to the existing chart.
    chart.add_rows(data2)

elif pag_selec == 'Mais Elementos':
    st.title('Mais alguns Elementos StreamLit')
    st.text('This will appear first')
    # Appends some text to the app.
    my_slot1 = st.empty()
    # Appends an empty slot to the app. We'll use this later.
    my_slot2 = st.empty()
    # Appends another empty slot.
    st.text('This will appear last')
    # Appends some more text to the app.
    my_slot1.text('This will appear second')
    # Replaces the first empty slot with a text string.
    my_slot2.line_chart(np.random.randn(20, 2))
    # Replaces the second empty slot with a chart.
    
    dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
    st.dataframe(dataframe.style.highlight_max(axis=0))
    
    dataframe1 = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
    st.table(dataframe1)
    
elif pag_selec == 'Graph':
    st.title('Testes com Grafos')
    nodes = []
    edges = []
    nodes.append( Node(id="Spiderman", label="Peter Parker", size=400, svg="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_spiderman.png") ) # includes **kwargs
    nodes.append( Node(id="Captain_Marvel", size=400, svg="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_captainmarvel.png") )
    nodes.append( Node(id="Thor", size=400, svg="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_thor.png") )
    nodes.append( Node(id="Thanos", size=400, svg="http://marvel-force-chart.surge.sh/marvel_force_chart_img/thanos.png") )

    edges.append( Edge(source="Captain_Marvel", label="Amiga de ", target="Spiderman", type="CURVE_SMOOTH") ) # includes **kwargs
    edges.append( Edge(source="Captain_Marvel", label="Conhece o", target="Thor", type="CURVE_SMOOTH") ) # includes **kwargs
    edges.append( Edge(source="Thor", label="Inimigo de", target="Thanos") ) # includes **kwargs

    config = Config(width=500, 
                    height=500, 
                    directed=True,
                    nodeHighlightBehavior=True, 
                    highlightColor="#F7A7A6", # or "blue"
                    collapsible=True,
                    node={'labelProperty':'label'},
                    link={'labelProperty': 'label', 'renderLabel': True}
                    # **kwargs e.g. node_size=1000 or node_color="blue"
                    ) 

    return_value = agraph(nodes=nodes, 
                      edges=edges, 
                      config=config)


