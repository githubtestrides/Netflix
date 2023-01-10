import pandas as pd
import numpy as np


def cleaning(df):
    cleaning=df.drop(columns=['date_added', 'show_id', 'rating', 'duration'], inplace=True)


    return cleaning

def category_year_list(df):
    category = np.unique(df['listed_in'].values).tolist()
    category.sort()
    category.insert(0, 'Overall')

    year = df['release_year'].unique().tolist()
    year.sort()
    year.insert(0, 'Overall')

    return year,category


def movie_fetch(df,year, category):



    if year == 'Overall' and category == 'Overall':
        temp_df = df
    if year != 'Overall' and category == 'Overall':
        temp_df = df[df['release_year'] == int(year)]
    if year == 'Overall' and category != 'Overall':
        temp_df = df[df['listed_in'] == category]
    if year != 'Overall' and category != 'Overall':
        temp_df = df[(df['release_year'] == int(year)) & (df['listed_in'] == category)]

    return temp_df

def category(df):
    category = np.unique(df['listed_in'].values).tolist()
    category.sort()
    category.insert(0, 'Overall')

    return category

def category_wise(df,category):
    if category == 'Overall':
        temp_df = df
    if category != 'Overall':
        temp_df = df[df['listed_in'] == category]
    return(temp_df)

def new_clean(df):
    new_clean=df.dropna(inplace=True)
    return new_clean

def year_wise(df,year):
    if year=='Overall':
        temp_df=df
    if year!='Overall':
        temp_df=df[df['release_year']==int(year)]
    return temp_df
def year_list(df):
    year = df['release_year'].unique().tolist()
    year.sort()
    year.insert(0, 'Overall')

    return year

def director_wise(df,director):
    if director=='Overall':
        temp_df=df
    if director!='Overall':
        temp_df=df[df['director']==director]
    return temp_df

def director_fetch(df):
    Director = df['director'].unique().tolist()
    Director.sort()
    return Director

def Type_wise(df):
    Type = df['type'].unique().tolist()
    Type.sort()
    Type.insert(0,'Overall')
    return Type

def Type_fetch(df,Type):
    if Type=='Overall':
        temp_df=df
    if Type!='Overall':
        temp_df=df[df['type']==Type]
    return temp_df






