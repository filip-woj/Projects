def chunk(text, chunk_size=500, overlap=50):
    """
    Splits text into overlapping chunks
    """
    chunks = []
    for i in range(0, len(text), chunk_size - overlap):
        chunks.append(text[i:i + chunk_size])
    return chunks