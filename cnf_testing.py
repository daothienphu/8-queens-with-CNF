def generate_cnf_level_2(size, verbose=False):
    restrictions = [[i for i in range(1,size*size+1)]]
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

res=generate_cnf_level_1(8, verbose=False)
open("fack_you.txt",mode="w").write(str(res))