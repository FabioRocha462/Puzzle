:- use_module(library(lists)).

% Operações para movimentar as peças
move([X, '', Y, Z | Tail], [ '', X, Y, Z | Tail]).
move([X1, X2, X3, X4 | Tail], [X1, X2, X3, X4 | NewTail]) :-move([X2, X1, X3, X4 | Tail], NewTail).

move([X, Y, '', Z | Tail], [X, Y, Z, '' | Tail]).
move([X1, X2, X3, X4 | Tail], [X1, X2, X3, X4 | NewTail]) :-move([X1, X2, X3, X4 | Tail], NewTail).

move([X1, '', X2, X3 | Tail], [X1, X2, '', X3 | Tail]).
move([X1, X2, X3, X4 | Tail], [X1, X2, X3, X4 | NewTail]) :- move([X1, X2, X3, X4 | Tail], NewTail).

move(['', X, Y, Z | Tail], [X, '', Y, Z | Tail]).
move([X1, X2, X3, X4 | Tail], [X1, X2, X3, X4 | NewTail]) :- move([X1, X2, X3, X4 | Tail], NewTail).

% Regra para verificar se o estado atual é o objetivo
goal_state(State) :- State = [1, 2, 3, 4, 5, 6, 7, 8, ''].

% Regra para gerar movimentos possíveis
generate_moves(State, Moves) :-findall(NewState, move(State, NewState), Moves).

% Regra para aplicar um movimento a um estado
apply_move(State, Move, NewState) :- move(State, NewState), goal_state(Move).

% Regra para buscar a solução utilizando busca em largura
breadth_first_search([[State|Path]|_], _, [State|Path]) :-goal_state(State).
breadth_first_search([[State|Path]|RestQueue], Visited, Solution):-  goal_state(State), member(State, Visited),generate_moves(State, Moves),append(RestQueue, NewQueue, [[State|Path]|RestQueue]),add_to_visited(Moves, State, Visited, NewVisited),breadth_first_search(NewQueue, NewVisited, Solution).

% Regra auxiliar para adicionar novos estados à lista de visitados
add_to_visited([], _, Visited, Visited).
add_to_visited([Move|Moves], State, Visited, NewVisited) :- member(Move, Visited),add_to_visited(Moves, State, [Move|Visited], NewVisited).
add_to_visited([_|Moves], State, Visited, NewVisited) :-add_to_visited(Moves, State, Visited, NewVisited).

% Regra para resolver o Eight Puzzle
solve(Solution) :-initial_state(InitialState),breadth_first_search([[InitialState]], [], Solution).


