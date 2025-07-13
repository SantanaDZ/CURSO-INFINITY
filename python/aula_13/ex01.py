class Funcionario:
    def __init__(self, nome:str,cpf:str,salario_bruto:float):
        self.nome = nome
        self.cpf = cpf
        self.salario_bruto = salario_bruto

    def Calcular_salario_liquido(self):
        self.salario_liquido = self.salario_bruto -(self.salario_bruto * 0.03)
        return self.salario_liquido

    def __str__(self):
        return f'Funcionário: {self.nome}  \n CPF: {self.cpf} \n Salário Bruto: {self.salario_bruto}  \n Salário Líquido: {self.Calcular_salario_liquido()}\n'

class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario_bruto, setor:str):
        super().__init__(nome, cpf, salario_bruto)
        self.setor = setor      
    def Calcular_salario_liquido(self):
        self.salario_liquido = self.salario_bruto -(self.salario_bruto * 0.07)
        return self.salario_liquido
    def __str__(self):
         return f'Gerente: {self.nome} \n CPF: {self.cpf}  \n Salário Bruto: {self.salario_bruto}  \n Salário Líquido: {self.Calcular_salario_liquido()}  \n Gerência: {self.setor}\n'     

empregado1 = Funcionario('João','134.648.559', 3000)
empregado2 = Gerente('Pedro','156.780.305', 5000, 'Compras')              
print(empregado1)
print(empregado2)