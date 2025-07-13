funcionarios = []
class Funcionario ():
    def __init__ (self,nome:str,salario:float,cargo:str):
        self.nome =nome
        self.salario =salario
        self.cargo =cargo



class Empresa ():
     def __init__(self,funcionarios: list =[]):
         self.funcionarios=funcionarios

     def Listar_Funcionarios(funcionarios):
         return print(funcionarios)
     
     def Adicionar_Funcionario(funcionarios):
         nome =  input("Digite o nome do funcionário: ")
         salario = float(input("Digite o salário do funcionário: "))
         cargo = input("Digite o cargo do funcionário: ")
         novo_funcionario = Funcionario (nome, salario, cargo)
         funcionarios.append(novo_funcionario)



class Funcionario():
    def __init__(self, nome: str, salario: float, cargo: str):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def __str__(self):
        return f"Nome: {self.nome}, Salário: R${self.salario:.2f}, Cargo: {self.cargo}"


class Empresa():
    def __init__(self, funcionarios: list[Funcionario] = []):
        self.funcionarios = funcionarios

    def listar_funcionarios(self):
        print('Funcionários: ')
        for funcionario in self.funcionarios:
            print(f"{funcionario}")

    def adicionar_funcionario(self, funcionario: Funcionario):
        for funcionario_atual in self.funcionarios:
            if funcionario_atual.nome == funcionario.nome:
                raise ValueError("Funcionário já existe")
        
    def remover_funcionario(self,nome:str) -> bool:
        pass

empresa = Empresa()
funcionario1 = Funcionario('André',2500,'Técnico de TI')
empresa.adicionar_funcionario(funcionario1)
empresa.listar_funcionarios()
empresa.adicionar_funcionario(funcionario1)
empresa.listar_funcionarios()