from random import randint, choice
from typing import List
from pysat.formula import CNF
from pysat.solvers import Lingeling

def generate_cnf(size, verbose=False):
    #input = 4 (0, 3)
    #-27 or ((-28)and(-26))
    #(-27 and -28) or (-27 and -26) 
    #output = [[-27, -28], [-27, -26]]
    restrictions = []
    for i in range(size*size):
        current_restriction = [(i+1)* -1]
        for j in range(size*size):
            if (i!=j)and((j % size == i %size) or (j // size == i // size) or (abs(i//size-j//size)==abs(i%size-j%size))):
                current_restriction.append((j+1)*-1)
        restrictions.append(current_restriction)
    if verbose:
        for i in restrictions:
            print(i)
    return restrictions

def get_restrictions_from_input(input,restrictions):
    return restrictions[input-1]

def format_cnf(cnfs):
    res = ''
    for i in cnfs:
        tmp = ''
        for j in i:
            j = str(j)
            if '-' in j:
                tmp += '('
            tmp += j
            if '-' in j:
                tmp += ')'
            tmp += ' ∨ '
        res += tmp[:-3] + ' ∧ '
    return res[:-3]

def print_board_console(queens):
    board = ['.']*64
    for i in queens:
        board[i-1] = 'Q'
    for i in range(8):
        print(*board[i*8:i*8+8])

def generate_cnf_level_2(size, verbose=False):
    restrictions = []
    for i in range(size):
        current=[i for i in range(i*8+1,i*8+9)]
        restrictions.append(current)
    for i in range(size):
        current=[j+1 for j in range(size*size) if (j-i)%size==0]
        restrictions.append(current)
    for i in range(size*size):
        for j in range(size*size):
            if (i!=j)and((j % size == i %size) or (j // size == i // size) or (abs(i//size-j//size)==abs(i%size-j%size))):
                restrictions.append([-1*(i+1),(j+1)*-1])
    if verbose:
        for i in restrictions:
            print(i)
    return restrictions

def generate_cnf_level_1(size, verbose=False):
    restrictions = []
    for i in range(size):
        current=[i for i in range(i*8+1,i*8+9)]
        restrictions.append(current)
    for i in range(size*size):
        for j in range(size*size):
            if (i!=j)and((j % size == i %size) or (j // size == i // size) or (abs(i//size-j//size)==abs(i%size-j%size))):
                restrictions.append([-1*(i+1),(j+1)*-1])
    if verbose:
        for i in restrictions:
            print(i)
    return restrictions

def find_satisfied_set(restrictions):
    chessboard = CNF()
    for i in restrictions:
        chessboard.append(i)
    r = ''
    with Lingeling(bootstrap_with=chessboard.clauses, with_proof=False) as l:
        r = l.solve()
        if not r:
            #print(f"proof it's not satisfiable: \n{l.get_proof()}")
            return [0] 
        else:
            m = l.get_model() 

            n = []
            #print(m)
            for i in m:
                if (i > 0):
                    n+=[i]
            #print(*n)
    return (m, n)
