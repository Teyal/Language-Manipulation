class afnd:
    """# colocar entrada?"""
    def __init__(self, estados, inicial, finais, transicoes):
        self.estados = estados
        self.inicial = inicial
        self.finais = finais
        self.transicoes = transicoes
        """self.validar"""

    def testar_entrada(self, entrada):
        estado = self.inicial
        print(entrada)
        for i in entrada:
            # print(i)
            estado = self._proximo_estado(estado, i)

        if estado in self.finais:
            print("Entrada válida")
            return True
        else:
            # print(estado)
            print("Entrada inválida")
            return False

    def _proximo_estado(self, estado, entrada):
        if entrada in self.transicoes[estado]:
            print("{}, {}".format(estado, entrada))
            return self.transicoes[estado][entrada]
        else:
            print("transição inválida, estado morto alcançado")
            return "q-1"

    def fechamento_lambda(self, inicial):
        lista = []
        lista.append(inicial)
        retorno = set()

        while lista:
            estado = lista.pop()
            if estado not in retorno:
                retorno.add(estado)
                if '' in self.transicoes[estado]:
                    lista.extend(self.transicoes[estado][''])

        return retorno
