import streamlit as st 
import pickle
import pandas as pd

def recommend(movie):
    # Check if the movie is in the list
    if movie in movies_list['title'].values:
        movie_index = movies_list[movies_list['title'] == movie].index[0]
        distances = similarity[movie_index]
        movie_list = sorted(list(enumerate(distances)),reverse=True, key=lambda x: x[1])[1:6]
        recommend_movies = []
        for i in movie_list:
            recommend_movies.append(movies_list.iloc[i[0]].title)
        return recommend_movies
    else:
        st.write("Movie not found in the database")
        return []

movies_list = pickle.load(open('movies.pkl','rb'))
movies_list = movies_list[['title']]  # Adjust if 'title' is not the only column

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Which movie would you like to watch today', movies_list['title'])

if st.button('Recommend'):
    recommendation = recommend(selected_movie_name)
    for movie in recommendation:
        st.write(movie)
