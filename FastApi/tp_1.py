from fastapi import FastAPI

api = FastAPI()

users_db = [
    {
        'user_id': 1,
        'name': 'Alice',
        'subscription': 'free tier'
    },
    {
        'user_id': 2,
        'name': 'Bob',
        'subscription': 'premium tier'
    },
    {
        'user_id': 3,
        'name': 'Clementine',
        'subscription': 'free tier'
    }
]


@api.get('/')
def get_index():
    return "Bienvenue sur mon API"


@api.get('/users')
def get_index():
    return users_db