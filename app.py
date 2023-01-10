import streamlit as st
import pandas as pd
from PIL import Image

import helper

df=pd.read_csv('netflix_titles.csv')


st.sidebar.title("Netflix Analysis")
image = Image.open('netflix_.webp')
st.sidebar.image('netflix_.webp')

user_menu=st.sidebar.radio(
    'select an option',
    ('Overall Analysis','category_wise','year_wise','Director_wise','Type_wise')
)

if user_menu=='Overall Analysis':
    st.header("Overall Analysis")

    cleaning=helper.cleaning(df)
    year,category=helper.category_year_list(df)
    cleaning=helper.new_clean(df)

    selected_year=st.sidebar.selectbox("select Year" , year)
    selected_category=st.sidebar.selectbox("select categories",category)

    cleaning=helper.movie_fetch(df,selected_year,selected_category)


    st.dataframe(cleaning)

if user_menu=='category_wise':
    st.title("category_wise_movies")
    category=helper.category(df)
    selected_category=st.sidebar.selectbox("select category",category)
    cleaning = helper.cleaning(df)
    cleaning=helper.new_clean(df)

    cleaning=helper.category_wise(df,selected_category)


    st.dataframe(cleaning)

if user_menu=='year_wise':
    st.title('year_wise_movies')
    year=helper.year_list(df)
    selected_year=st.sidebar.selectbox("select year",year)

    year_wise=helper.cleaning(df)
    year_wise=helper.new_clean(df)

    year_wise=helper.year_wise(df,selected_year)

    st.dataframe(year_wise)

if user_menu=='Director_wise':
    st.title('Director_wise_movie')

    Director=helper.cleaning(df)
    Director=helper.new_clean(df)
    Director = helper.director_fetch(df)

    selected_director=st.sidebar.selectbox("select director",Director)
    Director=helper.director_wise(df,selected_director)
    st.dataframe(Director)

if user_menu=='Type_wise':
    st.title('Type_wise_movie')
    Type=helper.cleaning(df)
    Type=helper.new_clean(df)
    Type=helper.Type_wise(df)
    selected_Type=st.sidebar.selectbox('select Type',Type)
    Type=helper.Type_fetch(df,selected_Type)
    st.dataframe(Type)


    













