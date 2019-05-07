from automato import automato
af = automato(
    estados={'q0', 'q1', 'q2'},
    inicial='q0',    finais={'q1'},
    transicoes={
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q0', '1': 'q2'},
        'q2': {'0': 'q2', '1': 'q1'}
    })
print(af.transicoes)
af.testar_entrada('1')
