import streamlit as st 
import pickle
import pandas as pd
import requests
import requests

def fetch_poster(movie_title):
    # Make an API request to fetch movie details
    url = f"https://api.themoviedb.org/3/search/movie?api_key=c6ed519f6881232a697a85bb958ec3fc&query={movie_title}"
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        # Check if any movie results were returned
        if data['results']:
            # Extract the poster path of the first movie
            poster_path = data['results'][0]['poster_path']
            
            # Construct the full URL of the poster image
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "Poster not found"
    else:
        return "Error fetching poster"

# Rest of the code remains unchanged

    
def recommend(movie):
    # Check if the movie is in the list
    if movie in movies_list['title'].values:
        movie_index = movies_list[movies_list['title'] == movie].index[0]
        distances = similarity[movie_index]
        movie_list = sorted(list(enumerate(distances)),reverse=True, key=lambda x: x[1])[1:6]
        recommend_movies = []
        recommended_movies_poster = []
        for i in movie_list:
            recommend_movies.append(movies_list.iloc[i[0]].title)
            recommended_movies_poster.append(fetch_poster(movies_list.iloc[i[0]].title))
        return recommend_movies, recommended_movies_poster
    else:
        st.write("Movie not found in the database")
        return [], []


movies_list = pickle.load(open('movies.pkl','rb'))
movies_list = movies_list[['title']]  # Adjust if 'title' is not the only column

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Which movie would you like to watch today', movies_list['title'])

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.write(names[0])
        st.image(posters[0])
    with col2:
        st.write(names[1])
        st.image(posters[1])
    with col3:
        st.write(names[2])
        st.image(posters[2])
    with col4:
        st.write(names[3])
        st.image(posters[3])
    with col5:
        st.write(names[4])
        st.image(posters[4])
               