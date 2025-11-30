import os
import re
from pathlib import Path
from qdrant_client.http.models import Batch

from backend.core.qdrant_client import get_qdrant_client

COLLECTION_NAME = "AIDD-BOOK"

def chunk_markdown_by_headers(text: str) -> list[str]:
    chunks = []
    # Split by headers, keeping the header in the chunk
    splits = re.split(r'(^#+\s.*)', text, flags=re.MULTILINE)

    # The first element might be empty if the document starts with a header
    # or it might be content before the first header.
    if splits[0].strip():
        chunks.append(splits[0].strip())

    # Iterate through the rest of the splits, pairing headers with their content
    for i in range(1, len(splits), 2):
        header = splits[i].strip()
        content = splits[i+1].strip() if (i + 1) < len(splits) else ""

        if header or content:
            chunks.append(f"{header}\n{content}".strip())

    return [chunk for chunk in chunks if chunk]

def ingest_documents():
    client = get_qdrant_client()

    documents = []
    metadata = []

    docs_path = Path("docs-frontend/docs")
    for file_path in docs_path.rglob("*.md"): # Recursively find .md files
        print(f"Processing file: {file_path}")
        content = file_path.read_text(encoding="utf-8")
        chunks = chunk_markdown_by_headers(content)

        for i, chunk in enumerate(chunks):
            documents.append(chunk)
            metadata.append({"source": str(file_path), "chunk_number": i})

    if documents:
        # Qdrant client.add() with documents generates embeddings automatically using FastEmbed
        client.add(collection_name=COLLECTION_NAME, documents=documents, metadata=metadata)
        print(f"Ingestion Complete. Added {len(documents)} chunks to '{COLLECTION_NAME}' collection.")
    else:
        print("No documents found for ingestion.")

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    ingest_documents()
