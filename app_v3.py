import base64
import streamlit as st

import numpy as np
import pandas as pd
from PIL import Image
from shopping_for_players.computer import predictor
import pickle

#@st.cache_data
def import_models_and_transformers():
    model_Attack = pickle.load(open("models/Attack_model.pickle", "rb"))
    transformer_Attack= pickle.load(open("models/Attack_transformer.pickle", "rb"))
    model_Defender = pickle.load(open("models/Defender_model.pickle", "rb"))
    transformer_Defender= pickle.load(open("models/Defender_transformer.pickle", "rb"))
    model_Goalkeeper = pickle.load(open("models/Goalkeeper_model.pickle", "rb"))
    transformer_Goalkeeper = pickle.load(open("models/Goalkeeper_transformer.pickle", "rb"))
    model_Midfield= pickle.load(open("models/Midfield_model.pickle", "rb"))
    transformer_Midfield= pickle.load(open("models/Midfield_transformer.pickle", "rb"))
    return model_Attack, \
           transformer_Attack, \
           model_Defender, \
           transformer_Defender, \
           model_Goalkeeper, \
           transformer_Goalkeeper, \
           model_Midfield, \
           transformer_Midfield

# with open("models/Midfield_model.pikle", 'r') as f:
#     # load using pickle de-serializer
#     model_Midfield = pickle.load(f)

st.markdown("""# Shopping for players
## value prediction
Give us some feauters and we provide you their market value """)

image = Image.open('web/football.jpg')
st.image(image, caption='Football is life', width=25, use_column_width=True)

columns =  st.columns(3)
name = columns[1].text_input("Name" , "")
columns[1].write(name)

columns = st.columns(4)

age = columns[0].text_input("Age",  "")
columns[0].write(age)

height = columns[1].text_input("Height",  "")
columns[1].write(height)

goals = columns[2].text_input("Goals",  "")
columns[2].write(goals)

goals_against = columns[3].text_input("Goals against",  "")
columns[3].write(goals_against)

columns = st.columns(4)

yellow_cards = columns[0].text_input("Yellow cards", "")
columns[0].write(yellow_cards)

red_cards = columns[1].text_input("Red cards", "")
columns[1].write(red_cards)

games = columns[2].text_input("Games",  "")
columns[2].write(games)

term_days_remaining = columns[3].text_input("Term days remaining", "")
columns[3].write(term_days_remaining)

columns = st.columns([1, 1,])


with columns[0]:
    with st.expander("Position"):
        position = st.radio("Position", ["Goalkeeper", "Defender", "Midfield", "Attack"])

#expander = st.expander("Position")
#expander.radio("Position",["Goalkepper", "Defender", "Midfield","Attack"])

with columns[1]:
    competitions = {'UKR1', 'DK1', 'GR1', 'SC1', 'BE1', 'RU1', 'NL1', 'TR1', 'PO1', 'FR1', 'L1', 'IT1', 'ES1', 'GB1'}
    clubs_by_competition = {
        'UKR1': {'Metal Kharkiv', 'Metalist 1925 Kharkiv', 'Pfk Lviv', 'Ingulets Petrove', 'Nk Veres Rivne', 'Fk Minaj', 'Kryvbas Kryvyi Rig', 'Rukh Lviv', 'Fk Oleksandriya', 'Zorya Lugansk', 'Dynamo Kiew', 'Vorskla Poltava', 'Shakhtar Donetsk', 'Chornomorets Odessa', 'Kolos Kovalivka', 'Sk Dnipro 1'},
        'DK1': {'Lyngby Bk', 'Fc Midtjylland', 'Aalborg Bk', 'Fc Kopenhagen', 'Aarhus Gf', 'Odense Boldklub', 'Fc Nordsjaelland', 'Silkeborg If', 'Ac Horsens', 'Randers Fc', 'Brondby If', 'Viborg Ff'},
        'GR1': {'Ionikos Nikeas', 'Panetolikos Gfs', 'Panathinaikos Athen', 'Aek Athen', 'Pas Lamia 1964', 'Pas Giannina', 'Atromitos Athen', 'Ofi Kreta', 'Asteras Tripolis', 'Olympiakos Piraus', 'Paok Thessaloniki', 'Aris Thessaloniki', 'Volos Nps', 'Apo Levadiakos'},
        'SC1': {'Kilmarnock Fc', 'Livingston Fc', 'Dundee United Fc', 'Ross County Fc', 'Celtic Glasgow', 'St Mirren Fc', 'Aberdeen Fc', 'Motherwell Fc', 'Hibernian Fc', 'Glasgow Rangers', 'Heart Of Midlothian Fc', 'St Johnstone Fc'},
        'BE1': {'Vv St Truiden', 'Fc Brugge', 'Sv Zulte Waregem', 'Rfc Seraing', 'Kas Eupen', 'Kvc Westerlo', 'Kv Oostende', 'Royale Union Saint Gilloise', 'Kv Mechelen', 'Kv Kortrijk', 'Cercle Brugge', 'Royal Antwerpen Fc', 'Rsc Charleroi', 'Krc Genk', 'Standard Luttich', 'Kaa Gent', 'Oud Heverlee Leuven', 'Rsc Anderlecht'},
        'RU1': {'Fakel Voronezh', 'Torpedo Moskau', 'Fk Khimki', 'Fk Orenburg', 'Krylya Sovetov Samara', 'Lokomotiv Moskau', 'Fk Krasnodar', 'Zenit St Petersburg', 'Akhmat Grozny', 'Zska Moskau', 'Dinamo Moskau', 'Fk Sochi', 'Fk Nizhny Novgorod', 'Ural Ekaterinburg', 'Spartak Moskau', 'Fk Rostov'},
        'NL1': {'Go Ahead Eagles Deventer', 'Sparta Rotterdam', 'Fc Volendam', 'Fc Emmen', 'Fortuna Sittard', 'Sc Heerenveen', 'Vitesse Arnheim', 'Fc Twente Enschede', 'Rkc Waalwijk', 'Ajax Amsterdam', 'Az Alkmaar', 'Psv Eindhoven', 'Fc Groningen', 'Fc Utrecht', 'Sbv Excelsior Rotterdam', 'Sc Cambuur Leeuwarden', 'Feyenoord Rotterdam', 'Nec Nijmegen'},
        'TR1': {'Umraniyespor', 'Hatayspor', 'Istanbulspor', 'Sivasspor', 'Kayserispor', 'Adana Demirspor', 'Kasimpasa', 'Konyaspor', 'Antalyaspor', 'Fatih Karagumruk', 'Alanyaspor', 'Gaziantep Fk', 'Trabzonspor', 'Mke Ankaragucu', 'Istanbul Basaksehir Fk', 'Fenerbahce Istanbul', 'Galatasaray Istanbul', 'Besiktas Istanbul', 'Giresunspor'},
        'PO1': {'Gd Chaves', 'Fc Vizela', 'Boavista Porto Fc', 'Portimonense Sc', 'Cd Santa Clara', 'Gd Estoril Praia', 'Fc Arouca', 'Fc Pacos De Ferreira', 'Sc Braga', 'Sporting Lissabon', 'Benfica Lissabon', 'Rio Ave Fc', 'Vitoria Guimaraes Sc', 'Fc Famalicao', 'Casa Pia Ac', 'Cs Maritimo', 'Gil Vicente Fc', 'Fc Porto'},
        'FR1': {'Ac Ajaccio', 'Es Troyes Ac', 'Fc Toulouse', 'Clermont Foot 63', 'Stade Reims', 'Rc Strassburg Alsace', 'Losc Lille', 'Rc Lens', 'Olympique Lyon', 'Fc Stade Rennes', 'Fc Paris Saint Germain', 'Sco Angers', 'As Monaco', 'Montpellier Hsc', 'Aj Auxerre', 'Stade Brest 29', 'Olympique Marseille', 'Fc Lorient', 'Ogc Nizza', 'Fc Nantes'},
        'L1':  {'Fc Bayern Munchen', 'Fc Schalke 04', 'Sv Werder Bremen', '1 Fc Koln', 'Fc Augsburg', 'Vfb Stuttgart', 'Tsg 1899 Hoffenheim', 'Borussia Monchengladbach', 'Rasenballsport Leipzig', 'Borussia Dortmund', 'Hertha Bsc', 'Bayer 04 Leverkusen', 'Sc Freiburg', 'Vfl Wolfsburg', 'Vfl Bochum', 'Eintracht Frankfurt', '1 Fc Union Berlin', '1 Fsv Mainz 05'},
        'IT1': {'Us Cremonese', 'Sampdoria Genua', 'Us Lecce', 'Ac Monza', 'Fc Bologna', 'Hellas Verona', 'Atalanta Bergamo', 'As Rom', 'Inter Mailand', 'Fc Empoli', 'Ac Florenz', 'Juventus Turin', 'Ac Mailand', 'Lazio Rom', 'Ssc Neapel', 'Fc Turin', 'Spezia Calcio', 'Us Sassuolo', 'Udinese Calcio', 'Us Salernitana 1919'},
        'ES1': {'Fc Cadiz', 'Rayo Vallecano', 'Real Valladolid', 'Fc Elche', 'Fc Girona', 'Celta Vigo', 'Ud Almeria', 'Real Betis Sevilla', 'Fc Getafe', 'Athletic Bilbao', 'Ca Osasuna', 'Real Sociedad San Sebastian', 'Atletico Madrid', 'Fc Barcelona', 'Real Madrid', 'Espanyol Barcelona', 'Fc Valencia', 'Fc Sevilla', 'Fc Villarreal', 'Rcd Mallorca'},
        'GB1': {'Leeds United', 'Afc Bournemouth', 'Fc Fulham', 'Fc Brentford', 'Fc Everton', 'Wolverhampton Wanderers', 'Leicester City', 'West Ham United', 'Newcastle United', 'Brighton Amp Hove Albion', 'Aston Villa', 'Fc Arsenal', 'Fc Southampton', 'Tottenham Hotspur', 'Manchester City', 'Fc Liverpool', 'Fc Chelsea', 'Manchester United', 'Crystal Palace', 'Nottingham Forest'}
    }
    with st.expander("Select Competition"):
        selected_competition = st.selectbox("Select a competition", list(competitions))
    with st.expander("Select Club"):
        clubs = clubs_by_competition[selected_competition]
        selected_club = st.selectbox("Select a club", list(clubs))

model_Attack, \
transformer_Attack, \
model_Defender, \
transformer_Defender, \
model_Goalkeeper, \
transformer_Goalkeeper, \
model_Midfield, \
transformer_Midfield = import_models_and_transformers()


if position == "Attack":
    model = model_Attack
    transformer = transformer_Attack
elif position == "Defender":
    model = model_Defender
    transformer = transformer_Defender
elif position == "Goalkeeper":
    model = model_Goalkeeper
    transformer = transformer_Goalkeeper
else:
    model = model_Midfield
    transformer = transformer_Midfield

if st.button('Tell me the value 😉'):
    value = predictor(age=int(age), height_in_cm=int(height), goals_for_2022=int(goals), goals_against_2022=int(goals_against),
                      yellow_cards_2022=int(yellow_cards), red_cards_2022=int(red_cards), games_2022=int(games),
                      term_days_remaining=int(term_days_remaining),
                      current_club_domestic_competition_id=selected_competition,
                      current_club_name=selected_club,model=model,transformer=transformer)

    float_value = float(value)
    formatted_value = '{:,.2f} €'.format(float_value)
    st.markdown(f'<div style="font-size: xx-large; color: #ff5733;">Surprise {name} 😲  Your market value = 🥳 {formatted_value}</div>', unsafe_allow_html=True)
