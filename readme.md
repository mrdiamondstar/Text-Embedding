1️ Import libraries for environment access, numerical computation, vector search, and embeddings.

2️ Initialize the OpenAI client using the API key from environment variables.

3️ Define a list of sentences that will act as the searchable knowledge base.

4️ Create an empty list to store embedding vectors.

5️ Convert each sentence into a semantic embedding using the OpenAI model.

6️ Convert the list of embeddings into a float32 NumPy matrix for FAISS.

7️ Extract the embedding vector dimension required to build the index.

8️ Create a FAISS vector index using L2 distance for similarity comparison.

9️ Add all sentence embeddings to the FAISS index.

 Define a new query sentence to search for similar meaning.

1️1️ Generate an embedding for the query using the same embedding model.

1️2️ Convert the query embedding into a FAISS-compatible NumPy vector.

1️3️ Specify how many nearest matches should be returned.

1️4️ Perform a similarity search in FAISS to find closest embeddings.

1️5️ Print the query and a separator for readable output.

1️6️ Display matched sentences with their distance scores indicating similarity.