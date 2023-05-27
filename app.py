import base64
import pickle
import streamlit as st
import requests
from PIL import Image


# Fetching Poster From tmdb website
def fetch_poster(Movie_id_x):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=0801e204f4527cf4a78827c23aac0698&language=en-US".format(
        Movie_id_x)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


# Recommendation System
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        Movie_id_x = movies.iloc[i[0]].Movie_id_x
        recommended_movie_posters.append(fetch_poster(Movie_id_x))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters

# Page Icon, Title and Layout
im = Image.open('img/movie_icon.png')
st.set_page_config(page_title="Movie Recommender", page_icon=im, layout="wide")
st.header('Movie Recommendation System')
st.subheader('-By Rahul Sharma(Team Leader)')
st.markdown('Team Members : Abhijeet Singh and Nipun Tiwari')

# Drop Down Movie Selector
movies = pickle.load(open('movie_list1.pkl', 'rb'))
similarity = pickle.load(open('similarity1.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
