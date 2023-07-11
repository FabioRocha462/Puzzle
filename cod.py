cod = "breadth_first_search([[State|Path]|RestQueue],Visited,Solution):-\+ goal_state(State),\+ member(State,Visited),generate_moves(State,Moves),append(RestQueue, NewQueue, [[State|Path]|RestQueue]),add_to_visited(Moves, State, Visited, NewVisited),breadth_first_search(NewQueue, NewVisited, Solution)."
parte = cod[50:70]
print(parte)