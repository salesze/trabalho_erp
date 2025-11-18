from sqlalchemy import create_engine, text
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

engine = create_engine("mysql+pymysql://root:Joao10203030!@localhost/erp_estoque")

def cadastrar_produto():
    nome = input("Nome do produto: ")
    categoria = input("Categoria: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade inicial: "))
    datahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with engine.connect() as conn:
        conn.execute(text(
            "INSERT INTO produtos (nome, categoria, preco, quantidade, ultima_mov) "
            "VALUES (:nome, :categoria, :preco, :quantidade, :ultima_mov)"
        ), {"nome": nome, "categoria": categoria, "preco": preco,
            "quantidade": quantidade, "ultima_mov": datahora})
        conn.commit()

    print("Produto cadastrado com sucesso!")