PROGRAM:

read_number(Number) :-
    read(Number),
    number(Number).

max_number(X, Y, Max) :-
    (X >= Y -> Max = X ; Max = Y).

min_number(X, Y, Min) :-
    (X =< Y -> Min = X ; Min = Y).

main :-
    write('Enter the first number: '),
    read_number(Num1),
    write('Enter the second number: '),
    read_number(Num2),
    max_number(Num1, Num2, Max),
    min_number(Num1, Num2, Min),
    format('The maximum of ~w and ~w is ~w~n', [Num1, Num2, Max]),
    format('The minimum of ~w and ~w is ~w~n', [Num1, Num2, Min]).



QUERIES:
?- main.
Enter the first number: 7.
Enter the second number: 3.
The maximum of 7 and 3 is 7
The minimum of 7 and 3 is 3
true.
