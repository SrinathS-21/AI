PROGRAM:
PROLOG:
:- use_module(library(clpfd)).% Finite domain constraints
n_queens(N, Qs) :-
length(Qs, N),
Qs ins 1..N,
safe_queens(Qs).
safe_queens([]).
safe_queens([Q|Qs]) :- safe_queens(Qs, Q, 1), safe_queens(Qs).
safe_queens([], _, _).
safe_queens([Q|Qs], Q0, D0) :-
Q0 #\= Q,
abs(Q0 - Q) #\= D0,
D1 #= D0 + 1,
safe_queens(Qs, Q0, D1).

QUERIES:
?- n_queens(8, Qs), label(Qs).
Qs = [1, 5, 8, 6, 3, 7, 2, 4]
?- n_queens(4, Qs), label(Qs).
Qs = [2, 4, 1, 3]
?-n_queens(2, Qs), label(Qs).
false