from random import randint
from typing import List


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
generate_cnf(8)

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

def filter_str_in_restrictions(restrictions):
    filtered=[]
    for i in restrictions:
        if (type(i)!=str):
            filtered.append(i)
    return filtered


restrictions=generate_cnf(8)

input_list=[]
for i in range(8):
    current_input=randint(1,64)
    if current_input not in input_list:
        input_list.append(current_input)
    else:
        i=i-1

for i in input_list:
    print("Setting a queen at",i)
    restrictions=generate_cnf_from_input(input=i,restrictions=restrictions)

for idx,i in enumerate(restrictions):
    print(i)
    



