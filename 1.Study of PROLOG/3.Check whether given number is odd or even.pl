
PROGRAM:
is_odd(Number) :-
0 is mod(Number, 2),
!,
false.
is_odd(_).


QUERIES:
?- is_odd(3).
true.
