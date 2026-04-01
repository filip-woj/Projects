from pathlib import Path

def load_documents(folder="Python/RAG/data/raw"):
    docs = []
    for file in Path(folder).glob("*.txt"):
        with open(file, "r", encoding="utf-8") as f:
            docs.append({
                "text": f.read(),
                "source": file.name
            })
    return docs

# Quick test
if __name__ == "__main__":
    docs = load_documents()
    print(f"Loaded {len(docs)} documents")
    if docs:
        print(docs[0]["text"][:200])  # print first 200 characters