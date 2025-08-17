import cliente as cl
from datetime import datetime

def gerenciador_clientes():
    while True:
        print('='*30)
        print('Gerenciador da Loja'.center(30))
        print('='*30)

        print('[1] Buscar Clientes')
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
            
            cliente_atualizado = ()
            cliente_atualizado = cl.Cliente(nome,email,data_nascimento, fl_ativo,id)
            cl.atualizar_cliente(cliente_atualizado)
            print('Cliente atualizado com sucesso.')

        elif opcao == '4':
            id = input('Digite o ID do cliente que deseja desativar: ')
            fl_ativo = input('Cliente ativo (S/N):') == 'S'

           
            cl.desativar_cliente(id)


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
        pass
    if opcao == '3':
        pass
    if opcao == '4':
        pass