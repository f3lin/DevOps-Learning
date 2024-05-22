from fastapi import FastAPI

api = FastAPI()

@api.get('/')
def get_index():
    return "Bienvenue sur mon API"