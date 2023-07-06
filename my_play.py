import random
import pytholog as pl
new_kb = pl.KnowledgeBase()
new_kb([
    ":- use_module(library(lists))",
    "move([X, '', Y, Z | Tail], [ '', X, Y, Z | Tail])",
    "move([X1, X2, X3, X4 | Tail], [X1, X2, X3, X4 | NewTail]) :-move([X2, X1, X3, X4 | Tail], NewTail)",
    "move([X, Y, '', Z | Tail], [X, Y, Z, '' | Tail])",
    "move([X1, X2, X3, X4 | Tail], [X1, X2, X3, X4 | NewTail]) :-move([X1, X2, X3, X4 | Tail], NewTail)",
    "move([X1, '', X2, X3 | Tail], [X1, X2, '', X3 | Tail])",
    "move([X1, X2, X3, X4 | Tail], [X1, X2, X3, X4 | NewTail]) :-move([X1, X2, X3, X4 | Tail], NewTail)",
    "move(['', X, Y, Z | Tail], [X, '', Y, Z | Tail])",
    "move([X1, X2, X3, X4 | Tail], [X1, X2, X3, X4 | NewTail]) :-move([X1, X2, X3, X4 | Tail], NewTail)",
    "goal_state(State) :- State = [1, 2, 3, 4, 5, 6, 7, 8, '']",
    "generate_moves(State, Moves) :-findall(NewState, move(State, NewState), Moves)",
    "apply_move(State, Move, NewState) :- move(State, NewState), goal_state(Move)",
    "breadth_first_search([[State|Path]|_], _, [State|Path]) :-goal_state(State)",
    "breadth_first_search([[State|Path]|RestQueue], Visited, Solution) :- goal_state(State),\+ member(State, Visited),generate_moves(State, Moves), append(RestQueue, NewQueue, [[State|Path]|RestQueue]), add_to_visited(Moves, State, Visited, NewVisited), breadth_first_search(NewQueue, NewVisited, Solution)",
    "add_to_visited([], _, Visited, Visited)",
    "add_to_visited([Move|Moves], State, Visited, NewVisited) :-\+ member(Move, Visited)",
    "add_to_visited(Moves, State, [Move|Visited], NewVisited)",
    "add_to_visited([_|Moves], State, Visited, NewVisited) :-add_to_visited(Moves, State, Visited, NewVisited)",
    "solve(Solution) :-initial_state(InitialState),breadth_first_search([[InitialState]], [], Solution)"
])
def numbers():
    numbers = list(range(9))  # Cria uma lista de números de 0 a 8
    random.shuffle(numbers)
    return numbers  # Embaralha os números aleatoriamente

initial_state = numbers()

def solve_eight_puzzle(initial_state):
    # Converte o estado inicial em uma lista de Prolog
    initial_state_list = list(initial_state)
    new_kb.assertz("initial_state({})".format(initial_state_list))

    # Encontra a solução usando Prolog
    solutions = list(new_kb.query("solve(Solution)"))

    # Retorna a solução encontrada
    if solutions:
        return solutions[0]["Solution"]
    else:
        return None


solution = solve_eight_puzzle(initial_state)

if solution:
    print("Solução encontrada:")
    for step in solution:
        print(step)
else:
    print("Não foi possível encontrar uma solução.")

