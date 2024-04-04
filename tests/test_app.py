from fast_zero.schemas import UserPublic


def test_create_user(client):
    response = client.post(
        '/users',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == 201
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }


def test_read_get(client):
    response = client.get('/users-get/')

    assert response.status_code == 200
    assert response.json() == {'users': []}


def test_read_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users-get/')

    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user):
    response = client.put(
        '/users/1',
        json={
            'username': 'Nunes',
            'email': 'Nunes@gmail.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        'username': 'Nunes',
        'email': 'Nunes@gmail.com',
        'id': 1,
    }


def test_delete_user(client, user):
    response = client.delete('/users/delete/1')
    assert response.status_code == 200
    assert response.json() == {'message': 'User deleted'}


def test_error_put(client, user):
    response = client.put(
        '/users/2',
        json={
            'username': 'Luiz',
            'email': 'luiz@test.com',
            'password': 'TesteLuiz',
        },
    )

    assert response.status_code == 404
    assert response.json() == {'detail': 'User not found'}


def test_error_delete(client, user):
    response = client.delete('/users/delete/2')

    assert response.status_code == 404
    assert response.json() == {'detail': 'User not found'}


def test_erro_post(client, user):
    response = client.post(
        '/users/',
        json={
            'username': 'Luiz',
            'email': 'luiz@test.com',
            'password': 'TesteLuiz',
        },
    )

    assert response.status_code == 404
    assert response.json() == {'detail': 'Username already registered'}


"""


def test_error_update(client):

    response = client.put(
        '/users/0',
        json={
            'username': 'Nunes',
            'email': 'teste@gmail.com',
            'password': 'mynewpassword',
        },
    )

    assert response.status_code == 404
    assert response.json() == {'detail': 'User Not found'}


def test_error_delete(client):
    response = client.delete('/users/delete/0')

    assert response.status_code == 404
    assert response.json() == {'detail': 'User Not found'}


def test_get_id(client):

    client.post(
        '/users/',
        json={
            'username': 'Test',
            'email': 'test@gmail.com',
            'password': 'test!',
        },
    )

    client.post(
        '/users/',
        json={
            'username': 'Luiz',
            'email': 'Gustavo@gmail.com',
            'password': 'test!',
        },
    )
    response = client.get('/users/2')

    assert response.status_code == 200
    assert response.json() == {
        'username': 'Luiz',
        'email': 'Gustavo@gmail.com',
        'id': 2,
    }


def test_error_getID(client):
    response = client.get('/users/0')

    assert response.status_code == 404
    assert response.json() == {'detail': 'User Not found'}

"""

"""def teste_get(client):

retorno = client.get('/')

assert retorno.status_code == 200
assert retorno.json() == {'message': 'Olá Mundo!'}"""

"""def teste_return_ola_mundo():
    client = TestClient(app)

    retorno = client.get('/response_json')

    assert retorno.status_code == 200
    assert retorno.json() == {'message': 'Olár Mundo!!'}

    response = client.get('/html_text')

    texto = response.text

    assert response.status_code == 200
    assert texto.count('Olár Mundo!!') == 1"""
