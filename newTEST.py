from pyswip import Prolog
import random

prolog = Prolog()
prolog.consult("newsroles.pl")

solutions = prolog.query("write_sol([]).")

for step in solutions:
    print(step)