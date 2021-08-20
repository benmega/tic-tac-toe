import tkinter as tk
from tkinter import messagebox

top = tk.Tk()
turn = 'X'


def button_press(j):
    global turn

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    if str(buttonText[j].get()) == '':
        buttonText[j].set(turn)
    else:
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    # Check if the game is over.  Should this be a separate function?
    if any(all(buttonText[j].get() == "X" for j in range(k, k + 3)) for k in range(0, 7, 3)):  # horizontal X's
        messagebox.showinfo("Ben Mega Creations", "X wins!")
        resetGame()

    if buttonText[2].get() != '' and all(buttonText[j].get() == buttonText[2].get() for j in [2, 4, 6]):  # positive slope diagonal
        messagebox.showinfo("Ben Mega Creations", buttonText[2].get() + " wins!")
        resetGame()

    if buttonText[0].get() != '' and all(buttonText[j].get() == buttonText[0].get() for j in [0, 4, 8]):  # negative slope diagonal
        messagebox.showinfo("Ben Mega Creations", buttonText[0].get() + " wins!")
        resetGame()

    if any(all(buttonText[j].get() == "X" for j in [k, k + 3, k + 6]) for k in range(3)):  # vertical X's
        messagebox.showinfo("Ben Mega Creations", "X wins!")
        resetGame()

    if any(all(buttonText[j].get() == "O" for j in range(k, k + 3)) for k in range(0, 7, 3)):  # horizontal O's
        messagebox.showinfo("Ben Mega Creations", "O wins!")
        resetGame()

    if any(all(buttonText[j].get() == "O" for j in [k, k + 3, k + 6]) for k in range(3)):  # vertical O's
        messagebox.showinfo("Ben Mega Creations", "O wins!")
        resetGame()

    if all(buttonText[j].get() != "" for j in range(len(buttonText))):  # Tie
        messagebox.showinfo("Ben Mega Creations", "Cat's Game!")
        resetGame()


def resetGame():
    for k in range(9):
        buttonText[k].set('')


top.geometry("450x450")
top.resizable(False,False)

# Create 3x3 grid of buttons and set their command to button_press
buttons = []
buttonText = []
for i in range(9):
    buttonText.append(tk.StringVar())
    buttons.append(tk.Button(top, textvariable=buttonText[i], command=lambda m=i: button_press(m), width=3,
                             height=1, font=("helvetica",60)))
    buttons[i].grid(row=i // 3, column=i % 3)

top.mainloop()
