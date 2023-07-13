from pyswip import Prolog
import random

prolog = Prolog()
prolog.consult("regras.pl") 

def solve_eight_puzzle(initial_state):
    # Converte o estado inicial em uma lista de Prolog
    initial_state_list = list(initial_state)
    prolog.assertz("initial_state({})".format(initial_state_list))

    # Encontra a solução usando Prolog
    solutions = list(prolog.query("solve(Solution)."))

    # Retorna a solução encontrada
    if solutions:
        return solutions[0]["Solution"]
    else:
        return None

initial_state = [1, 2, 3, 4, 5, 6, 7, 8,0]

# Embaralha o estado inicial
random.shuffle(initial_state)

# Encontra a solução
solution = solve_eight_puzzle(initial_state)

# Verifica se há uma solução
if solution:
    print("Solução encontrada:")
    for step in solution:
        print(step)
else:
    print("Não foi possível encontrar uma solução.")
