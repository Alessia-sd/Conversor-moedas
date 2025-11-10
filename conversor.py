"""Lógica de converssão entre as moedas."""

from conversor_utils.taxas import taxas 

def converter(valor, moeda_origem, moeda_destino):
    """
    Converte um valor entre duas moedas com base numa taxa ficticia.

    Args:
        valor (float): Valor a converter.
        moeda_origem (str): Código da moeda de origem.
        moeda_destino (str): Código da moeda de destino.
    
    """

    if moeda_origem not in taxas or moeda_destino not in taxas:
        raise ValueError("Moedade não suportada")
    
    valor_em_euros = valor/taxas[moeda_origem]
    valor_convertido = valor_em_euros * taxas[moeda_destino]

    return valor_convertido