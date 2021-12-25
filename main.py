from utils import *

def main():
    verbose = True
    cnf_cache = cache_all_cnf_clauses(verbose=verbose)
    given_queens_data = set_random_queens(cnf_cache, verbose=verbose)
    find_possible_solution(given_queens_data, cnf_cache, verbose=verbose)

if __name__ == '__main__':
    main()