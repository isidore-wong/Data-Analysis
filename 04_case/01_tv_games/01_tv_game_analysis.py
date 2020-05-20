# _*_ coding:utf-8 _*_
import pandas as pd
import numpy as np
from IPython import display
from collections import namedtuple  #

"""
@author: Hayes Wong
@email: 616132717@qq.com
@file: 01_tv_game_analysis
@time: 2020/05/19 0:18
"""

"""
Description: This is a program which analyzes data of tv game.
"""

# Define CalFunc which is namedtuple type , containing col, func and name attributes
CalFunc = namedtuple('CalFunc', 'col func name')


# get file path according to file name
def get_path(name):
    return f'../00_dataset/data_tv_game/{name}.csv'


# get data
def get_data():
    # sales
    sales_cols = ['GameID', 'Total Sales', 'User Score']
    sales_data = pd.read_csv(get_path('sales'), usecols=sales_cols)

    # games
    games_cols = ['Console Short Name', 'GameID', 'Release', 'Game', 'Ratings']
    games_data = pd.read_csv(get_path('games'), usecols=games_cols)

    # genres
    genres_cols = ['GameID', 'Genre']
    genres_data = pd.read_csv(get_path('genres'), usecols=genres_cols)

    # consoles
    consoles_cols = ['Console Short Name', 'Console Long Name', 'Manufacturer', 'Generation']
    consoles_data = pd.read_csv(get_path('consoles'), usecols=consoles_cols)

    # ratings
    ratings_cols = ['Rating Code', 'Ratings', 'Description cn', 'Sort Order']
    ratings_data = pd.read_csv(get_path('ratings'), usecols=ratings_cols)

    # connect all tables
    df_data = (
        sales_data.merge(games_data, how='left', on='GameID')
                  .merge(consoles_data, how='left', on='Console Short Name')
                  .merge(genres_data, how='left', on='GameID')
                  .merge(ratings_data, how='left', on='Ratings')
    )

    df_data['Time'] = df_data['Release'].apply(
        lambda x: pd.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
    )
    df_data['Year'] = df_data['Time'].dt.year
    cols = [c.replace(' ', '_') for c in df_data.columns]
    df_data.columns = cols
    return df_data

# output the integrated data
result_data = get_data()
result_data.to_excel('data integration.xlsx', index=False)

# sales of games
def cal_total_revenue():
    return CalFunc(col='Total_Sales', func='sum', name='total_revenue')


# number of games
def cal_total_games():
    return CalFunc(col='GameID', func='count', name='total_games')


# average user score
def cal_avg_user_score():
    return CalFunc(col='User_Score', func='mean', name='avg_user_score')


# convert each incoming statistical method into a dictionary
def cal(data, labels, *cal_funcs):
    funcs = (f() for f in cal_funcs)
    agg_dicts = {
        v.col: {v.name: v.func}
        for v in funcs
    }

    # summary
    res = (
        data.groupby(labels).agg(agg_dicts)
    )

    # remove the first-level column name
    res.columns = res.columns.droplevel(0)
    return res.reset_index()


def display_df_with_format(data, value_cols=None):
    res = data.style.bar(
        subset=value_cols,
        color='#00557f')

    display(res)

# get data
df = get_data()
df.info()

# overall market
res_market = cal(df, ['Year'], cal_total_games, cal_total_revenue)
display_df_with_format(res_market.query('Year >= 2000'), ['total_games', 'total_revenve'])

# brand
res_brand = cal(df, ['Manufacturer'], cal_total_games, cal_total_revenue)
display_df_with_format(res_brand, ['total_games', 'total_revenve'])

# Genres
res_genres = cal(df, ['Genres'], cal_avg_user_score, cal_total_revenue, cal_total_games)
res_genres.sort_values('avg_user_score', inplace=True, ascending=False)
display_df_with_format(res_genres)

# games
res_games = cal(df, ['Genre', 'Year'], cal_avg_user_score)
display_df_with_format(res_games, value_cols=['avg_user_score'])



