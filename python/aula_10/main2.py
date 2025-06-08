import streamlit as st
import requests

st.header("Cadastrar Produto")

with st.form('cadastrar-produto'):
    nome = st.text_input("Nome", placeholder="Placa de Vídeo RTX 3070")
    preco = st.number_input("Preço", format="%.2f")
    qtd = st.number_input("Quantidade", step=1)
    categoria = st.selectbox('Categoria', options=['Alimento', 'Informática', 'Higiene', 'Têxtil'], index=None, placeholder="Selecione uma opção")
    
    submit = st.form_submit_button("Cadastrar")

    if submit:
        if not nome or preco == 0 or qtd == 0 or not categoria:
            st.warning("Por favor, preencha todos os campos corretamente.")
        else:
            form_data = {
                "nome": nome,
                "preco": preco,
                "quantidade": qtd,
                "categoria": categoria
            }

            response = requests.post("https://formspree.io/f/xwpblkzg", data=form_data)

            if response.status_code == 200:
                st.success("Produto cadastrado com sucesso!")
            else:
                st.error("Erro ao cadastrar. Verifique os dados ou tente novamente.")
