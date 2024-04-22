from fast_zero.schemas import UserPublic


def test_create_user(client):
    response = client.post(
        '/users/',
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
    response = client.get('/users/get-users/')

    assert response.status_code == 200
    assert response.json() == {'users': []}


def test_read_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/get-users/')

    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user, token):
    response = client.put(
        f'/users/update/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'Nunes',
            'email': 'Nunes@gmail.com',
            'password': 'testtest',
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        'username': 'Nunes',
        'email': 'Nunes@gmail.com',
        'id': 1,
    }


def test_delete_user(client, user, token):
    response = client.delete(
        f'/users/delete/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
    )
    assert response.status_code == 200
    assert response.json() == {'message': 'User deleted'}


def test_error_put(client, user, token):
    response = client.put(
        f'/users/update/{2}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'Luiz',
            'email': 'luiz@test.com',
            'password': 'TesteLuiz',
        },
    )

    assert response.status_code == 400
    assert response.json() == {'detail': 'Not enough permissions'}


def test_error_delete(client, user, token):
    response = client.delete(
        f'/users/delete/{2}',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == 400
    assert response.json() == {'detail': 'Not enough permissions'}
