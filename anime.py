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


def filter_data_by_anime(anime):
    filtered_data_anime = data[data['name'].str.upper().str.contains(anime)]
    return filtered_data_anime


def filter_data_by_genre(genre):
    filtered_data_genre = data[data['genre'] == genre]
    return filtered_data_genre


data_load_state = st.text('Loading...')
data = load_data(500)
data_load_state.text("Done!")

if st.sidebar.checkbox('Mostrar Animes'):
    st.subheader('Todos los Animes')
    st.write(data)

titulofilme = st.sidebar.text_input('Titulo del Anime :')
btnBuscar = st.sidebar.button('Buscar Animes')

if (btnBuscar):
    data_anime = filter_data_by_anime(tituloanime.upper())
    count_row = data_anime.shape[0]
    st.write(f"Total mostrados : {count_row}")
    st.write(data_anime)

selected_genre = st.sidebar.selectbox(
    "Seleccionar Genero", data['genre'].unique())
btnFilterbyGenre = st.sidebar.button('Filtrar genero ')

if (btnFilterbyGenre):
    filterbygen = filter_data_by_genre(selected_genre)
    count_row = filterbygen.shape[0]
    st.write(f"Total Animes : {count_row}")

    st.dataframe(filterbygen)
