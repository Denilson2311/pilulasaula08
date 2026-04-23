def especialidade_top(consultas):
    cont = {}
    for consulta in consultas:
        esp = consulta['especialidade']
        if esp not in cont:
            cont[esp] = 0
        cont[esp] += 1
    maior = ''
    max_valor = -1
    for e in cont:
        if cont[e] > max_valor:
            max_valor = cont[e]
            maior = e
    return maior

def main():
    consultas = [
        {'paciente':'Ana'      , 'especialidade': 'Cardiologia'},
        {'paciente':'Carlos'   , 'especialidade': 'Ortopedia'  },
        {'paciente':'Carlos'   , 'especialidade': 'Ortopedia'  },
        {'paciente':'Carlos'   , 'especialidade': 'Ortopedia'  },
        {'paciente':'Carlos'   , 'especialidade': 'Ortopedia'  },
        {'paciente':'Betariz'  , 'especialidade': 'Cardiologia'},
        {'paciente':'João'     , 'especialidade': 'Cardiologia'}
    ]
    resultado = especialidade_top(consultas)
    print(f'Especilidade mais frequente: {resultado}')
    
main()