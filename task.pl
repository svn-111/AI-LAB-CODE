parent('Hasib' , 'Rakib').
parent('Hasib' , 'Jamil').
parent('Hasib' , 'Raisa').
parent('Rakib' , 'Sohel').
parent('Rakib' , 'Rahim').
parent('Raisa' , 'Rebeka').
parent('Rakib' , 'Sumi').
parent('Rakib' , 'Shila').
parent('Rashid' , 'Hasib').
male('Hasib').
male('Rakib').
male('Sohel').
male('Rashid').
male('Rahim').
male('Jamil').
female('Shila').
female('Rebeka').
female('Sumi').
female('Raisa').

brother(Y,Z) :-
parent(X,Y),parent(X,Z),male(Z),not(Y=Z).
sister(Y,Z) :-
parent(X,Y),parent(X,Z),female(Z),not(Y=Z).
uncle(N,U) :-
parent(X,Y),parent(Y,N),parent(X,U),not(U=Y),male(U).
aunt(N,A) :-
parent(X,Y),parent(Y,N),parent(X,A),not(A=Y),female(A)
.

grandparent(X, Z) :- parent(X, Y), parent(Y, Z).

/* [Built-in KB is enhanced with the 4 facts and 1 rule; two
2-place predicates; 3 variables; full stop
(.) as the end marker of a clause/ sentence / statement;
:- as ‘if’; comma (,) as logical AND. ] */

/* Procedure to find the grandchildren of X */

findGp :- write(' Grandchild: '), read(Z), write('Grandparent
'),

grandparent(Gp,Z), write(Gp).

findBro :-
write('Please Enter the Sibling name: '), read(X),
write('Brother: '), brother(X,Bro),
write(Bro), tab(5).

findSis :-
write('Please Enter the Sibling name: '), read(X),
write('Sister: '), sister(X,Sis),
write(Sis), tab(5).

findUncle :-
write('Please Enter the Nephew/Niece name : '), read(X),
write('Uncle: '), uncle(X,U),
write(U), tab(5).

findAunt:-
write('Please Enter the Nephew/Niece name: '), read(X),
write('Aunt: '), aunt(X,U),
write(U), tab(5).