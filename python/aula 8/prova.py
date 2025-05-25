class Funcionarios():
        def __init__(self, nome, funcao, salario):
            self.nome = nome
            self.funcao = funcao
            self.salario = salario    

class Quarto():
        def __init__(self, numero, preco_diaria):
            self.numero = numero
            self.preco_diaria = preco_diaria
            self.status = 'disponível' # ou 'ocupado'

class Reserva():
        def __init__(self, nome_hospede, dias_estadia, quarto: Quarto):
            self.nome_hospede = nome_hospede
            self.dias_estadia = dias_estadia
            self.quarto = quarto                
        
        def calcular_total(self):
         return self.dias_estadia * self.quarto.preco_diaria     
                   
class Hotel():
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = [] 
        self.reservas = []
        self.quartos = []

    # Gerenciamento de funcionários
    def adicionar_funcionario(self, nome, funcao, salario):
        funcionario = Funcionarios(nome, funcao, salario)
        self.funcionarios.append(funcionario)    

     # Gerenciamento de quartos
    def adicionar_quarto(self, numero, preco_diaria):
        quarto = Quarto(numero, preco_diaria)
        self.quartos.append(quarto)

    def listar_quartos_disponiveis(self):
        return [q for q in self.quartos if q.status == "disponível"]    
    
     # Gerenciamento de reservas
    def fazer_reserva(self, nome_hospede, dias_estadia, numero_quarto):
        quarto = next((q for q in self.quartos if q.numero == numero_quarto and q.status == "disponível"), None)
        
        if not quarto:
            print(f"O quarto {numero_quarto} não está disponível.")
            return None

        quarto.status = "ocupado"
        reserva = Reserva(nome_hospede, dias_estadia, quarto)
        self.reservas.append(reserva)
        print(f"Reserva feita com sucesso para {nome_hospede} no quarto {quarto.numero}.")
        return reserva

    def encerrar_reserva(self, nome_hospede):
        for reserva in self.reservas:
            if reserva.nome_hospede == nome_hospede:
                total = reserva.calcular_total()
                reserva.quarto.status = "disponível"
                self.reservas.remove(reserva)
                print(f"Reserva encerrada. Total a pagar: R${total:.2f}")
                return total
        print("Reserva não encontrada.")
        return None
    

hotel = Hotel("Hotel Infinty")

# Adicionando funcionários
hotel.adicionar_funcionario("Ana", "Gerente", 5000)
hotel.adicionar_funcionario("Carlos", "Recepcionista", 2500)

# Adicionando quartos
hotel.adicionar_quarto(101, 200)
hotel.adicionar_quarto(102, 250)

# Fazendo uma reserva
hotel.fazer_reserva("André Santana", 3, 101)

# Encerrando uma reserva
hotel.encerrar_reserva("André Santana")   