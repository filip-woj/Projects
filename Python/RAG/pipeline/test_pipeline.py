import sys
from pathlib import Path

# Add project root to sys.path
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from ingestion.load_documents import load_documents
from processing.clean_text import clean
from processing.chunking import chunk

docs = load_documents()
for doc in docs:
    cleaned = clean(doc["text"])
    chunks = chunk(cleaned)
    print(f"\n{doc['source']} → {len(chunks)} chunks")