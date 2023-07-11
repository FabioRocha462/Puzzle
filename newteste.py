from pyswip import Prolog

prolog = Prolog()
prolog.consult("prolog.pl")

responses = prolog.query("progenitor(X,joao)")

# for response in responses:

#     print(response)

responses = prolog.query("avo(maria,X).")

# for response in responses:

#     print(response)

responses = prolog.query("ancestral(X,joana).")

for response in responses:

    print(response)

response = prolog.query("mulher(ana).")