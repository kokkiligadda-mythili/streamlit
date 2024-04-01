import streamlit as st
import numpy as np

st.title("Tic Tac Toe")

board = np.array([[" " for x in range(3)] for y in range(3)])
player = "X"

def draw_board():
    st.write("""
    |{}|{}|{}|
    ---------
    |{}|{}|{}|
    ---------
    |{}|{}|{}|
""".format(*board.flatten()))

def play_game():
    global player
    row = int(st.number_input("Choose row (1-3)", min_value=1, max_value=3)) - 1
    col = int(st.number_input("Choose col (1-3)", min_value=1, max_value=3)) - 1
    board[row][col] = player
    player = "O" if player == "X" else "X"
    draw_board()
    if check_win():
        st.write("Congratulations Player " + player + "! You won!")
        return True
    return False

def check_win():
    for i in range(3):
        if board[i, 0] == board[i, 1] == board[i, 2] != " ":
            return True
    for i in range(3):
        if board[0, i] == board[1, i] == board[2, i] != " ":
            return True
    if board[0, 0] == board[1, 1] == board[2, 2] != " ":
        return True
    if board[0, 2] == board[1, 1] == board[2, 0] != " ":
        return True

while(True):
    draw_board()
    if play_game():
        break
