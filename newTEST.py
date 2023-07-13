from pyswip import Prolog
import random

prolog = Prolog()
prolog.consult("newsroles.pl")

solutions = prolog.query("test(Plan).")

for step in solutions:
    print(step)