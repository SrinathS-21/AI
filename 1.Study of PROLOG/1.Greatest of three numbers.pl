PROGRAM:

read_number(Number) :-
read(Number),
number(Number).
main :-
write('Enter the first number: '),
read_number(Num1),
write('Enter the second number: '),
read_number(Num2),
Sum is Num1 + Num2,
format('The sum of ~w and ~w is ~w~n', [Num1, Num2, Sum]).


QUERIES:

?- main.
Enter the first number: 5.
Enter the second number: 3.
The sum of 5 and 3 is 8
true
