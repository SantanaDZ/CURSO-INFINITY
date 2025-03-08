usuario_correto = 'andre'
senha_correta = 'andre2025'
tentativas = 3
while tentativas > 0:
    usuario_digitado = input('Digite o nome de usuário: ')
    senha_digitada = input('Digite a senha: ')
    if senha_digitada == senha_correta and usuario_digitado == usuario_correto:
        print('Bem vindo!')
        break
    else:
        tentativas -= 1
        if tentativas > 0:
            print(f"Credenciais incorretas. Você tem {tentativas} tentativa(s) restante(s).")
        else:
            for i in range(3):
                print("Acesso bloqueado")
    
