# -----------------------------------------------------------------------------
# Name:        tictac
# Purpose:     Implement a game of Tic Tac Toe
#
# Author:      Pavlos P
# -----------------------------------------------------------------------------
"""
Tic-tac-toe game
"""
import tkinter
import random


class Game(object):
    """
    Class for Tic-tac-toe game

    Argument:
    parent (tkinter.Tk): the root window object

    Attributes:
    parent: (tkinter.Tk) the root window object
    canvas: (tkinter.Canvas) canvas representing the game board
    count_moves:(int) counter for moves
    next:(bool) allows next move
    """

    tile_size = 100
    positions = []  # records the positions of the players

    def __init__(self, parent):

        parent.title("Tic Tac Toe")

        self.count_moves = 0
        self.next = True

        restart_button = tkinter.Button(parent, text='Restart', width=30, command=self.restart)
        restart_button.grid()

        self.draw_board(parent)

        self.canvas.bind("<Button-1>", self.play)

        self.title = tkinter.Label(parent, text='')
        self.title.grid()

        self.restart()

    def draw_board(self, parent):
        """
        draws the board

        :param parent:(tkinter.Tk) the root window object
        """

        self.canvas = tkinter.Canvas(parent,
                                     width=self.tile_size * 3,
                                     height=self.tile_size * 3)
        self.canvas.grid()

        for row in range(3):
            for column in range(3):
                self.canvas.create_rectangle(self.tile_size * column,
                                             self.tile_size * row,
                                             self.tile_size * (column + 1),
                                             self.tile_size * (row + 1),
                                             fill='white')
        self.canvas.grid()

    def play(self, event):
        """
        Switches players on the board and fills colors accordingly

        :param event:event handler
        """

        if self.next:
            square = self.canvas.find_closest(event.x, event.y)
            user_move = square[0]

            next_player = False
            for index, item in enumerate(self.positions):
                if index == user_move:
                    if item == "Empty":
                        self.count_moves += 1
                        self.positions[user_move] = 'x'
                        self.canvas.itemconfigure(square, fill="red")
                        if self.next:
                            next_player = True

            if self.count_moves < 5:
                if next_player:
                    self.comput_turn()

            self.check_if_won()

    def comput_turn(self):
        """
        Called from play method for the next computer move
        """

        comp_move = self.get_pc_move()

        for index, item in enumerate(self.positions):
            if index == comp_move:
                if item == "Empty":
                    self.positions[index] = 'O'
                    self.canvas.itemconfigure(tagOrId=(comp_move), fill='blue')

    def get_pc_move(self):
        """
        Generates a random integer for random computer move
        :return: the integer
        """

        found_index = False
        while not found_index:
            index = random.randint(1, 9)
            if 'Empty' in self.positions[index]:
                found_index = True
        return index

    def restart(self):
        """
        restarts the game at any given time
        """

        self.title.configure(text='')
        self.next = True
        self.count_moves = 0
        self.positions = ["Empty" for i in range(0, 10)]
        for shape in self.canvas.find_all():
            self.canvas.itemconfigure(shape, fill='white')

    def check_if_won(self):
        """
        checks if one of the players won by checking positions
        prints message if there is a winner or prints tie game
        """

        x = ['x', 'x', 'x']
        o = ['O', 'O', 'O']

        if self.positions[1::4] == x:
            self.title.configure(text='Winner is the user!')
            self.next = False
        elif self.positions[1::4] == o:
            self.title.configure(text='Winner is the computer!')
            self.next = False

        if self.positions[1::3] == x:
            self.title.configure(text='Winner is the user!')
            self.next = False
        elif self.positions[1::3] == o:
            self.title.configure(text='Winner is the computer!')
            self.next = False

        if self.positions[2::3] == x:
            self.title.configure(text='Winner is the user!')
            self.next = False
        elif self.positions[2::3] == o:
            self.title.configure(text='Winner is the computer!')
            self.next = False

        if self.positions[3::3] == x:
            self.title.configure(text='Winner is the user!')
            self.next = False
        elif self.positions[3::3] == o:
            self.title.configure(text='Winner is the computer!')
            self.next = False

        if self.positions[3] == self.positions[5] == self.positions[7] \
                and self.positions[5] == 'x':
            self.title.configure(text='Winner is the user!')
            self.next = False
        elif self.positions[3] == self.positions[5] == self.positions[7] \
                and self.positions[5] == 'O':
            self.title.configure(text='Winner is the computer!')
            self.next = False

        if self.positions[1:4] == x:
            self.title.configure(text='Winner is the user!')
            self.next = False
        elif self.positions[1:4] == o:
            self.title.configure(text='Winner is the computer!')
            self.next = False

        if self.positions[4:7] == x:
            self.title.configure(text='Winner is the user!')
            self.next = False
        elif self.positions[4:7] == o:
            self.title.configure(text='Winner is the computer!')
            self.next = False

        if self.positions[7:10] == x:
            self.title.configure(text='Winner is the user!')
            self.next = False
        elif self.positions[7:10] == o:
            self.title.configure(text='Winner is the computer!')
            self.next = False

        if self.count_moves == 5:
            if self.next:
                self.title.configure(text='Tie Game !')


def main():
    root = tkinter.Tk()
    Game(root)
    root.mainloop()


if __name__ == '__main__':
    main()
