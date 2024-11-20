import reflex as rx
from dotenv import load_dotenv
import os

load_dotenv()
config = rx.Config(
    app_name="reflex_site",
    api_url=os.getenv("API_URL"),
    db_url=os.getenv("DB_URL"),
)
