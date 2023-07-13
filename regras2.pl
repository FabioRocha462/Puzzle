% Operações para movimentar peças
move([X, 0, Y, Z | Tail], [0, X, Y, Z | Tail]).
move([X1, X2, X3, X4 | Tail], [X1, X2, X3, X4 | NewTail]) :- move([X2, X1, X3, X4 | Tail], NewTail).

move([X, Y, 0, Z | Tail], [X, Y, Z, 0 | Tail]).
move([X1, X2, X3, X4 | Tail], [X1, X2, X3, X4 | NewTail]) :- move([X1, X2, X3, X4 | Tail], NewTail).

move([X1, 0, X2, X3 | Tail], [X1, X2, 0, X3 | Tail]).
move([X1, X2, X3, X4 | Tail], [X1, X2, X3, X4 | NewTail]) :- move([X1, X2, X3, X4 | Tail], NewTail).

move([0, X, Y, Z | Tail], [X, 0, Y, Z | Tail]).
move([X1, X2, X3, X4 | Tail], [X1, X2, X3, X4 | NewTail]) :- move([X1, X2, X3, X4 | Tail], NewTail).

% Regra para verificar se o estado atual é o objetivo
goal_state(State) :- State = [1, 2, 3, 8, 0, 4, 7, 6, 5].

% Função para calcular a distância de Manhattan entre duas posições
manhattan_distance(Pos1, Pos2, Distance) :- nth1(Index1, Pos1, Value), nth1(Index2, Pos2, Value), Distance is abs(Index1 - Index2) // 3 + abs(Index1 - Index2) mod 3.

% Função para calcular a heurística do estado
heuristic(State, Heuristic) :- goal_state(Goal),findall(Distance, (nth1(Index, State, Value), nth1(Index, Goal, GoalValue), manhattan_distance(Value, GoalValue, Distance)), Distances),sum_list(Distances, Heuristic).

% Função auxiliar para realizar uma busca em largura aprimorada (IDA*)
ida_star(State, _, [], 0) :- goal_state(State).
ida_star(State, Bound, [Move | Path], NewBound) :- Bound > 0, move(State, NewState),heuristic(NewState, Heuristic),Heuristic =< Bound,NewBound is Heuristic,ida_star(NewState, Bound, Path, _),Move = NewState.
ida_star(State, Bound, Path, NewBound) :-heuristic(State, Heuristic),NewBound is Heuristic,ida_star(State, NewBound, Path, _).

% Função para resolver o Eight Puzzle utilizando o algoritmo IDA*
solve_ida_star(State, Solution) :- heuristic(State, Heuristic), ida_star(State, Heuristic, Solution, _).

% Exemplo de uso:
% Defina aqui o estado inicial do quebra-cabeça
% initial_state([1, 2, 3, 8, 0, 4, 7, 6, 5]).
% Resolva o quebra-cabeça usando o algoritmo IDA*
% solve_ida_star(initial_state(State), Solution).
