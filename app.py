"""Interface do conversor de moeda criada com Streamlit."""

import streamlit as st 
from conversor_utils.taxas import taxas 
from conversor_utils.conversor import converter 

# Titulo da pagina e o layout
st.set_page_config(page_title="Conversor de Moeda", layout="centered")

# Mostrar o titulo principal da aplicação
st.title("Conversor de Moeda 🪙")

# Texto intro
st.markdown("Esta aplicacão permite converter valores entre **EUR**, **USD** e **GBP**")

# User input
valor = st.number_input(
    label="Intrdoza o valor a converter:",
    min_value=0.0,
    format="%.2f"
)

# Lista de moedas disponiveis
moedas_disponiveis = list(taxas.keys())

# EScolha da moeda origem + moeda destino 
moeda_origem = st.selectbox("De:", moedas_disponiveis, index=0)
moeda_destino = st.selectbox("Para:", moedas_disponiveis, index=1)

# Executar a conversão
if st.button("Converter"):
    try:
        resultado = converter(valor, moeda_origem, moeda_destino)
        st.success(f"{valor:.2f} {moeda_origem} = {resultado:.2f} {moeda_destino}")

    except ValueError as e:
        st.error(f"Erro: {e}")
