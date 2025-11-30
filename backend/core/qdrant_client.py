import os
from qdrant_client import QdrantClient

_client: QdrantClient | None = None

def get_qdrant_client() -> QdrantClient:
    global _client
    if _client is None:
        qdrant_url = os.environ.get("QDRANT_URL_ENDPOINT")
        qdrant_api_key = os.environ.get("QDRANT_API_KEY")

        if not qdrant_url:
            raise ValueError("QDRANT_URL_ENDPOINT is missing from .env")
        if not qdrant_api_key:
            raise ValueError("QDRANT_API_KEY is missing from .env")

        _client = QdrantClient(url=qdrant_url, api_key=qdrant_api_key)
    return _client
