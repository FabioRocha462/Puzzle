progenitor(maria,joao).
progenitor(pedro,joao).
progenitor(pedro,luiz).
progenitor(helena,luiz).
progenitor(joao,jose).
progenitor(ana,jose).
progenitor(jose,joana).
progenitor(raquel,joana).
progenitor(luiz,mariana).
progenitor(rute,mariana).
progenitor(mariana,izabel).
progenitor(ezequiel,izabel).
progenitor(mariana,cerafim).
progenitor(lucas,cerafim).
progenitor(lucas,andre).
progenitor(mariana,andre).
progenitor(andre,henrique).
progenitor(lucia,henrique).


homem(pedro).
homem(joao).
homem(jose).
homem(luiz).
homem(ezequiel).
homem(cerafim).
homem(lucas).
homem(andre).
homem(henrique).

mulher(maria).
mulher(ana).
mulher(joana).
mulher(helena).
mulher(rute).
mulher(mariana).
mulher(izabel).
mulher(lucia).
avo(X,Y):- progenitor(X,Z),progenitor(Z,Y).

ancestral(X,Y):- progenitor(X,Y).
ancestral(X,Y):- progenitor(X,Z), ancestral(Z,Y).

mae(X,Y) :- progenitor(X,Y), mulher(X).
pai(X,Y) :- progenitor(X,Y), homem(X).

irmao(X,Y) :- pai(X,Y);mae(X,Y).

tio(X,Y) :- ancestral(Z,Y),irmao(X,Z).