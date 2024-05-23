from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

api = FastAPI()

class User(BaseModel):
    user_id: int
    name: str
    subscription: str

users_db = [
        User(user_id=1, name='Alice', subscription='free tier'),
        User(user_id=2, name='Bob', subscription='premium tier'),
        User(user_id=3, name='Clementine', subscription='free tier')
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

@api.get('/users/{user_id}/name')
def get_index(user_id:int):
    user = next((user for user in users_db if user['user_id'] == user_id), None)
    return {'name': user['name']} if user is not None else []

@api.post('/users')
def create_user(user:User):
    if any(u.user_id == user.user_id for u in users_db):
        raise HTTPException(status_code=400, detail="User already exists")
    else:
        users_db.append(user)
        return user
    
@api.put('/users/{user_id}')
def update_user(user_id:int, user:User):
    for idx, u in enumerate(users_db):
            if u.user_id == user_id:
                users_db[idx] = user
                return user
    raise HTTPException(status_code=404, detail="User not found")


@api.delete('/users/{user_id}')
def delete_user(user_id: int):
    for idx, u in enumerate(users_db):
        if u.user_id == user_id:
            del users_db[idx]
            return {"detail": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")

@api.get('/headers')
def get_headers(user_agent=Header(None)):
    return {
        'User-Agent': user_agent
    }