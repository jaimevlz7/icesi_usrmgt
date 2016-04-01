import pytest

import usuarios

@pytest.fixture
def client(request):
        client = service.app.test_client()
        return client

def hello(client):
        return client.get('/api/v1.0/usermgt/users', follow_redirects=True)

def test_get_users(client):
        result = get_users(client)
        assert b'operativos' in result.data
