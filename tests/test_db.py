from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    new_user = User(
        username='Luiz',
        password='Bruna1608!',
        email='lg.nunes.souza2006@gmail.com',
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'Luiz'))

    assert user.username == 'Luiz'
