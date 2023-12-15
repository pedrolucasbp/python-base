#!/usr/bin/env python3
"""Script para simular um compra de produtos
"""
__author__ = "Pedro Lucas"
__version__ = "0.0.1"

from pprint import pprint

produto = {
        "Nome": "Celular",
        "Cor": ["azul","branco"],
        "Preco": "200 €",
        "Dimensao": {
            "altura": "124mm",
            "largura": "020mm"},
        "em_estoque": True,
        "id": 123456
}

cliente = {
        "Nome": "Pedro Lucas",
        "id": 123
}

compra = {
        "cliente": cliente,
        "produto": produto,
        "quantidade": 1
}

total_compra = compra["quantidade"] * compra["produto"]["Preco"]

pprint(
        f"O cliente {compra['cliente']['Nome']}"
        f" comprou {compra['quantidade']} unidade(s) de {compra['produto']['Nome']}"
        f" e pagou o total de {total_compra}"
        )
