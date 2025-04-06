alunos = []

while True:
    print("\n--- Sistema de Cadastro de Alunos ---")
    print("1. Cadastrar aluno")
    print("2. Visualizar alunos cadastrados")
    print("3. Calcular e mostrar a melhor média")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        # Cadastro de aluno
        continuar = 's'
        while continuar == 's':
            aluno = {}
            aluno['nome'] = input("Digite o nome do aluno: ")
            aluno['idade'] = int(input("Digite a idade do aluno: "))
            aluno['notas'] = (
                float(input("Digite a nota de Matemática: ")),
                float(input("Digite a nota de Ciências: ")),
                float(input("Digite a nota de História: "))
            )
            alunos.append(aluno)
            continuar = input("Deseja cadastrar outro aluno? (s/n): ").lower()
     
    
    elif opcao == '2':
        # Visualizar os alunos cadastrados
        if not alunos:
            print("Nenhum aluno cadastrado.")
        else:
            for aluno in alunos:
                print(f"\nNome: {aluno['nome']}")
                print(f"Idade: {aluno['idade']}")
                print(f"Notas: Matemática - {aluno['notas'][0]}, Ciências - {aluno['notas'][1]}, História - {aluno['notas'][2]}")
                media = sum(aluno['notas']) / len(aluno['notas'])
                print(f"Média: {media:.2f}")
    
    elif opcao == '3':
        # Calcular e mostrar o aluno com a melhor média
        if not alunos:
            print("Nenhum aluno cadastrado para calcular a média.")
        else:
            melhor_media = 0
            aluno_melhor_media = None
            for aluno in alunos:
                media = sum(aluno['notas']) / len(aluno['notas'])
                if media > melhor_media:
                    melhor_media = media
                    aluno_melhor_media = aluno
            if aluno_melhor_media:
                print("\nAluno com a melhor média:")
                print(f"Nome: {aluno_melhor_media['nome']}")
                print(f"Idade: {aluno_melhor_media['idade']}")
                print(f"Notas: Matemática - {aluno_melhor_media['notas'][0]}, Ciências - {aluno_melhor_media['notas'][1]}, História - {aluno_melhor_media['notas'][2]}")
                print(f"Média: {melhor_media:.2f}")
    
    elif opcao == '4':
        print("Saindo do sistema...")
        break
    
    else:
        print("Opção inválida! Tente novamente.")
