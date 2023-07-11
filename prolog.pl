progenitor(maria,joao).
progenitor(pedro,joao).
progenitor(pedro,luiz).
progenitor(helena,luiz).
progenitor(joao,jose).
progenitor(ana,jose).
progenitor(jose,joana).
progenitor(raquel,joana).

homem(pedro).
homem(joao).
homem(jose).
homem(luiz).

mulher(maria).
mulher(ana).
mulher(joana).
mulher(helena).

avo(X,Y):- progenitor(X,Z),progenitor(Z,Y).

ancestral(X,Y):- progenitor(X,Y).
ancestral(X,Y):- progenitor(X,Z), ancestral(Z,Y).
