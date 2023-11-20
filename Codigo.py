class Carro:
    def __init__(self):
        self.modelo = ""
        self.cor = ""
        self.motor = ""
        self.transmissao = ""
        self.entretenimento = ""

class CarroBuilder:
    def __init__(self):
        self.carro = Carro()

    def construir_modelo(self):
        pass

    def construir_cor(self):
        pass

    def construir_motor(self):
        pass

    def construir_transmissao(self):
        pass

    def construir_entretenimento(self):
        pass

    def obter_carro(self):
        return self.carro

class CarroLuxoBuilder(CarroBuilder):
    def construir_modelo(self):
        self.carro.modelo = "Carro de Coleção"

    def construir_cor(self):
        self.carro.cor = "Vermelho Fosco"

    def construir_motor(self):
        self.carro.motor = "Motor de Foguete"

    def construir_transmissao(self):
        self.carro.transmissao = "Manual"

    def construir_entretenimento(self):
        self.carro.entretenimento = "Sistema de Som Intermediário"

class Diretor:
    def construir_carro(self, builder):
        builder.construir_modelo()
        builder.construir_cor()
        builder.construir_motor()
        builder.construir_transmissao()
        builder.construir_entretenimento()

def exibir_carro(carro):
    print(f"Modelo: {carro.modelo}")
    print(f"Cor: {carro.cor}")
    print(f"Motor: {carro.motor}")
    print(f"Transmissão: {carro.transmissao}")
    print(f"Entretenimento: {carro.entretenimento}")


builder_luxo = CarroLuxoBuilder()
diretor = Diretor()
diretor.construir_carro(builder_luxo)
carro_luxo = builder_luxo.obter_carro()

exibir_carro(carro_luxo)
