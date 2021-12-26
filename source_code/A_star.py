import random
import numpy as np
import math
# with open("input.txt", "r") as file: 
#     m = int(file.readline())
# #     print(m)
#     #queens_pos = list(map(lambda el: list(map(int,el[1:-1].split(","))),line.split(" ")))
#     queens_pos = [[*map(int, q.split(", "))] for q in file.readline().strip()[1:-1].split(") (")]
# queens_pos
class A_star:
    def __init__(self, queens):
        self.queens_pos = queens
 
    def attacked_queens_pairs(self, seqs):
        rows = [0] * 8
        cols = [0] * 8
        diagonal_main = [0] * 15
        diagonal_sub = [0] * 15
        LIST= list(seqs)
        res=0
        for i in range(len(LIST)):
            if LIST[i]>0:
                rows[i] += 1
                cols[LIST[i]-1]+=1
                diagonal_main[LIST[i]-1 + i] +=1
                diagonal_sub[LIST[i] - i +6]+=1
        for i in range(8):
                res += math.comb(rows[i], 2)+ math.comb(cols[i], 2) + math.comb(diagonal_main[i], 2) + math.comb(diagonal_sub[i], 2)
        for i in range(8,15):
                res +=  math.comb(diagonal_main[i], 2) + math.comb(diagonal_sub[i], 2)
        return res
    def next_row_invalids(self, seqs):
        if seqs.count(0) ==0:
            return 8
        cols = [0] * 8
        diagonal_main = [0] * 15
        diagonal_sub = [0] * 15
        POS = seqs.index(0)
        LIST= list(seqs)
        
        res= 0
        for i in range(len(LIST)):
            LIST[i]= [i,LIST[i]-1]
        LIST = list(filter(lambda x: x[1] >= 0, LIST))
        #print(LIST)

        for pos in LIST: 
            cols[pos[1]] = 1
            diagonal_main [pos[0]+ pos[1]]=1
            diagonal_sub [pos[1]- pos[0] +7]=1
      
        for i in range(8):
            #print("    " + str(diagonal_main[POS+ i]) +"    " + str(diagonal_sub[i- POS +7])+"     " + str(cols[i]))
            if (cols[i] ==1) | (diagonal_sub[i- POS +7] ==1)  | (diagonal_main[POS+ i] ==1) :
            #if (diagonal_main[POS+ i] ==1  ) :
                res +=  1
        return res
    def display_board(self, seqs):
        
        board = np.array([0] * 81)  
        board = board.reshape(9, 9)  

        for i in range(1, 9):
            board[seqs[i - 1]][i] = 1  
        print('The corresponding chessboard is as follows:')
        for i in board[1:]:
            for j in i[1:]:
                print(j, ' ', end="") 
            print()  
        print('The number of queens to attack is' + str(self.attacked_queens_pairs(seqs)) + "  f(n)= " +str(self.attacked_queens_pairs(seqs)+ self.next_row_invalids(seqs)))
    
    def solve(self):
        rows = [0] * 8
        cols = [0] * 8
        diagonal_main = [0] * 15
        diagonal_sub = [0] * 15
        table = np.array([[0]*9]*8)
        for pos in self.queens_pos: 
                table[pos[0]][pos[1]+1]=1
                cols[pos[1]] = 1
                diagonal_main [pos[0]+ pos[1]]=1
                diagonal_sub [pos[1]- pos[0] +7]=1

        avail_row_idx = [i  for i in range(len(cols)) if cols[i] == 0]
        print(diagonal_main)
        #decoded = tf.argmax(table, axis=1)

        decoded= [0]*8
        for pos in self.queens_pos:
            decoded[pos[0]]= pos[1 ]+1
        #decoded = np.array(decoded)
        SEQS= list(decoded)
        
        frontier_priority_queue = [{'unplaced_queens':8, 'pairs':28+8, 'seqs':SEQS}] #
        solution = []

        while frontier_priority_queue:
            first = frontier_priority_queue.pop(0)  
            if first['pairs'] == 8 and first['unplaced_queens'] == 0: #
                break
            nums = list(avail_row_idx) 
            seqs = first['seqs']
            print(seqs)
            #print(nums)
            LIST = list(filter(lambda x: x == 0, seqs))
            self.display_board(seqs)
            if(len(LIST)>0):
                for j in range(len(nums)): 
                    temp_seqs = list(seqs)
                    temp = random.choice(nums)  
                    nums.remove(temp)
                    if ((diagonal_main[pos + temp ] ==0) & (diagonal_sub [temp- pos +7]==0) ):
                        temp_seqs[pos] = temp +1 
                        print("     "+ str(temp_seqs))
                      
                        
                        frontier_priority_queue.append({'unplaced_queens':temp_seqs.count(0), 'pairs':8*self.attacked_queens_pairs(temp_seqs) + self.next_row_invalids(temp_seqs) + 8 -temp_seqs.count(0),'seqs':temp_seqs})
                frontier_priority_queue = sorted(frontier_priority_queue, key=lambda x:(x['pairs'], x['unplaced_queens'])) # First, the sequences are sorted in the order of h(n) from small to large; if h(n) is the same, the sequences are sorted in the order of g(n) from small to large


        if solution:
            solution2=[]
            for i in range(len(solution)):
                solution2 += [8*i + solution[i]]
            print('Solution sequence found:' + str(solution2))
            self.display_board(solution)
            return solution2[len(self.queens_pos):]
        else:
            return []
            #print('Algorithm failed, no solution found')