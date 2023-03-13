import streamlit as st
import pandas as pd
import numpy as np
import codecs

st.sidebar.image("Logo.png")
st.title('RECOMENDACIONES DE ANIME BY CHRISTIAN REYES')
st.text("Christian Eduardo Amaro Reyes - S19004895")

DATE_COLUMN = 'released'
DATA_URL = ('anime.csv')


@st.cache
def load_data(nrows):
    doc = codecs.open('anime.csv', 'rU', 'latin1')
    data = pd.read_csv(doc, nrows=nrows)
    def lowercase(x): return str(x).lower()
    return data


def filter_data_by_filme(filme):
    filtered_data_filme = data[data['name'].str.upper().str.contains(filme)]
    return filtered_data_filme


def filter_data_by_director(director):
    filtered_data_director = data[data['director'] == director]
    return filtered_data_director


data_load_state = st.text('Loading...')
data = load_data(500)
data_load_state.text("Done!")

if st.sidebar.checkbox('Mostrar filmes'):
    st.subheader('Todos los filmes')
    st.write(data)

titulofilme = st.sidebar.text_input('Titulo del filme :')
btnBuscar = st.sidebar.button('Buscar filmes')

if (btnBuscar):
    data_filme = filter_data_by_filme(titulofilme.upper())
    count_row = data_filme.shape[0]
    st.write(f"Total mostrados : {count_row}")
    st.write(data_filme)

selected_director = st.sidebar.selectbox(
    "Seleccionar Director", data['director'].unique())
btnFilterbyDirector = st.sidebar.button('Filtrar director ')

if (btnFilterbyDirector):
    filterbydir = filter_data_by_director(selected_director)
    count_row = filterbydir.shape[0]
    st.write(f"Total filmes : {count_row}")

    st.dataframe(filterbydir)
