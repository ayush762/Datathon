import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("datascience datathon.csv")

import nltk
from nltk.corpus import wordnet
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

import re 
data = df.iloc[:,2]
data.replace("[^a-zA-Z]", " ", regex = True, inplace = True)

corpus = []
for i in range(0, 90):
    data.iloc[i] = str(data.iloc[i]).lower()
    data.iloc[i] = data.iloc[i].split()
    ps = PorterStemmer()
    data.iloc[i] = [ps.stem(word) for word in data.iloc[i] if word not in set(stopwords.words('english'))]
    data.iloc[i] = ' '.join(data.iloc[i])
    corpus.append(data.iloc[i])
    

from sklearn.metrics.pairwise import cosine_similarity    
cv = CountVectorizer(max_features= 824)
X = cv.fit_transform(corpus)
sparse_matrix = X.toarray()

cosine_sim_bow = cosine_similarity(X)

print("Cosine similarity on bag-of-words model:")
print(cosine_sim_bow)

cosine_sim_sparse = cosine_similarity(sparse_matrix)

print("Cosine similarity on sparse matrix:")
print(cosine_sim_sparse)