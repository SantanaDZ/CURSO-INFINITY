from datetime import datetime, date
from db import get_db


def Buscar_clientes():
    # Conectando no Banco de Dados
    db = get_db()

    # Criando o Cursor
    cursor = db.cursor()

   
    # Script SQL
    sql = '''
        SELECT id , nome, email, data_nascimento, fl_ativo
        FROM clientes
        

    '''

    cursor.execute(sql)  
    clientes = cursor.fetchall()
    cursor.close()
    return clientes




def Criar_cliente(nome: str, email: str, data_nascimento: date, fl_ativo: bool = True):



# Conectando no Banco de Dados
    db = get_db()

    # Criando o Cursor
    cursor = db.cursor()

   
    # Script SQL
    sql = '''
        INSERT INTO clientes (nome, email, data_nascimento,fl_ativo)
        VALUES (?, ?, ?, ?)

    '''

    cursor.execute(sql,(nome,email,data_nascimento.isoformat(), fl_ativo))
    db.commit()

    cursor.close()

# nome = input('Digite o nome do cliente: ')
# email = input('Digite o email do cliente: ')
# data_nascimento = input('Digite data de nascimento do cliente: ')
# data_nascimento = datetime.strptime(data_nascimento,'%Y-%m-%d').date()

# Criar_cliente(nome,email,data_nascimento)

clientes = Buscar_clientes()
print (clientes)