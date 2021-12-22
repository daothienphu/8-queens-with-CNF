from random import randint
from typing import List
from pysat.formula import CNF
from pysat.solvers import Lingeling


def generate_cnf(size):
    restrictions = []
    for i in range(size*size):
        current_restriction = [i+1]
        for j in range(size*size):
            if (i!=j)and((j % size == i %size) or (j // size == i // size) or (abs(i//size-j//size)==abs(i%size-j%size))):
                current_restriction.append((j+1)*-1)
        restrictions.append(current_restriction)
    for i in restrictions:
        print(i)
    return restrictions

def generate_cnf_from_input(input:int,restrictions:List):
    if (type(restrictions[input-1])==str):
        return restrictions
    restrictions[input-1]="Removed as input "+str(input)
    for idx,i in enumerate(restrictions):
        if (type(i)==str):
            continue
        if (input*-1) in i:
            restrictions[idx]="Attacked by "+str(input)
    return restrictions

def get_restrictions_from_input(input,restrictions):
    return restrictions[input-1]


def find_satisfied_set(restrictions):
    chessboard = CNF()
    for i in restrictions:
        chessboard.append(i)
    r = ''
    with Lingeling(bootstrap_with=chessboard.clauses, with_proof=True) as l:
        r = l.solve()
        if not r:
            print(f"proof it's not satisfiable: \n{l.get_proof()}")
        else:
            print("8 queens can be solved")
    return res

print("\n\n\nCNF before setting any queen")
restrictions=generate_cnf(8)

#set random queens
input_list=[]
iterations=randint(1,7)
print("\n\n\nSetting",iterations,"queens on board")
for i in range(iterations):
    current_input=randint(1,64)
    if current_input not in input_list:
        input_list.append(current_input)
    else:
        i=i-1






#update restrictions
# for i in input_list:
#     print("Setting a queen at",i)
#     restrictions=generate_cnf_from_input(input=i,restrictions=restrictions)

#get restrictions of inputs
input_set=[]
for i in input_list:
    print("Setting a queen at",i)
    input_set.append(get_restrictions_from_input(i,restrictions=restrictions))

for i in input_set:
    print(i)

for i in range(8-len(input_set)):
    


# print("\n\n\nList of restrictions after CNF")
# for idx,i in enumerate(restrictions):
#     print(i)

    





