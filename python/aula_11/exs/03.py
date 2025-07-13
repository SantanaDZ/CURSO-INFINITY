class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"Nome: {self.nome}, Cargo: {self.cargo}, Salário: R$ {self.salario:.2f}"
    
class Empresa:
    def __init__(self, nome_empresa):
        self.nome_empresa = nome_empresa
        self.funcionarios = []

    def adicionar_funcionario(self, nome, cargo, salario):
        novo_funcionario = Funcionario(nome, cargo, salario)
        self.funcionarios.append(novo_funcionario)
        print(f"✅ Funcionário '{nome}' adicionado com sucesso!")

    def remover_funcionario(self, nome):
        for f in self.funcionarios:
            if f.nome == nome:
                self.funcionarios.remove(f)
                print(f"🗑️ Funcionário '{nome}' removido com sucesso.")
                return
        print(f"⚠️ Funcionário '{nome}' não encontrado.")

    def listar_funcionarios(self):
        if not self.funcionarios:
            print("📭 Nenhum funcionário cadastrado.")
        else:
            print(f"👥 Lista de funcionários da empresa '{self.nome_empresa}':")
            for f in self.funcionarios:
                print("-", f)

