from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

api = FastAPI(openapi_tags=[
    {
        'name': 'home',
        'description': 'default functions'
    },
    {
        'name': 'Users',
        'description': 'functions that are used to deal with Users'
    }
])

class User(BaseModel):
    user_id: int
    name: str
    subscription: str

users_db = [
        User(user_id=1, name='Alice', subscription='free tier'),
        User(user_id=2, name='Bob', subscription='premium tier'),
        User(user_id=3, name='Clementine', subscription='free tier')
    ]

responses = {
    200: {"description": "OK"},
    400: {"description": "User already exists"},
    404: {"description": "User not found"},
    403: {"description": "Not enough privileges"},
}


@api.get('/', summary="Welcome Message", description="Returns a welcome message.", tags=['home'])
def get_index():
    return "Bienvenue sur mon API"


@api.get('/users', responses=responses, summary="Get All Users", description="Returns a list of all users.", tags=['Users'])
def get_users():
    return users_db

@api.get('/users/{user_id}', responses=responses, summary="Get User by ID", description="Returns a user by their ID.", tags=['Users'])
def get_user(user_id: int):
    user = next((user for user in users_db if user.user_id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@api.get('/users/{user_id}/name', responses=responses, summary="Get User Name by ID", description="Returns the name of a user by their ID.", tags=['Users'])
def get_user_name(user_id: int):
    user = next((user for user in users_db if user.user_id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {'name': user.name}

@api.get('/users/{user_id}/subscription', responses=responses, summary="Get User Subscription by ID", description="Returns the subscription of a user by their ID.", tags=['Users'])
def get_user_subscription(user_id: int):
    user = next((user for user in users_db if user.user_id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {'subscription': user.subscription}

@api.post('/users', responses=responses, summary="Create User", description="Creates a new user.", tags=['Users'])
def create_user(user:User):
    if any(u.user_id == user.user_id for u in users_db):
        raise HTTPException(status_code=400, detail="User already exists")
    users_db.append(user)
    return user
    
@api.put('/users/{user_id}', responses=responses, summary="Update User by ID", description="Updates an existing user by their ID.", tags=['Users'])
def update_user(user_id:int, user:User):
    for idx, u in enumerate(users_db):
            if u.user_id == user_id:
                users_db[idx] = user
                return user
    raise HTTPException(status_code=404, detail="User not found")


@api.delete('/users/{user_id}', responses=responses, summary="Delete User by ID", description="Deletes a user by their ID.", tags=['Users'])
def delete_user(user_id: int):
    for idx, u in enumerate(users_db):
        if u.user_id == user_id:
            del users_db[idx]
            return {"detail": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")

@api.get('/headers', summary="Get Headers", description="Returns the 'User-Agent' header from the request.", tags=['home'])
def get_headers(user_agent=Header(None)):
    return {
        'User-Agent': user_agent
    }