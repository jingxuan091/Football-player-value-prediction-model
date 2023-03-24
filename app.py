import base64
import streamlit as st

import numpy as np
import pandas as pd
from PIL import Image



st.markdown("""# Shopping for players
## value prediction
Give us some feauters and we provide you their market value """)

image = Image.open('football.jpg')
st.image(image, caption='Football is life', width=25, use_column_width=True)

columns = st.columns(5)


age = columns[0].text_input("Age",  "")
columns[0].write(age)

goals = columns[1].text_input("Goals",  "")
columns[1].write(goals)

goals_against = columns[2].text_input("Goals against",  "")
columns[2].write(goals_against)

yellow_cards = columns[3].text_input("Yellow cards", "")
columns[3].write(yellow_cards)

red_cards = columns[4].text_input("Red cards", "")
columns[4].write(red_cards)

columns = st.columns([1, 1,2])

games = columns[0].text_input("Games",  "")
columns[0].write(games)


term_days_remaining = columns[1].text_input("Term days remaining", "")
columns[1].write(term_days_remaining)

with columns[2]:
    with st.expander("Position"):
        st.radio("Position", ["Goalkeeper", "Defender", "Midfield", "Attack"])
#expander = st.expander("Position")
#expander.radio("Position",["Goalkepper", "Defender", "Midfield","Attack"])



if st.button('Tell me the value 😉 '):
    # print is visible in the server output, not in the page
    st.write('Surprise 😲 Your Value equals 🥳')
