# If downloading, use latest version if Pycharm and Python interpreter
# Imports Zelle's graphics library to be used in the majority of this program, but also uses code from Python's built-in time
# library
from graphics import *


class TicTacToe:
    """The main class used to simulate the Tic Tac Toe Game"""
    def __init__(self, pwin):
        """Initializes all attributes to be used in later methods"""
        # Creates 9 X and 9 O text objects in all nine positions to be drawn later
        self.x1, self.x2, self.x3, self.x4, self.x5, self.x6, self.x7, self.x8, self.x9 = (Text(Point(4, 4), "X"),
                Text(Point(12, 4), "X"), Text(Point(20, 4), "X"), Text(Point(4, 12), "X"), Text(Point(12, 12), "X"),
                Text(Point(20, 12), "X"), Text(Point(4, 20), "X"), Text(Point(12, 20), "X"), Text(Point(20, 20), "X"))
        self.o1, self.o2, self.o3, self.o4, self.o5, self.o6, self.o7, self.o8, self.o9 = (Text(Point(4, 4), "O"),
                Text(Point(12, 4), "O"), Text(Point(20, 4), "O"), Text(Point(4, 12), "O"), Text(Point(12, 12), "O"),
                Text(Point(20, 12), "O"), Text(Point(4, 20), "O"), Text(Point(12, 20), "O"), Text(Point(20, 20), "O"))
        # Initializes a list with all X text objects
        self.x_objects_list = [self.x1, self.x2, self.x3, self.x4, self.x5, self.x6, self.x7, self.x8, self.x9]
        # Sets all the text objects to size 24 and color red/blue
        for obj in self.x_objects_list:
            obj.setSize(24), obj.setTextColor("red")
        # Initializes a list with all O text objects
        self.o_objects_list = [self.o1, self.o2, self.o3, self.o4, self.o5, self.o6, self.o7, self.o8, self.o9]
        for obj in self.o_objects_list:
            obj.setSize(24), obj.setTextColor("blue")
        # Initializes empty list with nine empty items to represent the 9 different boxes on a Tic Tac Toe board
        self.current = [""] * 9
        # Initializes a list with the coordinates of all nine boxes on a Tic Tac Toe board
        self.positions = [[0, 0, 8, 8], [8, 0, 16, 8], [16, 0, 24, 8], [0, 8, 8, 16], [8, 8, 16, 16], [16, 8, 24, 16],
                          [0, 16, 8, 24], [8, 16, 16, 24], [16, 16, 24, 24]]
        self.win = pwin
        self.turn = 0
        # Initializes a list that holds all winning combinations relative to the index in self.positions
        self.winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8],
                                     [2, 4, 6]]
        self.active_objects = []
        self.save_load_list = []

    def x_or_o(self, point):
        """Places and X or an O on the board where the user clicked and adds several attributes about the drawn text
        object to class lists"""
        for n in self.positions:
            # Checks if where the user clicked is between the coordinates of the boxes from self.positions and if the
            # box has already been occupied
            if (n[0] < point.getX() <= n[2] and n[1] <= point.getY() <= n[3] and
                    self.current[self.positions.index(n)] == ""):
                if self.turn % 2 == 0:
                    # Draws a text object from x_objects_list found because the indexes of self.positions match with it
                    self.x_objects_list[self.positions.index(n)].draw(self.win)
                    # Adds the object to a list with all active objects to refer to when the user decides to restart or
                    # load and the objects need to be undrawn
                    self.active_objects.append(self.x_objects_list[self.positions.index(n)])
                    # Adds X or O to current list to be used to see if it matches with any winning scores
                    self.current[self.positions.index(n)] = "X"
                    # Adds the index + X/O ro be referred to if the user decides to save ot load
                    self.save_load_list.append(str(self.positions.index(n)) + "X")
                else:
                    self.o_objects_list[self.positions.index(n)].draw(self.win)
                    self.active_objects.append(self.o_objects_list[self.positions.index(n)])
                    self.current[self.positions.index(n)] = "O"
                    self.save_load_list.append(str(self.positions.index(n)) + "O")
                self.turn += 1

    def win_checker(self, pstatus):
        """Checks if the TicTacToe game has been won, drawing a line over the three Xs/Os and changing the status to
        a winning message if there is a winner"""
        # Compares winning combinations of the TicTacToe boxes 1-9 (-1 to correlate with the indices of a list to the
        # current text objects on the board to see if there's a winner
        for n in self.winning_combinations:
            if ["X", "X", "X"] == [self.current[n[0]], self.current[n[1]], self.current[n[2]]]:
                pstatus.setText("X WINS")
                # Draws a line that connects the three in a row
                winning_line = Line(Point((self.positions[n[0]][0] + self.positions[n[0]][2]) / 2,
                                          (self.positions[n[0]][1] + self.positions[n[0]][3]) / 2),
                                    Point((self.positions[n[2]][0] + self.positions[n[2]][2]) / 2,
                                          (self.positions[n[2]][1] + self.positions[n[2]][3]) / 2))
                winning_line.setWidth(3), winning_line.setFill("purple")
                winning_line.draw(self.win)
                self.active_objects.append(winning_line)
                return True
            elif ["O", "O", "O"] == [self.current[n[0]], self.current[n[1]], self.current[n[2]]]:
                pstatus.setText("O WINS")
                winning_line = Line(Point((self.positions[n[0]][0] + self.positions[n[0]][2]) / 2,
                                          (self.positions[n[0]][1] + self.positions[n[0]][3]) / 2),
                                    Point((self.positions[n[2]][0] + self.positions[n[2]][2]) / 2,
                                          (self.positions[n[2]][1] + self.positions[n[2]][3]) / 2))
                winning_line.setWidth(3), winning_line.setFill("purple")
                winning_line.draw(self.win)
                self.active_objects.append(winning_line)
                return True
        return False

    def whose_turn(self, pstatus, over):
        """Simply method to display whose turn it is in the upper left"""
        if over is False:
            if self.turn % 2 == 0:
                pstatus.setText("X Turn")
            else:
                pstatus.setText("O Turn")


def confirmation_window():
    """A confirmation window to be used to affirm that the user wants to restart or load the game"""
    # create a confirmation window
    con_win = GraphWin("Confirmation")
    con_win.setBackground("dark slate gray")
    # set coordinates to go from (0,0) in the lower left, to (24,32) in the upper right
    con_win.setCoords(0.0, 0.0, 24.0, 32.0)
    question = Text(Point(12.5, 28), "Are you sure?")
    question.setSize(14)
    question.draw(con_win)
    # Yes button
    y_rectangle = Rectangle(Point(3, 14), Point(9, 22))
    y_rectangle.setFill("light blue")
    y_rectangle.draw(con_win)
    y_text = Text(Point(6, 18), "Yes")
    y_text.setSize(14)
    y_text.draw(con_win)
    # No button
    n_rectangle = Rectangle(Point(15, 14), Point(21, 22))
    n_rectangle.setFill("light blue")
    n_rectangle.draw(con_win)
    n_text = Text(Point(18, 18), "No")
    n_text.setSize(14)
    n_text.draw(con_win)
    # Stuck in while loop until either the areas of the yes or no buttons are clicked
    while True:
        point_click = con_win.getMouse()
        if point_click.getY() > 14:
            if 3 < point_click.getX() < 9:
                con_win.close()
                return "y"
            elif 15 < point_click.getX() < 21:
                con_win.close()
                return "n"


def main():
    # create a default 200x200 window
    win = GraphWin("Tic-Tac-Toe")
    win.setBackground("dark slate gray")
    # set coordinates to go from (0,0) in the lower left
    # to (24,32) in the upper right
    win.setCoords(0.0, 0.0, 24.0, 32.0)
    # Draw vertical lines for grid
    Line(Point(8, 0), Point(8, 24)).draw(win)
    Line(Point(16, 0), Point(16, 24)).draw(win)
    # Draw horizontal lines for grid
    Line(Point(0, 8), Point(24, 8)).draw(win)
    Line(Point(0, 16), Point(24, 16)).draw(win)
    Line(Point(0, 24), Point(24, 24)).draw(win)
    # Status text to show display whose turn it is and a winner
    status_rectangle = Rectangle(Point(0, 24), Point(6, 32))
    status_rectangle.setFill("dark orchid")
    status_rectangle.draw(win)
    status = Text(Point(3, 28), "X turn")
    status.setSize(12)
    status.draw(win)
    # Restart button
    restart_rectangle = Rectangle(Point(6, 24), Point(12, 32))
    restart_rectangle.setFill("dark orchid")
    restart_rectangle.draw(win)
    restart = Text(Point(9, 28), "Restart")
    restart.setSize(14)
    restart.draw(win)
    # Save button
    save_rectangle = Rectangle(Point(12, 24), Point(18, 32))
    save_rectangle.setFill("dark orchid")
    save_rectangle.draw(win)
    save_button = Text(Point(15, 28), "Save")
    save_button.setSize(14)
    save_button.draw(win)
    # Load button
    load_rectangle = Rectangle(Point(18, 24), Point(24, 32))
    load_rectangle.setFill("dark orchid")
    load_rectangle.draw(win)
    load_button = Text(Point(21, 28), "Load")
    load_button.setSize(14)
    load_button.draw(win)
    game_is_over = False
    game = TicTacToe(win)
    while True:
        point_click = win.getMouse()
        if point_click.getY() > 24:
            # If the restart button is clicked
            if 6 < point_click.getX() < 12:
                if confirmation_window() == "y":
                    # Undraws all active objects
                    for n in game.active_objects:
                        n.undraw()
                    # Resets all variables
                    game.turn = 0
                    game.active_objects = []
                    game.current = [""] * 9
                    game_is_over = False
                    game.whose_turn(status, game_is_over)
            # If the save button is clicked
            elif 12 < point_click.getX() < 18:
                savefile = open("TicTacToeSave.txt", "w")
                # Adds the elements of game.save_load_list which are the indices (from game.positions list) that
                # represent all active objects to the TicTacToeSave.txt savefile
                for item in game.save_load_list:
                    savefile.write(str(item) + " ")
                # Also adds the turn number the game was on when it was saved
                savefile.write(str(game.turn) + " ")
                save_button.setText("Saved!")
                time.sleep(0.5)
                savefile.close()
                save_button.setText("Save")
            # If the load button is clicked
            elif 18 < point_click.getX() < 24:
                # Undraws all active objects and resets all variables
                if confirmation_window() == "y":
                    for obj in game.active_objects:
                        obj.undraw()
                    game.save_load_list = []
                    print("")
                    game.current = [""] * 9
                    # Reads the savefile and splits it into a list
                    savefile = open("TicTacToeSave.txt", "r")
                    load = savefile.read().split(" ")
                    game.active_objects = []
                    # Adds the turn number added to the end of the file to game.turn
                    game.turn = int(load[-2])
                    for n in load[:-2]:
                        temp = int(n[0])
                        # Same process as in the x_or_o function
                        if n[1] == "X":
                            game.x_objects_list[temp].draw(win)
                            game.active_objects.append(game.x_objects_list[temp])
                            game.current[temp] = "X"
                            game.save_load_list.append(n)
                        else:
                            game.o_objects_list[temp].draw(win)
                            game.active_objects.append(game.o_objects_list[temp])
                            game.current[temp] = "O"
                            game.save_load_list.append(n)
                    # Checks to see if loaded game has a win or not
                    game_is_over = game.win_checker(status)
                    game.whose_turn(status, game_is_over)
                    load_button.setText("Loaded!")
                    time.sleep(0.5)
                    savefile.close()
                    load_button.setText("Load")
        else:
            if game_is_over is False:
                # When the game is not over and the board is pressed, the program calls game.x_or_o*( to see if an x/o
                # text object should be placed there, calls game_is_over() to see if there's a win, calls
                # game.whose_turn() to display whose turn it is, and then checks if there is a draw
                game.x_or_o(point_click)
                game_is_over = game.win_checker(status)
                game.whose_turn(status, game_is_over)
                if game.current.count("X") == 5 and game_is_over is False:
                    game_is_over = True
                    status.setText("Draw :(")


main()
