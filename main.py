import os
import numpy as np
import faiss
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

sentences = [
    "The cat chases the mouse.",
    "A kitten is playing.",
    "The stock market crashed."
]

embeddings = []
for s in sentences:
    resp = client.embeddings.create(
        input=s,
        model="text-embedding-3-small"
    )
    embeddings.append(resp.data[0].embedding)

embedding_matrix = np.array(embeddings).astype("float32")

dimension = embedding_matrix.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embedding_matrix)

query = "A small cat is running"

query_embedding = client.embeddings.create(
    input=query,
    model="text-embedding-3-small"
).data[0].embedding

query_vector = np.array([query_embedding]).astype("float32")

k = 2
distances, indices = index.search(query_vector, k)

print(f"Query: {query}")
print("-" * 40)

for idx, dist in zip(indices[0], distances[0]):
    print(f"Matched: {sentences[idx]}")
    print(f"Distance: {dist:.4f}")
    print()
