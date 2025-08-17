from db import get_db
from typing import Optional
from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class Produto:
    nome: str
    preco: float
    descricao: str
    quantidade: int
    id: Optional[int] = None

def buscar_produtos() -> list[Produto]:
       # Connectando no Banco de Dados
    db = get_db() 

    # Criando o Cursor
    cursor = db.cursor()

    # Script SQL
    sql = '''
        SELECT nome, preco, descricao, quantidade, id
        FROM produtos
    '''

    # Executando SQL
    cursor.execute(sql)

    # Buscando dados resultantes
    produtos = cursor.fetchall()

    cursor.close()
    db.close()

    return [
        Produto(
            nome=produto[0], 
            preco=produto[1], 
            descricao=produto[2],  
            quantidade=produto[3],
            id=produto[4]
        )
        for produto in produtos
    ]


def criar_produto(produto: Produto) -> Produto:
    # Connectando no Banco de Dados
    db = get_db() 

    # Criando o Cursor
    cursor = db.cursor()

    # Script SQL
    sql = '''
        INSERT INTO produtos (nome, preco, descricao, quantidade)
        VALUES (?, ?, ?, ?) RETURNING id
    '''
    parameters = (
        produto.nome,
        produto.preco,
        produto.descricao,
        produto.quantidade
    )

    cursor.execute(sql, parameters)

    produto.id = cursor.fetchone()[0]
    db.commit()

    cursor.close()
    db.close()

    return produto



def atualizar_produto(produto: Produto):
     # Connectando no Banco de Dados
    db = get_db() 

    # Criando o Cursor
    cursor = db.cursor()

    # Script SQL
    sql = '''
        UPDATE produtos
        SET nome = ?, preco = ?, descricao = ?, quantidade = ?
        WHERE id = ?
    '''   

    parameters = (
        produto.nome,
        produto.preco,
        produto.descricao,
        produto.quantidade,
        produto.id

    )

    cursor.execute(sql, parameters)
    db.commit()

    cursor.close()
    db.close()


def listar_produtos_disponiveis():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT id, nome, preco, quantidade FROM produtos WHERE quantidade > 0")
    produtos = cursor.fetchall()
    cursor.close()
    db.close()
    return produtos