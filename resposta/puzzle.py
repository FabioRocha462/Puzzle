from pyswip import Prolog

prolog = Prolog()
prolog.consult("quebracabeca.pl")

solution = prolog.query("ids.")

for step in solution:

    print(step)