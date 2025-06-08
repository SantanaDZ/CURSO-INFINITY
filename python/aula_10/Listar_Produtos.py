from db import produtos
import streamlit as st

st.set_page_config(
    page_title="Listagem de Pordutos",
)

st.title('Listagem de Produtos')

st.table(produtos)