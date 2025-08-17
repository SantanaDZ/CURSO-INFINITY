import cliente as cl
from datetime import datetime
import produtos as prd
import vendas as vd

# Gerenciador dos Clientes:


def gerenciador_clientes():
    while True:
        print('='*30)
        print('Gerenciador de Clientes'.center(30))
        print('='*30)

        print('[1] Listar Clientes')
        print('[2] Cadastrar Cliente')
        print('[3] Atualizar Cliente')
        print('[4] Desativar Cliente')
        print('[5] Voltar')

        opcao = input('> ')

        if opcao == '1':
            clientes = cl.buscar_clientes()
            print('Clientes: ')
            for cliente in clientes:
                print(f'[{cliente.id}] - {cliente.nome}')

        elif opcao == '2':
            nome = input('Digite o nome do cliente: ')
            email = input('Digite o email do cliente: ')
            data_nascimento = input('Digite a data de nascimento do cliente (YYYY-MM-DD): ')
            data_nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d').date()

            cliente = cl.buscar_cliente_pelo_email(email)

            if cliente is None:
                cliente = cl.Cliente(nome, email, data_nascimento)
                cliente = cl.criar_cliente(cliente)
                print('Cliente cadastrado com sucesso.')
            else: 
                print('Já existe um cliente com esse email.')


        elif opcao == '3':
            id = input('Digite o ID do cliente que deseja atualizar: ')
            nome = input('Digite o nome do cliente: ')
            email = input('Digite o email do cliente: ')
            data_nascimento = input('Digite a data de nascimento do cliente (YYYY-MM-DD): ')
            data_nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d').date()
            fl_ativo = input('Cliente ativo (S/N):') == 'S'
            
            
            cliente_atualizado = cl.Cliente(nome,email,data_nascimento, fl_ativo,id)
            cl.atualizar_cliente(cliente_atualizado)
            print('Cliente atualizado com sucesso.')

        elif opcao == '4':
            id = input('Digite o ID do cliente que deseja desativar: ')
            fl_ativo = input('Cliente ativo (S/N):') == 'S'           
            cl.desativar_cliente(id)
            print('Cliente desativado com sucesso.')

        elif opcao == '5':
            break


# Gerenciador de Produtos:

def gerenciador_produtos():
    while True:
        print('='*30)
        print('Gerenciador de Produtos'.center(30))
        print('='*30)

        print('[1] Listar Produtos')
        print('[2] Cadastrar Produtos')
        print('[3] Atualizar Produtos')        
        print('[4] Voltar')

        opcao = input('> ')

        if opcao == '1':
            produtos = prd.buscar_produtos()
            print('Produtos: ')
            for produto in produtos:
                print(f'[{produto.id}] - {produto.nome}')

        if opcao =='2':
            nome= input('Digite o nome do produto: ')
            preco= input('Digite o preço do produto: ')
            descricao= input('Digite a descrição do produto: ')
            quantidade= input('Digite a quantidade do produto: ')

            produto = prd.Produto(nome,preco,descricao,quantidade)
            prd.criar_produto(produto)
            print('Produto cadastrado com sucesso.')

        if opcao =='3':
            id = input('Digite o ID do produto para atualizar: ')
            nome= input('Digite o nome do produto: ')
            preco= input('Digite o preço do produto: ')
            descricao= input('Digite a descrição do produto: ')
            quantidade= input('Digite a quantidade do produto: ')

            produto_atualizado = prd.Produto(nome,preco,descricao,quantidade,id)   
            prd.atualizar_produto(produto_atualizado)
            print('Produto Atualizado com sucesso.')

        if opcao =='4':
            break

# Gerenciador das Vendas:

    # cliente: str
    # produto: str    
    # qtd_venda: int
    # preco_atual: float     
    # preco_venda: float
    # data_hora: datetime
    # total: float

def gerenciador_vendas():
    while True:
        print('='*30)
        print('Gerenciador de Vendas'.center(30))
        print('='*30)

        print('[1] Listar Vendas')
        print('[2] Cadastrar Vendas')
        print('[3] Atualizar Vendas')        
        print('[4] Voltar')

        opcao = input('> ')

        if opcao == '1':
            vendas = vd.listar_vendas()
            print('Vendas: ')
            for v in vendas:
                print(f"Venda {v['id']} | Cliente: {v['cliente']} | Produto: {v['produto']} | "
                    f"Qtd: {v['qtd_venda']} | Preço Atual: {v['preco_atual']:.2f} | "
                    f"Preço Venda: {v['preco_venda']:.2f} | Total: {v['total']:.2f} | Data: {v['data_hora']}")

        if opcao == '2':
            vd.criar_venda_interativa()

        if opcao == '3':
            vd.atualizar_venda()    

        if opcao == '4':
            break




# Menu Principal:


while True:
    print('='*30)
    print('Gerenciador da Loja'.center(30))
    print('='*30)

    print('[1] Gerenciar Clientes')
    print('[2] Gerenciar Produtos')                                       
    print('[3] Gerenciar Vendas')
    print('[4] Sair')

    opcao = input('> ')
    if opcao == '1':
        gerenciador_clientes()
    if opcao == '2':
        gerenciador_produtos()
    if opcao == '3':
        gerenciador_vendas()
    if opcao == '4':
        break