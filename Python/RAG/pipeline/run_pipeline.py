from openai import OpenAI
import os

from retrieval.faiss_index import load_faiss_index, query_faiss

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def answer_query(query, k=3):
    # 1. Load FAISS
    index, mapping = load_faiss_index()

    # 2. Embed query
    query_embedding = client.embeddings.create(
        model="text-embedding-3-small",
        input=query
    ).data[0].embedding

    # 3. Retrieve top-k chunks
    chunks = query_faiss(index, mapping, query_embedding, k=k)

    # 4. Build context
    context = "\n\n".join(chunks)

    # 5. Ask LLM
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Answer using the provided context only."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"}
        ]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    query = "What is machine learning?"
    answer = answer_query(query)
    print("\nAnswer:\n", answer)