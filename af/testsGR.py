from gramatica import gramatica

gr = gramatica(regras={
    "S": [
        ["a", "A0"],
        ["b", "A2"],
        ["ab"]
    ],
    "A0": [
        ["a", "A1"],
        ["b", "A0"]
    ],
    "A1": [
        ["a"],
        ["b", "A1"],
        ["a", "A2"]
    ],
    "A2": [
        ["a", "A0"],
        ["b", "A2"]
    ]
}, terminais=['a', 'b'])

gr.gerar_aleatorio("S")

# print(gr.gerar_aleatorio())
"""aa = gr.gerador()
print(aa)"""
