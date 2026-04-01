import os
from openai import OpenAI

# Initialize client with API key from environment
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def embed_text(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding