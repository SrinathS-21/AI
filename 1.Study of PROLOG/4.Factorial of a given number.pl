PROGRAM:

read_number(Number) :-
    read(Number),
    number(Number).

factorial(0, 1).
factorial(N, Result) :-
    N > 0,
    N1 is N - 1,
    factorial(N1, F1),
    Result is N * F1.

main :-
    write('Enter a number: '),
    read_number(N),
    factorial(N, Result),
    format('The factorial of ~w is ~w~n', [N, Result]).


QUERIES:
?- main.
Enter a number: 5.
The factorial of 5 is 120
true.
