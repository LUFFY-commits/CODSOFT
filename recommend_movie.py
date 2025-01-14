import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = {
    'Title': ['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E'],
    'Genre': ['Action', 'Adventure', 'Action', 'Drama', 'Action'],
    'Director': ['Director 1', 'Director 2', 'Director 1', 'Director 3', 'Director 1'],
    'Cast': ['Actor 1, Actor 2', 'Actor 3, Actor 4', 'Actor 1, Actor 3', 'Actor 2, Actor 5', 'Actor 1, Actor 5']
}

df = pd.DataFrame(data)

df['Features'] = df['Genre'] + " " + df['Director'] + " " + df['Cast']

tfidf = TfidfVectorizer(stop_words='english')

tfidf_matrix = tfidf.fit_transform(df['Features'])

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def recommend_movie(movie_title, cosine_sim=cosine_sim):
    idx = df.index[df['Title'] == movie_title].tolist()[0]

    sim_scores = list(enumerate(cosine_sim[idx]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:4]

    movie_indices = [i[0] for i in sim_scores]

    return df['Title'].iloc[movie_indices]

# Example: Get recommendations for 'Movie A'
recommended_movies = recommend_movie('Movie A')
print("Recommended Movies based on 'Movie A':")
print(recommended_movies)
