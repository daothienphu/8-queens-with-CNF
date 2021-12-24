from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from time import sleep
from random import randint 
 
class Window(QMainWindow):
    def __init__(self, *queens):
        #create window
        super().__init__()
        self.acceptDrops()
        self.setWindowTitle("8 Queens Problem Solver")
        self.setGeometry(1920//2 - 300, 1080//2 - 350, 600, 700)
        
        #create widget instance
        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        
        #create 
        pixmap1 = QPixmap('chessboard.png')
        pixmap1 = pixmap1.scaledToWidth(600)
        self.board = QLabel()
        self.board.setPixmap(pixmap1)
        self.board.move(0, 0)
        
        #create button
        button = QPushButton('Input queens', self)
        button.setToolTip('Press this button to input the queens\' locatons')
        button.move(275,650)
        button.clicked.connect(self.import_queens)

        #create layout with only the chessboard
        layout_box = QHBoxLayout(self.widget)
        layout_box.setContentsMargins(0, 0, 0, 0)
        layout_box.addWidget(self.board)
        #layout_box.setAlignment() set alignment vertical then add the button underneath
        #layout_box.addWidget(button)
        
        self.queens_counter = 0
        self.pre_create_queens()
        self.show_board()

        #show steps - still need fixing
        for i in list(queens[0]):
            self.set_queen_at(i)
            self.show_board()
                      

    def import_queens(self): 
        with open(QFileDialog().getOpenFileName(self, 'Open File', '', 'Text Files (*.txt)')[0], "r") as file: 
            file.readline()
            [(self.set_queen_at([*map(int, q.split(", "))][0]*8 + [*map(int, q.split(", "))][1])) for q in file.readline().strip()[1:-1].split(") (")]

    def show_board(self):
        self.show()

    def pre_create_queens(self):
        self.queens_black = [0]*8
        for i in range(8):
            self.queens_black[i] = QLabel(self.widget)
            self.queens_black[i].setFixedSize(0, 0)
            self.queens_black[i].setPixmap(QPixmap('queen_black.png').scaledToWidth(75))
            self.queens_black[i].move(0, 0)
        
        self.queens_white = [0]*8
        for i in range(8):
            self.queens_white[i] = QLabel(self.widget)
            self.queens_white[i].setFixedSize(0, 0)
            self.queens_white[i].setPixmap(QPixmap('queen_white.png').scaledToWidth(75))
            self.queens_white[i].move(0, 0)

    def set_queen_at(self, position):
        j = position % 8
        i = position // 8
        if (i & 1 != j & 1):
            self.queens_white[self.queens_counter].setFixedSize(75, 75)
            self.queens_white[self.queens_counter].move(j * 75, 50 + i * 75)
        else:
            self.queens_black[self.queens_counter].setFixedSize(75, 75)
            self.queens_black[self.queens_counter].move(j * 75, 50 + i * 75)
        #50 + j* 75 is because the chessboard size is 600x600, but the window size is 600x700
        self.queens_counter += 1

class UI:
    def __init__(self, *queens):
        self.app = QApplication(sys.argv)
        self.window = Window(queens)
        self.app.exec_()

    def set_queen_at(self, position):
        self.window.set_queen_at(position)
        self.window.show_board()
        
if __name__ == '__main__':
    ui = UI(62, 25)