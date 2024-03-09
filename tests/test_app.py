def teste_post(client):

    response = client.post(
        '/users/',
        json={
            'username': 'Luiz',
            'email': 'lg.nunes.souza2006@gmail.com',
            'password': 'Bruna1608!',
        },
    )

    assert response.status_code == 201
    assert response.json() == {
        'username': 'Luiz',
        'email': 'lg.nunes.souza2006@gmail.com',
        'id': 1,
    }


def teste_db_get(client):

    response = client.get('/users-get/')

    assert response.status_code == 200
    assert response.json() == {
        'users': [
            {
                'username': 'Luiz',
                'email': 'lg.nunes.souza2006@gmail.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):

    response = client.put(
        '/users/1',
        json={
            'username': 'Nunes',
            'email': 'teste@gmail.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        'username': 'Nunes',
        'email': 'teste@gmail.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/delete/1')

    assert response.status_code == 200
    assert response.json() == {'message': 'User deleted'}


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
