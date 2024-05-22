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

@api.get('/users/{user_id}')
def get_index(user_id:int):
    user = next((user for user in users_db if user['user_id'] == user_id), None)
    return user if user is not None else []
