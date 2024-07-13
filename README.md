# Movie Recommender System

## Overview

This repository contains a Streamlit-based web application for recommending movies based on a selected movie. The application uses a pre-trained similarity model and displays recommended movies along with their posters.

## Features

- Select a movie from a list to get recommendations.
- Displays the recommended movies with their posters.
- Utilizes The Movie Database (TMDb) API to fetch movie posters.

## Requirements

- Python 3.6 or higher
- Streamlit
- Pandas
- Requests
- Pickle
- Numpy

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/abhi23shek/movie-recommender-system.git
    cd movie-recommender-system
    ```

2. Install the required packages:
    ```bash
    pip install streamlit pandas requests numpy
    ```

3. Ensure you have the required pickle files (`moviesdict.pkl`, `similarity1.pkl`, `similarity2.pkl`) in the repository directory.

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open the provided URL in your web browser to access the application.

3. Select a movie from the dropdown menu and click the "Recommend" button to get recommendations.

## File Descriptions

- `app.py`: Main script for running the Streamlit app.
- `moviesdict.pkl`: Pickle file containing movie data.
- `similarity1.pkl` and `similarity2.pkl`: Pickle files containing pre-trained similarity matrices.

## API Key

The application uses The Movie Database (TMDb) API to fetch movie posters. The API key is included in the script. Make sure to replace it with your own API key if necessary.

## How It Works

1. The user selects a movie from the dropdown menu.
2. Upon clicking the "Recommend" button, the app fetches similar movies using the pre-trained similarity model.
3. The app then retrieves the posters of the recommended movies using the TMDb API.
4. The recommended movies and their posters are displayed on the web interface.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [The Movie Database (TMDb) API](https://www.themoviedb.org/documentation/api)
- [Numpy](https://numpy.org/)

