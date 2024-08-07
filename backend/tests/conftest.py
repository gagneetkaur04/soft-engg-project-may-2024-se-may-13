import pytest
from app import create_app, db
from app.utils import insert_default_courses, insert_default_instructors, insert_default_programming_assignments, insert_default_assignments_stats
from app.services.user_service import UserService

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('testing')
    
    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!


# the module level scope for a fixture means that the fixture is set up
# once for the module and then all tests in that module use the same fixture
@pytest.fixture(scope='module')
def init_database(test_client):
    # Create the database and the database table
    db.create_all()

    # Insert default instructors and courses
    insert_default_instructors()
    insert_default_courses()

    # Insert some default assignments (for example from the Stats - 1 course)
    insert_default_assignments_stats()

    # Insert default programming assignments
    insert_default_programming_assignments()

    # Insert some random student for testing
    UserService.create_user('frodo', 'baggins', 'frodo@shire.com', 'password123')

    yield db # this is where the testing happens!

    # teardown
    db.drop_all()

@pytest.fixture(scope='module')
def auth_token(test_client, init_database):
    # this fixture depends on the init_database fixture
    # so whenever it is used, it will first call init_database and then proceed further

    # Create a valid auth token for testing protected routes
    response = test_client.post('/auth/login', json={
        'email': 'frodo@shire.com',
        'password': 'password123'
    })
    token = response.json['access_token']
    return token