# retrieval/faiss_index.py

import faiss
import numpy as np
import pickle
import os

def build_faiss_index(embeddings, chunks, index_path="storage/faiss.index", mapping_path="storage/index_mapping.pkl"):
    """
    Build a FAISS index from embeddings and save it with a mapping to original chunks.

    Args:
        embeddings (list of list[float]): List of embedding vectors
        chunks (list of dict): Original chunks, each with 'text' key
        index_path (str): Path to save FAISS index
        mapping_path (str): Path to save index → chunk mapping
    Returns:
        index (faiss.Index): FAISS index object
        index_mapping (dict): {index_position: chunk_text}
    """

    # Convert embeddings to float32 numpy array
    embedding_matrix = np.array(embeddings).astype("float32")
    dim = embedding_matrix.shape[1]

    # Create FAISS index (L2 distance)
    index = faiss.IndexFlatL2(dim)
    index.add(embedding_matrix)  # add vectors

    # Create mapping: index → chunk text
    index_mapping = {i: chunk['text'] for i, chunk in enumerate(chunks)}

    # Ensure storage directory exists
    os.makedirs(os.path.dirname(index_path), exist_ok=True)

    # Save index to disk
    faiss.write_index(index, index_path)

    # Save mapping
    with open(mapping_path, "wb") as f:
        pickle.dump(index_mapping, f)

    print(f"FAISS index with {len(embeddings)} vectors saved to {index_path}")
    print(f"Mapping saved to {mapping_path}")

    return index, index_mapping


def load_faiss_index(index_path="storage/faiss.index", mapping_path="storage/index_mapping.pkl"):
    """
    Load a FAISS index and its mapping from disk.

    Returns:
        index (faiss.Index): Loaded FAISS index
        index_mapping (dict): {index_position: chunk_text}
    """
    index = faiss.read_index(index_path)
    with open(mapping_path, "rb") as f:
        index_mapping = pickle.load(f)
    return index, index_mapping


def query_faiss(index, index_mapping, query_vector, k=5):
    """
    Search FAISS for top-k nearest chunks.

    Args:
        index (faiss.Index): FAISS index
        index_mapping (dict): {index_position: chunk_text}
        query_vector (list[float] or np.array): Query embedding
        k (int): Number of nearest neighbors to retrieve

    Returns:
        list of str: Top-k chunk texts
    """
    query_vector = np.array(query_vector).astype("float32").reshape(1, -1)
    distances, indices = index.search(query_vector, k)
    results = [index_mapping[i] for i in indices[0]]
    return results


# if __name__ == "__main__":
#     # Quick test
#     import os
#     from openai import OpenAI
#     from embeddings.create_embeddings import create_embeddings

#     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

#     chunks = [
#         {"text": "Machine learning is a subset of AI."},
#         {"text": "RAG pipelines allow retrieval-augmented answers."},
#         {"text": "Allows you to combine LLMs with external knowledge sources."}
#     ]

#     # Create embeddings
#     embeddings = create_embeddings(chunks, client)
#     print(f"Created {len(embeddings)} embeddings.")

#     # Build FAISS index
#     index, index_mapping = build_faiss_index(embeddings, chunks)

#     # Query example
#     query_text = "How do RAG pipelines work?"
#     query_embedding = client.embeddings.create(
#         model="text-embedding-3-small",
#         input=query_text
#     ).data[0].embedding

#     results = query_faiss(index, index_mapping, query_embedding, k=2)
#     print("\nTop matching chunks:")
#     for r in results:
#         print("-", r)