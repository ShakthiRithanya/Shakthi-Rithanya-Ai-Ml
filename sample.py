def guessing_game():
    st.title("Guessing Game!!!")
    st.write("Guess a number between 1 to 100")

    # Initialize state variables
    if "low" not in st.session_state:
        st.session_state.low = 1
    if "high" not in st.session_state:
        st.session_state.high = 100
    if "mid" not in st.session_state:
        st.session_state.mid = (st.session_state.high + st.session_state.low) // 2
    if "game_over" not in st.session_state:
        st.session_state.game_over = False

    if not st.session_state.game_over:
        st.write(f"Is **{st.session_state.mid}** your guess?")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Yes"):
                st.session_state.game_over = True
        with col2:
            if st.button("No"):
                st.session_state.no_clicked = True

        if "no_clicked" in st.session_state and st.session_state.no_clicked:
            st.session_state.no_clicked = False
            st.write(f"Is your guess **less** or **greater** than **{st.session_state.mid}**?")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("Less"):
                    st.session_state.high = st.session_state.mid
                    st.session_state.mid = (st.session_state.high + st.session_state.low) // 2
            with col2:
                if st.button("Greater"):
                    st.session_state.low = st.session_state.mid
                    st.session_state.mid = (st.session_state.high + st.session_state.low) // 2
    else:
        st.success(f"HORRAY!!! We found your guess: {st.session_state.mid}")
        if st.button("Play Again"):
            st.session_state.low = 1
            st.session_state.high = 100
            st.session_state.mid = (st.session_state.high + st.session_state.low) // 2
            st.session_state.game_over = False

if __name__ == "__main__":
    guessing_game()

