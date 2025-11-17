import pinecone
from app.core.config import settings

pinecone.init(api_key=settings.PINECONE_API_KEY, environment=settings.PINECONE_ENVIRONMENT)

def get_index():
    if settings.PINECONE_INDEX_NAME not in pinecone.list_indexes():
        pinecone.create_index(
            name=settings.PINECONE_INDEX_NAME,
            dimension=settings.EMBEDDING_DIMENSION,
            metric="cosine"
        )
    return pinecone.Index(settings.PINECONE_INDEX_NAME)

def upsert_vectors(vectors, index):
    index.upsert(vectors=vectors)

def query_vectors(query_embedding, top_k, index):
    return index.query(vector=query_embedding, top_k=top_k, include_metadata=True)
