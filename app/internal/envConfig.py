from dotenv import load_dotenv
import os


load_dotenv()

MYSQL_URI = os.getenv("MYSQL_URI")
