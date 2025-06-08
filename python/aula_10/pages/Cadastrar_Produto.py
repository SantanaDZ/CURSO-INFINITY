from db import produtos
import streamlit as st

st.title('Gerencimento de Produtos')


with st.form('cadastrar-produto', clear_on_submit=True) as form:
    nome = st.text_input('Nome', placeholder='Placa de Video RTX 3070')
    preco = st.number_input('Preço')
    quantidade = st.number_input('Quantidade', step=1)
    categoria = st.selectbox(
        'Categoria',
        placeholder='Selecione uma Opção',
        index=None,
        options=['Alimento', 'Informática', 'Higiene', 'Têxtil']
    )

    button = st.form_submit_button('Cadastrar')

    if button:
        produto = {
            'nome': nome,
            'preco': preco,
            'quantidade': quantidade,
            'categoria': categoria
        }
        produtos.append(produto)


