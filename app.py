import base64
import streamlit as st

import numpy as np
import pandas as pd
from PIL import Image
from shopping_for_players.computer import predictor


st.markdown("""# Shopping for players
## value prediction
Give us some feauters and we provide you their market value """)

image = Image.open('web/football.jpg')
st.image(image, caption='Football is life', width=25, use_column_width=True)

columns = st.columns(6)


age = columns[0].text_input("Age",  "")
columns[0].write(age)

height = columns[1].text_input("Height",  "")
columns[1].write(height)

goals = columns[2].text_input("Goals",  "")
columns[2].write(goals)

goals_against = columns[3].text_input("Goals against",  "")
columns[3].write(goals_against)

yellow_cards = columns[4].text_input("Yellow cards", "")
columns[4].write(yellow_cards)

red_cards = columns[5].text_input("Red cards", "")
columns[5].write(red_cards)

columns = st.columns([1, 1,2,3])

games = columns[0].text_input("Games",  "")
columns[0].write(games)


term_days_remaining = columns[1].text_input("Term days remaining", "")
columns[1].write(term_days_remaining)

with columns[2]:
    with st.expander("Position"):
        st.radio("Position", ["Goalkeeper", "Defender", "Midfield", "Attack"])
#expander = st.expander("Position")
#expander.radio("Position",["Goalkepper", "Defender", "Midfield","Attack"])

with columns[3]:
    competitions = {
     'UKR1', 'DK1', 'GR1', 'SC1', 'BE1', 'RU1', 'NL1', 'TR1', 'PO1', 'FR1', 'L1', 'IT1', 'ES1', 'GB1'
}
    clubs = { 'Fk Minaj', 'Pfk Lviv', 'Gaziantep Fk', 'Ingulets Petrove', 'Kryvbas Kryvyi Rig', 'Metal Kharkiv', 'Nk Veres Rivne', 'Metalist 1925 Kharkiv', 'Chornomorets Odessa', 'Motherwell Fc', 'Dundee United Fc', 'Pas Lamia 1964', 'Pas Giannina', 'Lyngby Bk', 'Kilmarnock Fc', 'Rukh Lviv', 'Fk Oleksandriya', 'Ac Horsens', 'Kolos Kovalivka', 'Asteras Tripolis', 'Aberdeen Fc', 'Ross County Fc', 'St Mirren Fc', 'Go Ahead Eagles Deventer', 'St Johnstone Fc', 'Livingston Fc', 'Viborg Ff', 'Fakel Voronezh', 'Fc Volendam', 'Volos Nps', 'Ionikos Nikeas', 'Ofi Kreta', 'Torpedo Moskau', 'Istanbulspor', 'Fc Emmen', 'Apo Levadiakos', 'Panetolikos Gfs', 'Odense Boldklub', 'Rfc Seraing', 'Zorya Lugansk', 'Portimonense Sc', 'Sbv Excelsior Rotterdam', 'Gd Chaves', 'Heart Of Midlothian Fc', 'Vorskla Poltava', 'Aarhus Gf', 'Rio Ave Fc', 'Sv Zulte Waregem', 'Vv St Truiden', 'Fk Nizhny Novgorod', 'Umraniyespor', 'Sparta Rotterdam', 'Aalborg Bk', 'Boavista Porto Fc', 'Silkeborg If', 'Randers Fc', 'Kv Oostende', 'Ural Ekaterinburg', 'Fc Pacos De Ferreira', 'Fc Vizela', 'Casa Pia Ac', 'Rkc Waalwijk', 'Kas Eupen', 'Fc Arouca', 'Sc Cambuur Leeuwarden', 'Nec Nijmegen', 'Atromitos Athen', 'Fk Orenburg', 'Fk Sochi', 'Kv Kortrijk', 'Cd Santa Clara', 'Cs Maritimo', 'Fk Khimki', 'Hibernian Fc', 'Ac Ajaccio', 'Gd Estoril Praia', 'Fc Famalicao', 'Fortuna Sittard', 'Kvc Westerlo', 'Akhmat Grozny', 'Giresunspor', 'Mke Ankaragucu', 'Kv Mechelen', 'Kayserispor', 'Brondby If', 'Vitoria Guimaraes Sc', 'Sivasspor', 'Fc Twente Enschede', 'Fatih Karagumruk', 'Vitesse Arnheim', 'Sc Heerenveen', 'Cercle Brugge', 'Hatayspor', 'Dynamo Kiew', 'Alanyaspor', 'Kasimpasa', 'Krylya Sovetov Samara', 'Fc Midtjylland', 'Aj Auxerre', 'Aris Thessaloniki', 'Fk Rostov', 'Fc Nordsjaelland', 'Gil Vicente Fc', 'Fc Utrecht', 'Adana Demirspor', 'Antalyaspor', 'Aek Athen', 'Oud Heverlee Leuven', 'Fc Schalke 04', 'Konyaspor', 'Paok Thessaloniki', 'Clermont Foot 63', 'Sco Angers', 'Standard Luttich', 'Fc Groningen', 'Vfl Bochum', 'Rsc Charleroi', 'Shakhtar Donetsk', 'Istanbul Basaksehir Fk', 'Sampdoria Genua', 'Hellas Verona', 'Fc Cadiz', 'Us Cremonese', '1 Fc Koln', 'Fc Toulouse', 'Sk Dnipro 1', 'Panathinaikos Athen', 'Royale Union Saint Gilloise', 'Kaa Gent', 'Krc Genk', 'Rc Strassburg Alsace', 'Fk Krasnodar', 'Stade Brest 29', 'Spezia Calcio', 'Fc Elche', 'Us Lecce', 'Vfb Stuttgart', 'Fc Empoli', 'Fc Kopenhagen', 'Lokomotiv Moskau', 'Hertha Bsc', 'Olympiakos Piraus', 'Real Valladolid', 'Es Troyes Ac', 'Royal Antwerpen Fc', 'Sv Werder Bremen', 'Fc Augsburg', 'Az Alkmaar', 'Rcd Mallorca', 'Stade Reims', 'Zska Moskau', 'Rsc Anderlecht', 'Spartak Moskau', 'Fc Lorient', '1 Fsv Mainz 05', 'Rayo Vallecano', 'Ud Almeria', 'Espanyol Barcelona', 'Ac Monza', '1 Fc Union Berlin', 'Feyenoord Rotterdam', 'Dinamo Moskau', 'Glasgow Rangers', 'Celtic Glasgow', 'Fc Girona', 'Montpellier Hsc', 'Brighton Amp Hove Albion', 'Rc Lens', 'Ca Osasuna', 'Celta Vigo', 'Fc Nantes', 'Udinese Calcio', 'Fc Bologna', 'Sc Braga', 'Trabzonspor', 'Us Salernitana 1919', 'Besiktas Istanbul', 'Tsg 1899 Hoffenheim', 'Zenit St Petersburg', 'Psv Eindhoven', 'Fenerbahce Istanbul', 'Fc Getafe', 'Fc Turin', 'Vfl Wolfsburg', 'Borussia Monchengladbach', 'Sc Freiburg', 'Fc Brugge', 'Fc Valencia', 'Galatasaray Istanbul', 'Olympique Lyon', 'Afc Bournemouth', 'Us Sassuolo', 'Lazio Rom', 'Sporting Lissabon', 'Nottingham Forest', 'Fc Porto', 'Olympique Marseille', 'Fc Sevilla', 'Ac Florenz', 'Ogc Nizza', 'Fc Fulham', 'As Monaco', 'Fc Southampton', 'Athletic Bilbao', 'Ajax Amsterdam', 'Losc Lille', 'Real Betis Sevilla', 'Leeds United', 'Real Sociedad San Sebastian', 'Atalanta Bergamo', 'Wolverhampton Wanderers', 'Fc Everton', 'Eintracht Frankfurt', 'Benfica Lissabon', 'Ac Mailand', 'As Rom', 'Fc Brentford', 'Crystal Palace', 'Borussia Dortmund', 'Fc Stade Rennes', 'Fc Villarreal', 'Juventus Turin', 'Newcastle United', 'Aston Villa', 'West Ham United', 'Leicester City', 'Bayer 04 Leverkusen', 'Rasenballsport Leipzig', 'Atletico Madrid', 'Ssc Neapel', 'Inter Mailand', 'Manchester United', 'Fc Chelsea', 'Real Madrid', 'Fc Bayern Munchen', 'Fc Arsenal', 'Fc Barcelona', 'Tottenham Hotspur', 'Fc Liverpool', 'Fc Paris Saint Germain', 'Manchester City'}
    with st.expander("Select Competition"):
        selected_competition = st.selectbox("Select a competition", competitions )

    with st.expander("Select Club"):
        selected_club = st.selectbox("Select a club", clubs)


if st.button('Tell me the value 😉 '):
    # print is visible in the server output, not in the page
    value = predictor(age=int(age),height_in_cm=int(height),goals_2022=int(goals),goals_against_2022=int(goals_against),
                      yellow_cards_2022=int(yellow_cards),red_cards_2022=int(red_cards),games_2022=int(games),
                      term_days_remaining=int(term_days_remaining),
                      current_club_domestic_competition_id=selected_competition,current_club_name=selected_club)
    st.write(f'Surprise 😲 Your Value equals 🥳 {value}')
