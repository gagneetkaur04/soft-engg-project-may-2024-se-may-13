## Test cases for authentication routes

def test_login(test_client, init_database):
    """Test login with valid credentials"""

    response = test_client.post('/auth/login', json={
        'email': 'frodo@shire.com',
        'password': 'password123'
    })

    assert response.status_code == 200
    assert 'access_token' in response.json

def test_login_invalid_credentials(test_client, init_database):
    """Test login with invalid credentials"""

    response = test_client.post('/auth/login', json={
        'email': 'test@test.com',
        'password': 'wrongpassword'
    })

    assert response.status_code == 401
    assert response.json['message'] == 'Invalid credentials'

def test_registration(test_client, init_database):
    """Test registration with valid credentials"""

    new_user = {
        'email': 'test@test.com',
        'password': 'password123',
        'first_name': 'Test',
        'last_name': 'User'
    }

    response = test_client.post('/auth/register', json=new_user)
    assert response.status_code == 201

def test_registration_existing_user(test_client, init_database):
    """Test registration with existing user"""

    new_user = {
        'email': 'test@test.com',
        'password': 'password123',
        'first_name': 'Test',
        'last_name': 'User'
    }

    response = test_client.post('/auth/register', json=new_user)
    assert response.status_code == 400
    assert response.json['message'] == 'User with this email already exists'