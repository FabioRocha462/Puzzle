from pyswip import Prolog

def solve_slider_puzzle(initial_state, goal_state):
    prolog = Prolog()
    prolog.consult("regras.pl")  # Carrega as regras Prolog

    # Converte o estado inicial e o estado objetivo em uma lista de Prolog
    initial_state_list = list(initial_state)
    goal_state_list = list(goal_state)
    prolog.assertz("initial_state({})".format(initial_state_list))
    prolog.assertz("goal_state({})".format(goal_state_list))

    # Encontra a solução usando Prolog
    solutions = list(prolog.query("solve(Solution)"))

    # Retorna a solução encontrada
    if solutions:
        return solutions[0]["Solution"]
    else:
        return None

# Exemplo de uso
initial_state = [2, 1, 3, 4, 5, 6, 7, 8, '']
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, '']
solution = solve_slider_puzzle(initial_state, goal_state)

if solution:
    print("Solução encontrada:")
    for step in solution:
        print(step)
else:
    print("Não foi possível encontrar uma solução.")
