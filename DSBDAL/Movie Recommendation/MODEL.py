def read_csv(inputs):
  import pandas as pd
  import difflib
  from sklearn.feature_extraction.text import TfidfVectorizer
  from sklearn.metrics.pairwise import cosine_similarity

  df = pd.read_csv("movies.csv")

  # Understanding Important Features
  important_features = ['genres', 'keywords', 'cast', 'director', 'tagline']

# Filling Missing/NaN values
  for feat in important_features:
      df[feat] = df[feat].fillna('')

  # Combining Important Features
  combined_features = df['genres']+' '+df['keywords']+' '+df['tagline']+' '+df['cast']+' '+df['director']

  # Converting Text Data into Vectors
  vectorizer = TfidfVectorizer()
  feature_vectors = vectorizer.fit_transform(combined_features)

  # Understanding Similar Score
  similar_score = cosine_similarity(feature_vectors)

  # Taking User Input
  user_movie = inputs

  all_movies_list = df['title'].tolist()
  find_matching = difflib.get_close_matches(user_movie, all_movies_list)

  # Finding Similar Movies
  close_match = find_matching[0]
  id_matching_movie = df[df.title == close_match]['index'].values[0]
  sim_score = list(enumerate(similar_score[id_matching_movie]))
  sorted_similar_movies = sorted(sim_score, key = lambda x:x[1], reverse = True)

  # Top Recommended Movies
  get_recon_movies = []
  i = 1
  for movie in sorted_similar_movies:
    index = movie[0]
    title_from_index = df[df.index==index]['title'].values[0]
    if(i<=30):
      get_recon_movies.append(title_from_index)
      i+=1

  return get_recon_movies[:10]
