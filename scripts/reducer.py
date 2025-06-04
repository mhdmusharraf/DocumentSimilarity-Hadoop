#!/usr/bin/python3

import sys
import numpy as np
from itertools import combinations

doc_vectors = {}

for line in sys.stdin:
    doc_id, vec_str = line.strip().split("\t", 1)
    vec = np.array([float(x) for x in vec_str.split(",")])
    doc_vectors[int(doc_id)] = vec

def cosine_sim(v1, v2):
    num = np.dot(v1, v2)
    denom = np.linalg.norm(v1) * np.linalg.norm(v2)
    return num / denom if denom else 0

for (id1, vec1), (id2, vec2) in combinations(doc_vectors.items(), 2):
    sim = cosine_sim(vec1, vec2)
    print(f"{id1},{id2}\t{sim:.4f}")
