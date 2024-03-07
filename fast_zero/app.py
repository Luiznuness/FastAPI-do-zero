from fastapi import FastAPI, HTTPException

from fast_zero.schemas import Massage, UserDB, UserList, UserPublic, UserSchema

app = FastAPI()

database = []


@app.get('/users-get/', status_code=200, response_model=UserList)
def read_users():
    return {'users': database}


@app.post('/users/', status_code=201, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)

    database.append(user_with_id)

    return user_with_id


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code=404, detail='User not found')

    user_with_id = UserDB(**user.model_dump(), id=user_id)
    database[user_id - 1] = user_with_id

    return user_with_id


@app.delete('/users/delete/{user_id}', response_model=Massage)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code=404, detail='User Not found')

    del database[user_id - 1]

    return {'message': 'User deleted'}


# Response Json
"""
@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}
"""

# Response HTML
"""
@app.get('/', response_class=HTMLResponse)
def read_root():
      return  <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>
    """

# Aula 'Introdução ao desenvolvimento WEB'
'''@app.get('/response_json', response_model=Massage)
def read_root():
    return {'message': 'Olár Mundo!!'}


@app.get('/html_text', response_class=HTMLResponse)
def read_root_htlm():
    return """ 
        <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olár Mundo!! </h1>
      </body>
    </html>
"""
'''
