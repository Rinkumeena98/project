import streamlit as st

# Initialize session state variables
if 'board' not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.current_player = "x"
    st.session_state.winner = False

# Function to check for a winner
def check_winner():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
        [0, 4, 8], [2, 4, 6]              # diagonal
    ]
    for combo in winning_combinations:
        if st.session_state.board[combo[0]] == st.session_state.board[combo[1]] == st.session_state.board[combo[2]] != "":
            return st.session_state.board[combo[0]]  # Return the winner ('x' or 'o')
    return None

# Function to handle button click
def button_click(index):
    if st.session_state.board[index] == "" and not st.session_state.winner:
        st.session_state.board[index] = st.session_state.current_player
        winner = check_winner()
        if winner:
            st.session_state.winner = winner
            st.success(f"Player {winner} wins!")
        else:
            st.session_state.current_player = "o" if st.session_state.current_player == "x" else "x"

# Streamlit interface layout
st.title("Tic-Tac-Toe Game")
st.write(f"Player {st.session_state.current_player}'s turn")

# Display the game board
col1, col2, col3 = st.columns(3)

for i in range(3):
    with [col1, col2, col3][i]:
        buttons = []
        for j in range(3):
            index = i * 3 + j
            button_text = st.session_state.board[index] if st.session_state.board[index] != "" else ""
            if st.button(button_text or " ", key=index):
                button_click(index)

# Display reset button
if st.button("Restart Game"):
    st.session_state.board = [""] * 9
    st.session_state.current_player = "x"
    st.session_state.winner = False

