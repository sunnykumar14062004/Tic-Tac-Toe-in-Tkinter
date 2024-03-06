from tkinter import ttk
import tkinter
import random

def clear(turn, shape):
    label.config(text = "")
    for i in range (0, 3):
        for j in range(0, 3):
            button_list[i][j].config(text = " ", bg = "white", state = tkinter.NORMAL)
    if turn == -1:
        label["text"] = "x's turn"
    elif turn.get() == 0:
        computer_move(shape)

def modify():
    for i in range (0, 3):
        for j in range(0, 3):
            button_list[i][j].config(state = tkinter.DISABLED)

def is_draw():
    for i in range (0, 3):
        for j in range(0, 3):
            if button_list[i][j]["text"] == " ":
                return False
    return True

def check_winner(symbol, colour):
    for i in range(0, 3):
        count = 0
        for j in range(0, 3):
            if button_list[i][j]["text"] == symbol:
                count += 1
        if count == 3:
            for j in range(0, 3):
                button_list[i][j].config(bg = colour)
            return True
    for i in range(0, 3):
        count = 0
        for j in range(0, 3):
            if button_list[j][i]["text"] == symbol:
                count += 1
        if count == 3:
            for j in range(0, 3):
                button_list[j][i].config(bg = colour)
            return True
    row = column = count = 0
    for i in range(0, 3):
        if button_list[row][column]["text"] == symbol:
            count += 1
            row += 1
            column += 1
    if count == 3:
        for i in range(0, 3):
            row -= 1
            column -= 1
            button_list[row][column].config(bg = colour)
        return True
    row = count = 0
    column = 2
    for i in range(0, 3):
        if button_list[row][column]["text"] == symbol:
            count += 1
            row += 1
            column -= 1
    if count == 3:
        for i in range(0, 3):
            row -= 1
            column += 1
            button_list[row][column].config(bg = colour)
        return True
    return False

def can_win(shape):
    for i in range(0, 3):
        present = empty = 0
        for j in range(0, 3):
            if button_list[i][j]["text"] == shape:
                present += 1
            if button_list[i][j]["text"] == " ":
                empty += 1
                row = i
                col = j
        if present == 2 and empty == 1:
            return [row, col]
    for i in range(0, 3):
        present = empty = 0
        for j in range(0, 3):
            if button_list[j][i]["text"] == shape:
                present += 1
            if button_list[j][i]["text"] == " ":
                empty += 1
                row = j
                col = i
        if present == 2 and empty == 1:
            return [row, col]
    present = empty = 0
    for i in range(0, 3):
        if button_list[i][i]["text"] == shape:
            present += 1
        if button_list[i][i]["text"] == " ":
            empty += 1
            row = col = i
    if present == 2 and empty == 1:
        return [row, col]
    present = empty = 0
    for i in range(0, 3):
        if button_list[2-i][i]["text"] == shape:
            present += 1
        if button_list[2-i][i]["text"] == " ":
            empty += 1
            row = 2 - i
            col = i
    if present == 2 and empty == 1:
        return [row, col]
    return [-1, -1]

def no_of_trap(row, col, computer_shape):
    trap = 0
    present = empty = 0
    for i in range(0, 3):
        if button_list[row][i]["text"] == computer_shape:
            present += 1
        if button_list[row][i]["text"] == " " and col != i:
            empty += 1
    if present == 1 and empty == 1:
        trap += 1
    present = empty = 0
    for i in range(0, 3):
        if button_list[i][col]["text"] == computer_shape:
            present += 1
        if button_list[i][col]["text"] == " " and row != i:
            empty += 1
    if present == 1 and empty == 1:
        trap += 1
    if row == col:
        present = empty = 0
        for i in range(0, 3):
            if button_list[i][i]["text"] == computer_shape:
                present += 1
            if button_list[i][i]["text"] == " " and row != i:
                empty += 1
        if present == 1 and empty == 1:
            trap += 1
    if row + col == 2:
        present = empty = 0
        for i in range(0, 3):
            if button_list[2-i][i]["text"] == computer_shape:
                present += 1
            if button_list[2-i][i]["text"] == " " and not (row == 2-i and col == i):
                empty += 1
        if present == 1 and empty == 1:
            trap += 1
    return trap

def computer_move(shape):
    if shape.get() == "x":
        computer_shape = "o"
    else:
        computer_shape = "x"
    count = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if button_list[i][j]["text"] == " ":
                count += 1
    if count == 9:
        rand_row = random.choice([0, 2])
        rand_col = random.choice([0, 2])
        button_list[rand_row][rand_col].config(text = computer_shape)
        return
    if count == 8:
        if button_list[1][1]["text"] == " ":
            button_list[1][1].config(text = computer_shape)
        else:
            button_list[0][0].config(text = computer_shape)
        return
    if can_win(computer_shape) != [-1, -1]:
        button_list[can_win(computer_shape)[0]][can_win(computer_shape)[1]].config(text = computer_shape)
        return
    if can_win(shape.get()) != [-1, -1]:
        button_list[can_win(shape.get())[0]][can_win(shape.get())[1]].config(text = computer_shape)
        return
    if count == 7 and button_list[1][1]["text"] == " ":
        for i in range(0, 3):
            for j in range(0, 3):
                if button_list[i][j]["text"] == shape.get():
                    player_position = [i, j]
                if button_list[i][j]["text"] == computer_shape:
                    computer_position = [i, j]
        first_position = [computer_position[0]]
        if computer_position[1] == 2:
            first_position.append(computer_position[1] - 2)
        else:
            first_position.append(computer_position[1] + 2)
        second_position = []
        if computer_position[0] == 2:
            second_position.append(computer_position[0] - 2)
        else:
            second_position.append(computer_position[0] + 2)
        second_position.append(computer_position[1])
        if abs(computer_position[0] - player_position[0]) == 2 and abs(computer_position[1] - player_position[1]) == 2:
            if random.choice([1, 2]) == 1:
                button_list[first_position[0]][first_position[1]].config(text = computer_shape)
                return
            elif random.choice([1, 2]) == 2:
                button_list[second_position[0]][second_position[1]].config(text = computer_shape)
                return
        if player_position[0] == first_position[0] or player_position[1] == first_position[1]:
            button_list[second_position[0]][second_position[1]].config(text = computer_shape)
            return
        if player_position[0] == second_position[0] or player_position[1] == second_position[1]:
            button_list[first_position[0]][first_position[1]].config(text = computer_shape)
            return
    executed = False
    index_trap_dict = {}
    for i in range(0, 3):
        for j in range(0, 3):
            if button_list[i][j]["text"] == " ":
                index_trap_dict[(i, j)] = no_of_trap(i, j, computer_shape)
                executed = True
    if executed == True:
        max_trap = max(list(index_trap_dict.values()))
        corner = []
        non_corner = []
        for i in index_trap_dict:
            if index_trap_dict[i] == max_trap:
                if i[0] == i[1] or i[0] + i[1] == 2:
                    corner.append(i)
                else:
                    non_corner.append(i)
        if button_list[1][1]["text"] == computer_shape:
            if len(non_corner) != 0:
                random_index = random.choice(non_corner)
            else:
                random_index = random.choice(corner)
        else:
            if len(corner) != 0:
                random_index = random.choice(corner)
            else:
                random_index = random.choice(non_corner)
        button_list[random_index[0]][random_index[1]].config(text = computer_shape)
        return

def clicked(window, shape, row, col):
    if window == False:
        if button_list[row][col]["text"] == " ":
            button_list[row][col].config(text = (label["text"].split("'s"))[0])
            if (label["text"].split("'s"))[0] == "x":
                label.config(text = "o's turn")
                if check_winner("x", "lawn green"):
                    label.config(text = "x won")
                    modify()
                    return
            else:
                label.config(text = "x's turn")
                if check_winner("o", "lawn green"):
                    label.config(text = "o won")
                    modify()
                    return
    else:
        if button_list[row][col]["text"] == " ":
            button_list[row][col].config(text = shape.get())
            if check_winner(shape.get(), "lawn green"):
                label.config(text = "You Won")
                modify()
                return
            computer_move(shape)
            if shape.get() == "x":
                computer_shape = "o"
            else:
                computer_shape = "x"
            if check_winner(computer_shape, "tan1"):
                label.config(text = "You Lost")
                modify()
                return
    if is_draw():
        label.config(text = "Draw")
        modify()

def start_game(window, turn, shape):
    global label, button_list
    game_window = tkinter.Toplevel()
    game_window.geometry("+500+170")
    if window == False:
        game_window.title("Tic Tac Toe With Friend")
        label = ttk.Label(game_window, text = "x's turn", font = ("Agency FB", 14))
    else:
        window.destroy()
        game_window.title("Tic Tac Toe With Computer")
        label = ttk.Label(game_window, font = ("Agency FB", 14))
    label.grid(row = 0, column = 3)
    button_list = []
    for i in range (0, 3):
        sub_list = []
        for j in range(0, 3):
            button = tkinter.Button(game_window, text = " ", command = lambda row = i, col = j : clicked(window, shape, row, col))
            button.config(height = 2, width = 5, font = ("Constantia", 14))
            button.grid(row = i, column = j)
            sub_list.append(button)
        button_list.append(sub_list)
    if window != False:
        if turn.get() == 0:
            computer_move(shape)
    restart = ttk.Button(game_window, text = "Restart", command = lambda : clear(turn, shape))
    quit = ttk.Button(game_window, text = "Quit", command = game_window.destroy)
    restart.grid(row = 1, column = 3, padx = 10)
    quit.grid(row = 2, column = 3, padx = 20)
    game_window.mainloop()

def submit_data(customize_window, turn_var, shape_var):
    if turn_var.get() == -1 or shape_var.get() == " ":
        error_window = tkinter.Toplevel()
        error_window.geometry("+525+120")
        error_window.title("Error")
        if turn_var.get() == -1:
            ttk.Label(error_window, text = "Select yes or no").pack()
        if shape_var.get() == " ":
            ttk.Label(error_window, text = "Select one of the shapes").pack()
        ttk.Button(error_window, text = "OK", command = error_window.destroy).pack()
        error_window.mainloop()
    else:
        start_game(customize_window, turn_var, shape_var)

def customize_game():
    customize_window = tkinter.Toplevel()
    customize_window.title("Select your choices")
    customize_window.geometry("+500+240")
    turn = ttk.Label(customize_window, text = "  Do you want to play first     ")
    turn_var = tkinter.IntVar()
    turn_var.set(-1)
    yes = ttk.Radiobutton(customize_window, text = "YES    ", variable = turn_var, value = 1)
    no = ttk.Radiobutton(customize_window, text = "NO", variable = turn_var, value = 0)
    turn.grid(row = 0, column = 0)
    yes.grid(row = 0, column = 1)
    no.grid(row = 0, column = 2)
    shape = ttk.Label(customize_window, text = "Select your shape")
    shape_var = tkinter.StringVar()
    shape_var.set(" ")
    cross = ttk.Radiobutton(customize_window, text = "X", variable = shape_var, value = "x")
    circle = ttk.Radiobutton(customize_window, text = "O", variable = shape_var, value = "o")
    shape.grid(row = 1, column = 0)
    cross.grid(row = 1, column = 1)
    circle.grid(row = 1, column = 2)
    start_button = ttk.Button(customize_window, text = "Start Game", command = lambda : submit_data(customize_window, turn_var, shape_var))
    start_button.grid(row = 2, column = 1, columnspan = 2)
    customize_window.mainloop()

def my_info():
    info_window = tkinter.Toplevel()
    info_window.geometry("+10+170")
    info_window.title("Credit")
    ttk.Label(info_window, text = "SUNNY KUMAR", font = ("Times New Roman", 18)).pack()
    ttk.Label(info_window, text = "B Tech in CSE", font = ("Times New Roman", 16)).pack()
    ttk.Label(info_window, text = "Chandigarh University", font = ("Times New Roman", 14)).pack()
    ttk.Label(info_window, text = "2021-2025", font = ("Times New Roman", 12)).pack()
    info_window.mainloop()

window = tkinter.Tk()
window.title("Tic Tac Toe")
window.geometry("+230+60")
picture = tkinter.PhotoImage(file = "Tic Tac Toe.png")
ttk.Label(window, image = picture).pack()
ttk.Button(window, text = "Credit", command = my_info).pack()
ttk.Button(window, text = "Multiplayer Game", command = lambda : start_game(False, -1, " ")).pack()
ttk.Button(window, text = "Play With Computer", command = lambda : customize_game()).pack()
ttk.Button(window, text = "Quit Application", command = window.destroy).pack()
window.mainloop()