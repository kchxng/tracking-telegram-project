from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    HOST:str #='10.1.23.16'
    TELEGRAM_URL:str
    TELEGRAM_BOT_TOKEN:str #= '7212583015:AAHBIauA3hkiDKg9u9YK4JPEQvDBY-BJcDM'
    TELEGRAM_CHAT_ID:str#='5519725111'
    class Config:
        env_file=".env"
        env_file_encoding='utf-8'
settings=Settings()