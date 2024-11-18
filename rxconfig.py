import reflex as rx
from dotenv import load_dotenv
import os

load_dotenv()
config = rx.Config(
    app_name="reflex_site",
    db_url=os.getenv("DB_URL"),
)
