from pydantic import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str
    embedding_model_name: str = "openai"
    llm_model_name: str = "gpt-3.5-turbo"
    chunk_size: int = 1000
    overlap: int = 200

    class Config:
        env_file = ".env"

settings = Settings()
