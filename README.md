# Movie Recommender System
## web url : https://movie-recommender-ap.streamlit.app/
## Overview
Welcome to the Movie Recommender System! This application uses machine learning to suggest a list of 5 personalized movie recommendations based on a movie provided by the user. The system leverages collaborative filtering and content-based filtering techniques to analyze movie features and user preferences, providing accurate recommendations.

The app is developed using Python, Streamlit, and machine learning models, and is hosted on Streamlit for an easy-to-use, interactive interface.

## Key Features
1. 5 Personalized Recommendations: Get a list of 5 movie recommendations based on a movie you like.
2. Collaborative and Content-Based Filtering: The system combines multiple approaches to recommend the most relevant movies.
3.Interactive Interface: Hosted on Streamlit for an easy-to-use, dynamic interface.
4.Movie Details: Provides essential information like title, release year, and genre for each recommendation.
## Technologies Used
Python: Core programming language used for building the recommendation system.
Streamlit: For creating an interactive web app interface.
Pandas: For data manipulation and preprocessing.
Scikit-learn: For implementing machine learning models.
Surprise: For collaborative filtering algorithms.
TMDb API: For fetching movie metadata like titles, descriptions, and genres.
# How It Works

User Input:
You start by providing the name of a movie you like or have watched.
Movie Analysis:
The system processes the movie's features (e.g., genre, director, actors) and uses collaborative filtering techniques to find movies that are similar based on ratings and other user behavior.
Recommendations:
The model generates a list of 5 movie recommendations based on the input movie and presents them to you.
Movie Information:
For each recommended movie, the app displays important details such as:
Title
Release Year
Genre(s)
Brief Description

## How to Use
1. Access the App
To use the Movie Recommender System, visit the hosted Streamlit app at [Your Streamlit URL].
2. Enter Movie Name
Type the name of any movie you like or have recently watched into the input box.
3. Get Recommendations
Click the button to get 5 movie recommendations based on your input. The system will fetch relevant movie suggestions and display their details.
4. Explore Recommendations
Review the 5 movie suggestions and discover new movies you might enjoy!
Installation (Local Setup)

To run the Movie Recommender System locally, follow the instructions below:

Prerequisites

Python 3.x

pip (Python package installer)

Steps Clone the Repository:

bash Copy git clone https://github.com/Aksh-acc/movie-recommender-system.git

cd movie-recommender-system

Install Dependencies: Install all required libraries by running:

bash Copy pip install -r requirements.txt

Run the App: Start the Streamlit app with the following command:

bash Copy streamlit run app.py

Access the App Locally: Open your browser and navigate to http://localhost:8501 to interact with the app.

## Example Use Case
 You provide the name of a movie, such as "Inception."
 
 The system analyzes the movie’s features and user preferences to find similar films.
 
 It then displays 5 movie recommendations like "The Prestige," "Interstellar," "Shutter Island," and others.

## Future Enhancements
~Improved Recommendation Algorithms: Exploring the use of deep learning models for more accurate and diverse recommendations.

~User Feedback: Allowing users to rate recommended movies, further improving the system.  

~Additional Filtering: Implementing additional filters for genres, release year, etc., to refine the recommendations.

## Acknowledgements
TMDb API: For providing the movie data and metadata.

Streamlit: For making it easy to build and host interactive web apps.

Scikit-learn and Surprise: For machine learning algorithms that power the recommendation system.
