from dataclasses import dataclass


@dataclass
class Imposto:
    valor : float
    
    def calcular(self,valor:float):
        return 0

class DAS(Imposto):
    
    
    def calcular(self, valor:float):
        return valor * 0.06
    
class ISS(Imposto):
    
    
    def calcular(self, valor:float):
        return valor * 0.05

class IRPJ(Imposto):
    
    
    def calcular(self, valor:float):
        return valor * 0.1


def calcularImposto(valor_bruto:float,impostos:list[Imposto]):
    valor_bruto = 8000
    valor_liquido = calcularImposto(valor_bruto,impostos)
    print(valor_liquido)


calcularImposto()