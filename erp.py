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

def excluir_produto():
    id_produto = int(input("Informe o ID do produto a ser excluído: "))
    
    with engine.connect() as conn:
        conn.execute(text("DELETE FROM produtos WHERE id=:id"), {"id": id_produto})
        conn.commit()

    print("🗑️ Produto excluído com sucesso!")

def movimentar_estoque():
    id_produto = int(input("Informe o ID do produto: "))
    tipo = int(input("Tipo (1-Entrada, 2-Saída): "))
    qtd = int(input("Quantidade: "))

    with engine.connect() as conn:
        df = pd.read_sql("SELECT * FROM produtos WHERE id=%s" % id_produto, conn)

        if df.empty:
            print("Produto não encontrado.")
            return

        quantidade_atual = int(df.loc[0, "quantidade"])

        # Entrada
        if tipo == 1:
            nova_qtd = quantidade_atual + qtd
        # Saída
        elif tipo == 2:
            if qtd > quantidade_atual:
                print("Estoque insuficiente.")
                return
            nova_qtd = quantidade_atual - qtd
        else:
            print("Tipo inválido.")
            return

        datahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        conn.execute(text(
            "UPDATE produtos SET quantidade=:qtd, ultima_mov=:mov WHERE id=:id"
        ), {"qtd": nova_qtd, "mov": datahora, "id": id_produto})
        conn.commit()

    print("Movimentação registrada.")

def mostrar_relatorio():
    df = pd.read_sql("SELECT * FROM produtos", engine)

    print("\n📊 --- Relatório de Produtos ---")

    if df.empty:
        print("Nenhum produto cadastrado.")
        return

    for _, p in df.iterrows():
        msg = f'ID:{p["id"]} | Nome:{p["nome"]} | Cat:{p["categoria"]} | Preço:R${p["preco"]:.2f} | Qtd:{p["quantidade"]} | Última Mov:{p["ultima_mov"]}'
        if p["quantidade"] < 5:
            msg += " ESTOQUE BAIXO"
        print(msg)