from sklearn.model_selection import train_test_split, cross_validate
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.feature_selection import SelectPercentile, mutual_info_regression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OrdinalEncoder, MinMaxScaler, OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer, KNNImputer
# VIEWING OPTIONS IN THE NOTEBOOK
from sklearn import set_config; set_config(display='diagram')
import pandas as pd
import numpy as np

def predictor(games_2022=20,minutes_played_2022=1800,goals_2022=200,assists_2022=15,goals_against_2022=150,
              goals_for_2022=10,clean_sheet_2022=7,height_in_cm=186,age=31,club_value=15e8,squad_size=18,
              term_days_remaining=200,value_goals_for_2022=15e8,yellow_cards_2022=2,red_cards_2022=0,
              sub_position="Left Winger",foot="Right",country_of_citizenship="Italy",
              current_club_domestic_competition_id="IT1",current_club_name="Juventus Turin",
              model=None, transformer=None):

    player = pd.DataFrame()
    player['games_2022'] =[games_2022]
    player['minutes_played_2022'] =[minutes_played_2022]
    player['goals_2022'] =[goals_2022]
    player['assists_2022'] =[assists_2022]
    player['goals_against_2022'] =[goals_against_2022]
    player['goals_for_2022'] =[goals_for_2022]
    player['clean_sheet_2022'] =[clean_sheet_2022]
    player['height_in_cm'] =[height_in_cm]
    player['age'] =[age]
    player['club_value'] =[club_value]
    player['squad_size'] =[squad_size]
    player['term_days_remaining'] =[term_days_remaining]
    player['value_goals_for_2022'] =[value_goals_for_2022]
    player['yellow_cards_2022'] =[yellow_cards_2022]
    player['red_cards_2022'] =[red_cards_2022]
    player['sub_position'] =[sub_position]
    player['foot'] =[foot]
    player['country_of_citizenship'] =[country_of_citizenship]
    player['current_club_domestic_competition_id'] =[current_club_domestic_competition_id]
    player['current_club_name'] = [current_club_name]

    player_transformed = transformer.transform(player)
    my_value = model.predict(player_transformed)
    return my_value
