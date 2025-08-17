from db import get_db
from typing import Optional
from dataclasses import dataclass
from datetime import datetime, date
import cliente as cl
import produtos as prd

@dataclass
class Venda:
    cliente: str
    produto: str    
    qtd_venda: int
    preco_atual: float     
    preco_venda: float
    data_hora: datetime
    total: float
    id: Optional[int] = None


def listar_vendas():
    # Conectar ao banco
    db = get_db()
    cursor = db.cursor()

    sql = '''
        SELECT 
            v.id,
            c.nome as cliente,
            p.nome as produto,
            v.quantidade as qtd_venda,
            p.preco as preco_atual,
            v.preco_referencia as preco_venda,
            v.data_hora,
            v.total
        FROM vendas v
        INNER JOIN clientes c ON v.cliente_id = c.id
        INNER JOIN produtos p ON v.produto_id = p.id
        ORDER BY v.data_hora DESC
    '''
    
    cursor.execute(sql)
    rows = cursor.fetchall()

    cursor.close()
    db.close()

    # Transformar em lista de dicionários
    vendas = []
    for row in rows:
        vendas.append({
            "id": row[0],
            "cliente": row[1],
            "produto": row[2],
            "qtd_venda": row[3],
            "preco_atual": float(row[4]),
            "preco_venda": float(row[5]),
            "data_hora": row[6],
            "total": float(row[7])
        })

    return vendas




def criar_venda_interativa():
    # Listar clientes ativos
    clientes = cl.listar_clientes_ativos()
    if not clientes:
        print("Nenhum cliente ativo disponível.")
        return

    print("\n--- Clientes Ativos ---")
    for c in clientes:
        print(f"[{c[0]}] {c[1]} ({c[2]})")

    cliente_id = int(input("Digite o ID do cliente: "))

    # Listar produtos disponíveis
    produtos = prd.listar_produtos_disponiveis()
    if not produtos:
        print("Nenhum produto disponível em estoque.")
        return

    print("\n--- Produtos Disponíveis ---")
    for p in produtos:
        print(f"[{p[0]}] {p[1]} - R${p[2]:.2f} (Estoque: {p[3]})")

    produto_id = int(input("Digite o ID do produto: "))

    # Buscar dados do produto escolhido
    produto = next((p for p in produtos if p[0] == produto_id), None)
    if not produto:
        print("Produto inválido.")
        return

    qtd = int(input("Digite a quantidade que o cliente está comprando: "))

    if qtd <= 0 or qtd > produto[3]:
        print(f"Quantidade inválida. Estoque disponível: {produto[3]}")
        return

    preco_referencia = produto[2]
    total = qtd * preco_referencia

    # Inserir a venda
    db = get_db()
    cursor = db.cursor()
    sql = """
        INSERT INTO vendas (produto_id, cliente_id, quantidade, preco_referencia, data_hora, total)
        VALUES (?, ?, ?, ?, ?, ?) RETURNING id
    """
    parameters = (produto_id, cliente_id, qtd, preco_referencia, datetime.now(), total)

    cursor.execute(sql, parameters)
    venda_id = cursor.fetchone()[0]

    # Atualizar estoque do produto
    cursor.execute("UPDATE produtos SET quantidade = quantidade - ? WHERE id = ?", (qtd, produto_id))

    db.commit()
    cursor.close()
    db.close()

    print(f"\n Venda registrada com sucesso! ID da venda: {venda_id}")
    print(f"Cliente ID: {cliente_id}, Produto ID: {produto_id}, Quantidade: {qtd}, Total: R${total:.2f}")






def atualizar_venda():
    db = get_db()
    cursor = db.cursor()

    # --- Solicitar ID da venda ---
    venda_id = int(input("Digite o ID da venda que deseja atualizar: "))

    # Buscar a venda atual
    cursor.execute("""
        SELECT v.id, c.nome, p.nome, v.quantidade, v.preco_referencia, v.total, v.data_hora
        FROM vendas v
        JOIN clientes c ON v.cliente_id = c.id
        JOIN produtos p ON v.produto_id = p.id
        WHERE v.id = ?
    """, (venda_id,))
    venda_atual = cursor.fetchone()

    if not venda_atual:
        print("Venda não encontrada.")
        cursor.close()
        db.close()
        return

    print(f"\nVenda atual: ID={venda_atual[0]}, Cliente={venda_atual[1]}, Produto={venda_atual[2]}, "
          f"Qtd={venda_atual[3]}, Preço={venda_atual[4]}, Total={venda_atual[5]}, Data={venda_atual[6]}")

    # --- Solicitar novos dados ---
    cliente_id = int(input("Digite o novo ID do cliente: "))
    produto_id = int(input("Digite o novo ID do produto: "))
    qtd_venda = int(input("Digite a nova quantidade: "))
    preco_venda = float(input("Digite o novo preço de venda: "))
    data_hora = datetime.now()
    total = qtd_venda * preco_venda

    # --- Atualizar ---
    sql = '''
        UPDATE vendas
        SET cliente_id = ?,
            produto_id = ?,
            quantidade = ?,
            preco_referencia = ?,
            data_hora = ?,
            total = ?
        WHERE id = ?
    '''
    parameters = (
        cliente_id,
        produto_id,
        qtd_venda,
        preco_venda,
        data_hora,
        total,
        venda_id
    )

    cursor.execute(sql, parameters)
    db.commit()

    cursor.close()
    db.close()

    print(f"\n Venda {venda_id} atualizada com sucesso!")
    print(f"Novo Total: R${total:.2f}")
