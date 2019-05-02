import random as rd


class gramatica:

    """infere-se que os simbolos nao terminais sao os nao listados nos terminais
    e que a variável inicial é S"""
    def __init__(self, regras, terminais):
        self.regras = regras
        self.terminais = terminais

    def gerar_aleatorio(self, linguagem):
        resul = self._gerador_aleatorio("S")
        print(''.join(resul))

    def _gerador_aleatorio(self, linguagem):
        resultado = []
        for i in linguagem:
            if i in self.regras:
                substring = rd.choice(self.regras[i])
                resultado.append(''.join(self._gerador_aleatorio(substring)))
            else:
                resultado.append(i)
        return resultado
