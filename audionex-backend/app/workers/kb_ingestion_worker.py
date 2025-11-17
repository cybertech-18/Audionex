import tiktoken
import requests
from bs4 import BeautifulSoup
from pypdf import PdfReader
import io
from typing import List
from uuid import uuid4

from app.services import embedding_client, vector_db

# --- Text Chunking Logic ---

def num_tokens_from_string(string: str, encoding_name: str = "cl100k_base") -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

def chunk_text(text: str, max_tokens: int = 512, overlap: int = 50) -> List[str]:
    """Chunks text into smaller pieces with overlap."""
    tokens = text.split()
    chunks = []
    current_chunk = []
    current_tokens = 0

    for token in tokens:
        token_len = num_tokens_from_string(token)
        if current_tokens + token_len > max_tokens:
            chunks.append(" ".join(current_chunk))
            current_chunk = current_chunk[-overlap:]
            current_tokens = sum(num_tokens_from_string(t) for t in current_chunk)
        
        current_chunk.append(token)
        current_tokens += token_len

    if current_chunk:
        chunks.append(" ".join(current_chunk))
    
    return chunks

# --- Content Extraction Logic ---

def extract_text_from_url(url: str) -> str:
    """Extracts text content from a URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.extract()
        return soup.get_text(separator='\n', strip=True)
    except requests.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return ""

def extract_text_from_pdf(file_stream: io.BytesIO) -> str:
    """Extracts text from a PDF file stream."""
    reader = PdfReader(file_stream)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

# --- Main Ingestion Logic ---

def process_and_embed(text: str, metadata: dict, index):
    """Chunks text, creates embeddings, and upserts to vector DB."""
    chunks = chunk_text(text)
    vectors_to_upsert = []

    for i, chunk in enumerate(chunks):
        embedding = embedding_client.get_embedding(chunk)
        vector_id = f"{metadata.get('source', 'unknown')}-{uuid4()}"
        
        vector_metadata = metadata.copy()
        vector_metadata['chunk'] = i
        vector_metadata['text'] = chunk

        vectors_to_upsert.append({
            "id": vector_id,
            "values": embedding,
            "metadata": vector_metadata
        })

        # Upsert in batches
        if len(vectors_to_upsert) >= 100:
            vector_db.upsert_vectors(vectors_to_upsert, index)
            vectors_to_upsert = []
    
    # Upsert any remaining vectors
    if vectors_to_upsert:
        vector_db.upsert_vectors(vectors_to_upsert, index)

def ingest_from_url(url: str, tenant_id: str):
    """High-level function to ingest knowledge from a URL."""
    print(f"Ingesting from URL for tenant {tenant_id}: {url}")
    text = extract_text_from_url(url)
    if not text:
        return
    
    index = vector_db.get_index()
    metadata = {"source": url, "tenant_id": tenant_id}
    process_and_embed(text, metadata, index)
    print(f"Finished ingesting from URL: {url}")

def ingest_from_pdf(file_stream: io.BytesIO, filename: str, tenant_id: str):
    """High-level function to ingest knowledge from a PDF."""
    print(f"Ingesting from PDF for tenant {tenant_id}: {filename}")
    text = extract_text_from_pdf(file_stream)
    if not text:
        return

    index = vector_db.get_index()
    metadata = {"source": filename, "tenant_id": tenant_id}
    process_and_embed(text, metadata, index)
    print(f"Finished ingesting from PDF: {filename}")
