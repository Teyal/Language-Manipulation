class automato:
    """# colocar entrada?"""
    def __init__(self, estados, inicial, finais, transicoes):
        self.estados = estados
        self.inicial = inicial
        self.finais = finais
        self.transicoes = transicoes
        """self.validar"""

    def testar_entrada(self, entrada):
        estado = self.inicial
        for i in entrada:
            estado = self._proximo_estado(estado, i)
        if estado in self.finais:
            print("Entrada válida")
            return True
        else:
            print("Entrada inválida")
            return False

    def _proximo_estado(self, estado, entrada):
        if entrada in self.transicoes[estado]:
            return self.transicoes[estado][entrada]
        else:
            print("transição inválida, estado morto alcançado")
            return "q-1"
