from random import randint, choice
from typing import List
from pysat.formula import CNF
from pysat.solvers import Lingeling

def generate_cnf(size, verbose=False):
    restrictions = []
    for i in range(size*size):
        current_restriction = [(i+1)]
        for j in range(size*size):
            if (i!=j)and((j % size == i %size) or (j // size == i // size) or (abs(i//size-j//size)==abs(i%size-j%size))):
                current_restriction.append((j+1)*-1)
        restrictions.append(current_restriction)
    if verbose:
        for i in restrictions:
            print(i)
    return restrictions

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

def get_restrictions_from_input(input,restrictions):
    return restrictions[input-1]

#--------------------------------------------------To Be Deleted-----------------------------------------------------

# def cache_all_cnf_clauses(verbose=False):
#     if verbose:
#         print("\n\n\nCNF BEFORE SETTING ANY QUEEN")
#     return generate_cnf(8, verbose)
# def set_random_queens(cnf_cache, verbose=False):
#     #set random queens
#     input_list=[]
#     for i in range(64):
#         input_list+=[i+1]
#     clauses = [input_list]
#     queens_set=[]
#     iterations=randint(1,7)
#     print("\n\n\nSETTING",iterations,"QUEENS ON THE BOARD")
#     for i in range(iterations):
#         current_input=choice(input_list)
#         queens_set+=[current_input]
#         if verbose:
#             print("SETTING " + str(current_input))
#         for j in get_restrictions_from_input(current_input, cnf_cache):
#             clauses += [[j]]
#         input_list = find_satisfied_set(clauses)
#         if verbose:
#             print("Clauses: ")
#             print(clauses,end="\n\n")
#             print("Input_list: ")
#             print(input_list,end="\n\n\n")
#     print("THE GIVEN INPUT IS:", *queens_set)
#     return (iterations, queens_set, clauses, input_list)
# def find_possible_solution(given_queens_data, cnf_cache, verbose=False):
#     iterations = given_queens_data[0]
#     queens_set = given_queens_data[1]
#     clauses = given_queens_data[2]
#     input_list = given_queens_data[3]
#     byColumns = False
#     if len(given_queens_data) == 5:
#         columns = given_queens_data[4]
#         byColumns = True
#     if verbose:
#         print()
#     while iterations < 8:
#         current_input=choice(input_list)
#         if byColumns:
#             col_index=choice(columns)
#             columns.remove(col_index)
#             reduced_input_list = [j for j in input_list if col_index * 8 <= j and j < col_index*8 + 7]
#             current_input=choice(reduced_input_list)    
#         queens_set+=[current_input]
#         if verbose:
#             print("SETTING " + str(current_input))
#         for i in get_restrictions_from_input(current_input, cnf_cache):
#             clauses += [[i]]
#         input_list = find_satisfied_set(clauses)
#         if verbose:
#             print("Clauses: ")
#             print(clauses,end="\n\n")
#             print("Input_list: ")
#             print(input_list,end="\n\n\n")
#         if 0 in input_list:
#             break
#         iterations += 1
#     if (iterations == 8):
#         print("THE QUEENS CAN BE PLACED AT:", *queens_set)
#         return True
#     else:
#         print("CANNOT FIND SOLUTION TO THE 8 QUEENS PROBLEM WITH THE GIVEN INPUT.\n")
#         return False
# def set_random_queens_by_col(cnf_cache, verbose=False):
    #set queens by column such that no two queen is on the same column
    # input_list=[]
    # for i in range(64):
    #     input_list+=[i+1]
    # clauses = [input_list]
    # queens_set=[]
    # iterations=randint(1,7)
    # #put all column indexes in a list
    # columns=[i for i in range (8)]
    # print("\n\n\nSETTING",iterations,"QUEENS ON THE BOARD")
    # for i in range(iterations):
    #     #get a random column
    #     col_index=choice(columns)
    #     #remove the column from the column list
    #     columns.remove(col_index)
    #     #put a queen randomly in the selected column
    #     reduced_input_list = [j for j in input_list if col_index * 8 <= j and j < col_index*8 + 7]
    #     current_input=choice(reduced_input_list)
    #     queens_set+=[current_input]
    #     if verbose:
    #         print("SETTING " + str(current_input))
    #     for j in get_restrictions_from_input(current_input, cnf_cache):
    #         clauses += [[j]]
    #     input_list = find_satisfied_set(clauses)
    #     if verbose:
    #         print("Clauses: ")
    #         print(clauses,end="\n\n")
    #         print("Input_list: ")
    #         print(input_list,end="\n\n\n")

    # print("THE GIVEN INPUT IS:", *queens_set)
    # return (iterations, queens_set, clauses, input_list, columns)
#--------------------------------------------------To Be Deleted-----------------------------------------------------