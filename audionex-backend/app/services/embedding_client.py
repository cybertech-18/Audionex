import openai
from app.core.config import settings

openai.api_key = settings.OPENAI_API_KEY

def get_embedding(text: str, model: str = settings.EMBEDDING_MODEL):
    text = text.replace("\n", " ")
    response = openai.Embedding.create(input=[text], model=model)
    return response['data'][0]['embedding']
