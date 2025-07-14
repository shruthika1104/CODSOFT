import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample movie data
movies = {
    'title': [
        'The Avengers', 'Avengers: Age of Ultron', 'Iron Man', 'Iron Man 2', 'Captain America: Civil War',
        'Thor', 'Thor: Ragnarok', 'Guardians of the Galaxy', 'Doctor Strange', 'Black Panther'
    ],
    'description': [
        'Superheroes save the world from alien invasion.',
        'Avengers fight a powerful robot created by Tony Stark.',
        'Billionaire builds a high-tech iron suit to fight evil.',
        'Iron Man faces a new enemy with advanced tech.',
        'Heroes clash over the Sokovia Accords.',
        'Norse god battles to save his realm.',
        'Thor teams up with Hulk to stop Ragnarok.',
        'A group of misfits come together to save the galaxy.',
        'A neurosurgeon learns mystic arts to save the world.',
        'A prince becomes the Black Panther and defends Wakanda.'
    ]
}

# Convert to DataFrame
df = pd.DataFrame(movies)

# Vectorize the descriptions
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['description'])

# Compute cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Recommend n movies
def recommend_movie(title, num_recommendations):
    if title not in df['title'].values:
        print("❌ Movie not found.")
        return
    idx = df[df['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:num_recommendations+1]
    
    print(f"\n🎥 Because you watched '{title}', you might also like:")
    for i, score in sim_scores:
        print(f"- {df.iloc[i]['title']}")

# Main program
print("🎬 Welcome to the Movie Recommender!")
print("Available movies:")
print("\n".join(df['title']))

movie = input("\nEnter a movie name from above: ")
try:
    n = int(input("How many recommendations do you want? "))
    recommend_movie(movie, n)
except:
    print("❌ Invalid input for number of recommendations.")
