import pickle
import streamlit as st
import pandas as pd

movies = pickle.load(open('movie.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []

    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names


st.header('Movie Recommendation System')

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)

    for i in recommended_movie_names:
        st.text(i)