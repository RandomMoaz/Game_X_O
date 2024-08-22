import random
from tkinter import *

def next_turn(row, col):
    global player
    if game_btns[row][col]['text'] == "" and not check_winner():
        game_btns[row][col]['text'] = player

        if check_winner():
            label.config(text=(player + " wins!"))
            update_score(player)
        elif not check_empty_spaces():
            label.config(text="Tie, No Winner!")
        else:
            player = players[1] if player == players[0] else players[0]
            label.config(text=(player + " turn"))

def check_winner():
    # Winning conditions
    winning_combinations = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]

    for combination in winning_combinations:
        if all(game_btns[row][col]['text'] == player for row, col in combination):
            for row, col in combination:
                game_btns[row][col].config(bg="cyan")
            return True

    return False

def check_empty_spaces():
    return any(game_btns[row][col]['text'] == "" for row in range(3) for col in range(3))

def start_new_game():
    global player
    player = random.choice(players)
    label.config(text=(player + " turn"))
    for row in range(3):
        for col in range(3):
            game_btns[row][col].config(text="", bg="#F0F0F0")

def update_score(winner):
    scores[winner] += 1
    score_label.config(text=f"X: {scores['x']}  O: {scores['o']}")

# Initialize main window
window = Tk()
window.title("Tic-Tac-Toe")

players = ["x", "o"]
player = random.choice(players)
scores = {"x": 0, "o": 0}

# Create UI elements
label = Label(text=(player + " turn"), font=('consolas', 40))
label.pack(side="top")

restart_btn = Button(text="Restart", font=('consolas', 20), command=start_new_game)
restart_btn.pack(side="top")

score_label = Label(text=f"X: {scores['x']}  O: {scores['o']}", font=('consolas', 20))
score_label.pack(side="top")

btns_frame = Frame(window)
btns_frame.pack()

game_btns = [[Button(btns_frame, text="", font=('consolas', 50), width=4, height=1,
                     command=lambda row=row, col=col: next_turn(row, col))
              for col in range(3)] for row in range(3)]

for row in range(3):
    for col in range(3):
        game_btns[row][col].grid(row=row, column=col)

window.mainloop()
