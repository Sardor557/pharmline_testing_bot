from dotenv import load_dotenv
import os


load_dotenv()

SERVER_URL = "http://" + os.getenv("ip") + "/"
