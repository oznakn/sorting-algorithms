quicksort([H|T],RR) :- partition(T,H,L,R), quicksort(L,Ls), quicksort(R,Rs), append(Ls,[H|Rs],RR).
quicksort([],[]).

partition([H|T],Y,[H|Ls],Rs) :- H =< Y, partition(T,Y,Ls,Rs).
partition([H|T],Y,Ls,[H|Rs]) :- H > Y, partition(T,Y,Ls,Rs).
partition([],_,[],[]).

append([],R,R).
append([H|T],R,[H|TT]) :- append(T,R,TT).
