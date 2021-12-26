from utils import *
from ui import *


def main():
    verbose = False
    while True:
        task = input("Task: ")
        if task == "c":
            print("\nExecuting task c:")
            point = [*map(int, input("Cordinates of point to test CNF: ").split())]
            point = point[0]*8 + point[1]
            cnf = generate_cnf(8, verbose)
            print("\nCNF:", format_cnf([get_restrictions_from_input(point, cnf)]))
            print("\nDone task c.\n\n")
        elif task == "d":
            print("\nExecuting level 1 of task d:")
            cnfs_1 = generate_cnf_level_1(8,verbose=verbose)
            print("Generated CNF clauses:")
            print(format_cnf(cnfs_1), end="\n\n\n")
            cnf_and_queens = find_satisfied_set(cnfs_1)
            print("Satisfied set of queens: ", cnf_and_queens[1])
            print_board_console(cnf_and_queens[1])
            print("\nDone level 1 of task d.\n\n")


            print("\nExecuting level 2 of task d:")
            cnfs_2 = generate_cnf_level_2(8,verbose=verbose)
            print("Generated CNF clauses:")
            print(format_cnf(cnfs_2), end="\n\n\n")
            cnf_and_queens_2 = find_satisfied_set(cnfs_2)
            print("Satisfied set of queens: ", cnf_and_queens_2[1])
            print_board_console(cnf_and_queens_2[1])
            print("\nDone level 2 of task d.\n\n")
        elif task == 'f':
            print("\nExecuting task f:")
            ui = UI()
            print("\nDone task f.\n\n")
        elif task == 'q':
            print("\nExiting...")
            break
        else:
            print("Task has to be in {c, d, f}, q to quit.")

if __name__ == '__main__':
    main()