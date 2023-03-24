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

columns = st.columns(6)

club = columns[0].text_input("Club", "")
columns[0].write(club)

age = columns[1].text_input("Age",  "")
columns[1].write(age)

goals = columns[2].text_input("Goals",  "")
columns[2].write(goals)

minutes_played = columns[3].text_input("Minutes played",  "")
columns[3].write(minutes_played)

yellow_cards = columns[4].text_input("Yellow cards", "")
columns[4].write(yellow_cards)

position = columns[5].text_input("Position", "")
columns[5].write(position)



if st.button('Tell me the value 😉 '):
    # print is visible in the server output, not in the page
    st.write('Surprise 😲 Your Value equals 🥳')
