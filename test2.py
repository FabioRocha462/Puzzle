from pyswip import Prolog

# Inicialize o objeto Prolog
prolog = Prolog()

# Carregue o arquivo Prolog
prolog.consult("regras2.pl")

# Defina o estado inicial do quebra-cabeça
prolog.assertz("initial_state([1, 2, 3, 4, 5, 6, 7, 0, 8])")

# Execute a consulta para obter a solução
solutions = list(prolog.query("solve_ida_star(initial_state(State), Solution)"))
for i in range(1000):
    print(i)
# Extraia a solução
if solutions:
    solution = solutions[0]["Solution"]
    print("Solução encontrada:")
    print(solution)
else:
    print("Nenhuma solução encontrada.")
