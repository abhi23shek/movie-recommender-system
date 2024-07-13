import streamlit as st
import pandas as pd
import pickle
import requests
import numpy as np

def fetch_poster(movie_id):

    url = "https://api.themoviedb.org/3/movie/{}?language=en-US".format(movie_id)

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlYzU2YWM1MzVhNDhmNTQ2ZTAzZDQyNWMxNWRkMTc5MCIsIm5iZiI6MTcyMDc3ODA4Ny43MTc5ODEsInN1YiI6IjY2ODRkZmM5ZGM3YTlhY2NjOTFhM2Y3YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.3qJoiB5AxjjQcCSYvGA2BNJcRMAAtPXWtBzCPCLbwRI"
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

movies_list = pickle.load(open('moviesdict.pkl', 'rb'))
movies = pd.DataFrame(movies_list)
similarity1 = pickle.load(open('similarity1.pkl', 'rb'))
similarity2 = pickle.load(open('similarity2.pkl', 'rb'))
similarity = np.vstack((similarity1, similarity2))


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select the movie on which you want recommendation',
    movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")

    col4, col5, col6 = st.columns(3, gap="medium")

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

    with col6:
        st.text(names[5])
        st.image(posters[5])