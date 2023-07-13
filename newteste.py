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

print("--------------------------------")

responses = prolog.query("ancestral(pedro,X).")

for response in responses:

    print(response)

print("--------------------------------")

responses = prolog.query("avo(X,mariana).")

for response in responses:
    print(response)

print("--------------------------------")

responses = prolog.query("irmao(Y,izabel).")

for response in responses:
    print(response)


print("--------------------------------")

responses = prolog.query("pai(X,andre).")

for response in responses:
    print(response)

print("--------------------------------")

responses = prolog.query("ancestral(X,andre).")

for response in responses:
    print(response)

print("--------------------------------")

responses = prolog.query("tio(Y,luiz).")

for response in responses:
    print(response)