# Sistema de Gerenciamento de Biblioteca

biblioteca = []
emprestimos = {}  # chave: nome do usuário, valor: lista de títulos

def adicionar_livro():
    titulo = input("Título do livro: ").strip()
    autor = input("Autor do livro: ").strip()
    try:
        copias = int(input("Número de cópias: "))
    except ValueError:
        print("Número inválido.")
        return

    for livro in biblioteca:
        if livro["titulo"].lower() == titulo.lower():
            print("Este livro já existe na biblioteca. Atualizando cópias...")
            livro["copias"] += copias
            return

    biblioteca.append({
        "titulo": titulo,
        "autor": autor,
        "copias": copias
    })
    print("Livro adicionado com sucesso!")

def listar_livros():
    if not biblioteca:
        print("Nenhum livro na biblioteca.")
        return
    print("\n--- LIVROS DISPONÍVEIS ---")
    for livro in biblioteca:
        print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Cópias: {livro['copias']}")

def emprestar_livro():
    usuario = input("Nome do usuário: ").strip()
    titulo = input("Título do livro a emprestar: ").strip()

    for livro in biblioteca:
        if livro["titulo"].lower() == titulo.lower():
            if livro["copias"] > 0:
                livro["copias"] -= 1
                emprestimos.setdefault(usuario, []).append(livro["titulo"])
                print(f"Livro '{livro['titulo']}' emprestado para {usuario}.")
                return
            else:
                print("Não há cópias disponíveis.")
                return
    print("Livro não encontrado.")

def devolver_livro():
    usuario = input("Nome do usuário: ").strip()
    titulo = input("Título do livro a devolver: ").strip()

    if usuario not in emprestimos or titulo not in emprestimos[usuario]:
        print("Este livro não foi emprestado por esse usuário.")
        return

    for livro in biblioteca:
        if livro["titulo"].lower() == titulo.lower():
            livro["copias"] += 1
            emprestimos[usuario].remove(titulo)
            if not emprestimos[usuario]:
                del emprestimos[usuario]  # limpa se não houver mais empréstimos
            print(f"Livro '{titulo}' devolvido por {usuario}.")
            return
    print("Livro não encontrado na biblioteca.")

def verificar_disponibilidade():
    titulo = input("Digite o título do livro: ").strip()
    for livro in biblioteca:
        if livro["titulo"].lower() == titulo.lower():
            if livro["copias"] > 0:
                print(f"'{livro['titulo']}' está disponível com {livro['copias']} cópias.")
            else:
                print(f"'{livro['titulo']}' está indisponível.")
            return
    print("Livro não encontrado.")

def listar_livros_usuario():
    usuario = input("Nome do usuário: ").strip()
    if usuario in emprestimos:
        print(f"Livros emprestados para {usuario}:")
        for titulo in emprestimos[usuario]:
            print(f"- {titulo}")
    else:
        print(f"{usuario} não possui livros emprestados.")

def menu():
    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Emprestar Livro")
        print("4. Devolver Livro")
        print("5. Verificar Disponibilidade")
        print("6. Mostrar Livros Emprestados por Usuário")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_livro()
        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            emprestar_livro()
        elif opcao == "4":
            devolver_livro()
        elif opcao == "5":
            verificar_disponibilidade()
        elif opcao == "6":
            listar_livros_usuario()
        elif opcao == "7":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida.")

# Iniciar o programa
menu()
