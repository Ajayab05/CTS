import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()

password = quote_plus(os.getenv("DB_PASSWORD", ""))

url = (
    f"postgresql://{os.getenv('DB_USER')}:"
    f"{password}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)

print(
    f"Connecting to PostgreSQL at "
    f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}"
)

class Config:
    SQLALCHEMY_DATABASE_URI = url
    SQLALCHEMY_TRACK_MODIFICATIONS = False