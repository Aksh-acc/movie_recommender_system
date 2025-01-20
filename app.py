import streamlit as st
import pickle
def recommend(movie):
    movie_index =movies_list_load[movies_list_load['title'] == movie].index[0]
    distances =similarity[movie_index]
    movies_list =sorted(list(enumerate(distances)) ,reverse =True ,key =lambda x:x[1])[1:6]
    recommended_movies =[]
    for i in movies_list:
        recommended_movies.append(movies_list_load.iloc[i[0]].title)
    return recommended_movies
similarity =pickle.load(open('similarity.pkl' ,'rb'))
movies_list_load =pickle.load(open('movies.pkl' ,'rb'))
movies_list_loaded =movies_list_load['title'].values
st.title('Selected movie name')
selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    (movies_list_loaded),
)
if st.button("Recommend"):
    recommendations =recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
