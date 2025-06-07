#!/usr/bin/python3

import sys
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from itertools import combinations

documents = []

# Read input data
for line in sys.stdin:
    doc_id, text = line.strip().split("\t", 1)
    documents.append(text)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

doc_vectors = {}

for idx, row in enumerate(tfidf_matrix):
    vec = row.toarray()[0]
    doc_vectors[idx] = vec


# Cosine similarity function
def cosine_sim(v1, v2):
    num = np.dot(v1, v2)
    denom = np.linalg.norm(v1) * np.linalg.norm(v2)
    return num / denom if denom else 0

# Calculate pairwise cosine similarity
for (id1, vec1), (id2, vec2) in combinations(doc_vectors.items(), 2):
    sim = cosine_sim(vec1, vec2)
    print(f"{id1:<12} {id2:<12} {sim:<18.4f}")

