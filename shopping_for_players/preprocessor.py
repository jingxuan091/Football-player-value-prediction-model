import pandas as pd
import numpy as np
import datetime as dt
import calendar
import datetime
from datetime import datetime, timedelta, date
import warnings

#settings
warnings.filterwarnings("ignore")


def players_df_preproc(players_df):
    #add year to game valuations
    now = datetime.now()
    players_df['date_of_birth'] = pd.to_datetime(players_df['date_of_birth'])
    players_df = players_df[players_df['date_of_birth'].isnull() == False]
    players_df['age'] = (now - players_df['date_of_birth']).apply(lambda x: x.days) / 365.25
    players_df['age'] = players_df['age'].round().astype(int)

    # Calculate the contract remaining of each player
    players_df['contract_expiration_date'] = pd.to_datetime(players_df['contract_expiration_date'])
    players_df = players_df[players_df['contract_expiration_date'].isnull() == False]
    players_df['term_days_remaining'] = (players_df['contract_expiration_date']- now).apply(lambda x: x.days)
    return players_df


def appearances_df_preproc(appearances_df):
    # add year to player appearances
    appearances_df['datetime']=pd.to_datetime(appearances_df['date'], format="%Y-%m-%d")
    appearances_df['year']=appearances_df['datetime'].dt.year
    appearances_df = appearances_df[(appearances_df.year > 2004 ) & (appearances_df.year < 2023 )]
    return appearances_df


def games_and_appearances_df_preproc(games_df,appearances_df):
    games_df['datetime']=pd.to_datetime(games_df['date'], format="%Y-%m-%d")
    games_df['year']=games_df['datetime'].dt.year
    games_df = games_df[(games_df.year > 2004 ) & (games_df.year < 2023 )]
    games_and_appearances_df = appearances_df.merge(games_df, on=['game_id'], how='left')
    return games_and_appearances_df


#create a function to collate player stats
def player_stats(player_id, season, games_and_appearances_df):

    df = games_and_appearances_df[games_and_appearances_df['player_id'] == player_id]
    df =  df[df['season'] == season]
    if (df.shape[0] == 0):
        Out = [(np.nan, season,0,0,0,0,0,0,0,0,0)]
        out_df = pd.DataFrame(data = Out, columns = ['player_id','season','goals','games',
                                                     'assists','minutes_played','goals_for',
                                                     'goals_against','clean_sheet',
                                                     'yellow_cards','red_cards'])
        return out_df
    else:
        df["goals_for"] = df.apply(lambda row: row['home_club_goals'] if row['home_club_id'] == row['player_club_id']
            else row['away_club_goals'] if row['away_club_id'] == row['player_club_id']
            else np.nan, axis=1)
        df["goals_against"] = df.apply(lambda row: row['away_club_goals'] if row['home_club_id'] == row['player_club_id']
            else row['home_club_goals'] if row['away_club_id'] == row['player_club_id']
            else np.nan, axis=1)
        df['clean_sheet'] = df.apply(lambda row: 1 if row['goals_against'] == 0
            else 0 if row['goals_against'] > 0
            else np.nan, axis=1)
        df = df.groupby(['player_id',"season"],as_index=False).agg({'goals': 'sum', 'game_id': 'nunique',
                                                                    'assists': 'sum', 'minutes_played' : 'sum', 'goals_for' : 'sum',
                                                                    'goals_against' : 'sum', 'clean_sheet' : 'sum','yellow_cards':'sum','red_cards':'sum'})
        out_df = df.rename(columns={'game_id': 'games'})
        return out_df


# preprocessing function to return a dataframe
def preprocessing(clubs_df,players_df,games_and_appearances_df):

    merged_players_df=players_df.drop(['current_club_id', 'city_of_birth', 'date_of_birth','first_name', 'last_name', 'player_code', 'image_url', 'url'], axis=1)
    merged_players_df = merged_players_df.reindex(columns = merged_players_df.columns.tolist() + ['club_value','squad_size','goals','goals_2022','games_2022','assists_2022','minutes_played_2022','goals_against_2022','goals_for_2022','clean_sheet_2022'])

    for player_id in merged_players_df.player_id.unique():
        club_id = players_df.current_club_id[(players_df.player_id==player_id)]
        try:
            merged_players_df.club_value[(players_df.player_id==player_id)]=int(clubs_df.total_market_value[(clubs_df.club_id==int(club_id))])
        except:
            merged_players_df.club_value[(players_df.player_id==player_id)]='NaN'
        merged_players_df.squad_size[(players_df.player_id==player_id)]=int((clubs_df.squad_size[(clubs_df.club_id==int(club_id))]))

    columns=['player_id','games_2022','minutes_played_2022','goals_2022','assists_2022','goals_against_2022','goals_for_2022','clean_sheet_2022','name','position','sub_position','last_season','foot','height_in_cm','age','country_of_citizenship','country_of_birth','current_club_name','club_value','squad_size','current_club_domestic_competition_id','agent_name','contract_expiration_date','term_days_remaining','market_value_in_eur','highest_market_value_in_eur']
    merged_players_df=merged_players_df[columns]

    #iterate through players
    for index in merged_players_df.index:
        id = merged_players_df.loc[index][0]
        name = merged_players_df.loc[index][1]

        season = 2022
        stats = player_stats(id, season, games_and_appearances_df)

        merged_players_df.at[index,'games_{}'.format(season)]= stats['games'][0]
        merged_players_df.at[index,'goals_{}'.format(season)]= stats['goals'][0]
        merged_players_df.at[index,'assists_{}'.format(season)]= stats['assists'][0]
        merged_players_df.at[index,'minutes_played_{}'.format(season)]= stats['minutes_played'][0]
        merged_players_df.at[index,'goals_for_{}'.format(season)]= stats['goals_for'][0]
        merged_players_df.at[index,'goals_against_{}'.format(season)]= stats['goals_against'][0]
        merged_players_df.at[index,'clean_sheet_{}'.format(season)]= stats['clean_sheet'][0]
        merged_players_df.at[index,'yellow_cards_{}'.format(season)]= stats['yellow_cards'][0]
        merged_players_df.at[index,'red_cards_{}'.format(season)]= stats['red_cards'][0]


    #drop nan
    merged_players_df1=merged_players_df.dropna(subset=['market_value_in_eur'])

    # convert position categories to Columns for test data
    dummies=pd.get_dummies(merged_players_df1[['position']], prefix_sep='_')
    merged_players_df1 = pd.concat([merged_players_df1, dummies], axis=1)
    dummies=pd.get_dummies(merged_players_df1[['sub_position']], prefix_sep='_')
    merged_players_df1 = pd.concat([merged_players_df1, dummies], axis=1)
    dummies=pd.get_dummies(merged_players_df1[['foot']], prefix_sep='_')
    merged_players_df1 = pd.concat([merged_players_df1, dummies], axis=1)

    #separate numeric columns
    drop_cols = ['player_id', 'clean_sheet_2022', 'name', 'position', 'sub_position', 'last_season',
       'foot', 'country_of_citizenship',
       'country_of_birth', 'current_club_name', 'club_value',
       'current_club_domestic_competition_id', 'agent_name',
       'contract_expiration_date', 'highest_market_value_in_eur']
    merged_players_df1 = merged_players_df1.drop(columns=drop_cols)
    return merged_players_df1
