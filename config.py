import os

BASE_URL = os.getenv("POKEAPI_BASE_URL", "https://pokeapi.co/api/v2")
MAX_RESPONSE_TIME_SECONDS = float(os.getenv("MAX_RESPONSE_TIME_SECONDS", "1"))