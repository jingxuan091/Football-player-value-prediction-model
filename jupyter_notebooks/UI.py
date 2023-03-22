import streamlit as st

import numpy as np
import pandas as pd

st.markdown("""# Shopping for players
## value prediction
Give us a player name and we provide you their market value""")

title = st.text_input('Player name', '')
st.write('The player name is', title)

if st.button('calculate '):
    # print is visible in the server output, not in the page
    st.write('button clicked!')
