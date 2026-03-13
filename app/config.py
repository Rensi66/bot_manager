from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    DATABASE = os.getenv('DATABASE')