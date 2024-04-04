from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from fast_zero.database import get_session
from fast_zero.models import User
from fast_zero.schemas import Massage, UserList, UserPublic, UserSchema

app = FastAPI()


@app.post('/users/', response_model=UserPublic, status_code=201)
def create_user(user: UserSchema, session: Session = Depends(get_session)):
    db_user = session.scalar(
        select(User).where(User.username == user.username)
    )

    if db_user:
        raise HTTPException(
            status_code=404, detail='Username already registered'
        )

    db_user = User(
        username=user.username, password=user.password, email=user.email
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


@app.get('/users-get/', status_code=200, response_model=UserList)
def read_users(
    skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):
    users = session.scalars(select(User).offset(skip).limit(limit)).all()
    return {'users': users}


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(
    user_id: int, user: UserSchema, session: Session = Depends(get_session)
):

    db_user = session.scalar(select(User).where(User.id == user_id))
    if not db_user:
        raise HTTPException(status_code=404, detail='User not found')

    db_user.username = user.username
    db_user.password = user.password
    db_user.email = user.email
    session.commit()
    session.refresh(db_user)

    return db_user


@app.delete('/users/delete/{user_id}', response_model=Massage)
def delete_user(user_id: int, session: Session = Depends(get_session)):
    db_user = session.scalar(select(User).where(User.id == user_id))

    if not db_user:
        raise HTTPException(status_code=404, detail='User not found')

    session.delete(db_user)
    session.commit()

    return {'message': 'User deleted'}


"""
@app.get('/users/{user_id}', status_code=200, response_model=UserPublic)
def get_id(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code=404, detail='User Not found')

    user_with_id = database[user_id - 1]

    return user_with_id






"""
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
'''
@app.get('/response_json', response_model=Massage)
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
