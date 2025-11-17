from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Audionex"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str = "postgresql://user:password@localhost/db"
    REDIS_URL: str = "redis://localhost:6379"

    # For Vector DB + KB Ingestion
    OPENAI_API_KEY: str = "your-openai-api-key"
    PINECONE_API_KEY: str = "your-pinecone-api-key"
    PINECONE_ENVIRONMENT: str = "gcp-starter" # Or your pinecone environment
    PINECONE_INDEX_NAME: str = "audionex-kb"
    EMBEDDING_MODEL: str = "text-embedding-ada-002"
    EMBEDDING_DIMENSION: int = 1536

    # For Telephony
    TWILIO_ACCOUNT_SID: str = "your-twilio-account-sid"
    TWILIO_AUTH_TOKEN: str = "your-twilio-auth-token"
    # This should be the publicly accessible URL of your server
    BASE_URL: str = "http://localhost:8000" 


    class Config:
        env_file = ".env"

settings = Settings()
