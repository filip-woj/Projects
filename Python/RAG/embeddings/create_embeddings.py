import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# # Example: list of texts (your cleaned/chunked docs)
texts = [
    {"text": "Machine learning is a subset of AI."},
    {"text": "RAG pipelines allow retrieval-augmented answers."},
    {"text": "Allows you to combine LLMs with external knowledge sources."}
]

# embeddings = []
# for text in texts:
#     response = client.embeddings.create(
#         model="text-embedding-3-small",  # cheap and fast
#         input=text
#     )
#     vector = response.data[0].embedding
#     embeddings.append(vector)

# print(f"Created {len(embeddings)} embeddings.")


# embeddings/create_embeddings.py
from openai import OpenAI

def create_embeddings(chunks, client):
    """
    Input: 
        chunks: list of dicts with 'text' key
        client: OpenAI client object
    Output:
        list of embeddings (vectors)
    """
    embeddings = []
    for chunk in chunks:
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=chunk["text"]
        )
        embeddings.append(response.data[0].embedding)
    return embeddings



embeddings = create_embeddings(texts, client)
print(embeddings)