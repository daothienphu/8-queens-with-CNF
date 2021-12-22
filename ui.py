from pysat.formula import CNF
from pysat.solvers import Lingeling

def find_satisfied_set(restrictions):
    chessboard = CNF()
    for i in restrictions:
        chessboard.append(i)
    res = ''
    with Lingeling(bootstrap_with=chessboard.clauses, with_proof=True) as l:
        if l.solve() == False:
            res = l.get_proof()
            print(f"The satisfied set is: \n{res}")
    return res