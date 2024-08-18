## Test cases for course related routes

def test_get_courses(test_client, auth_token):
    """Test that the endpoint for getting courses returns a list of courses."""

    response = test_client.get('/courses/', 
                               headers={'Authorization': f'Bearer {auth_token}'})
    
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_get_single_course(test_client, auth_token):
    """Test that the endpoint for getting a single course works correctly."""

    response = test_client.get('/courses/CS1002', 
                               headers={'Authorization': f'Bearer {auth_token}'})
    
    assert response.status_code == 200
    assert response.json['title'] == 'Programming in Python'

    # Test that the endpoint returns a 404 error for a nonexistent course
    response = test_client.get('/courses/CS9999', 
                               headers={'Authorization': f'Bearer {auth_token}'})
    assert response.status_code == 404

def test_get_course_contents(test_client, auth_token):
    """Test that the endpoint for getting course contents returns the contents of a course."""

    response = test_client.get('/courses/CS1002/contents', 
                               headers={'Authorization': f'Bearer {auth_token}'})
    
    assert response.status_code == 200
    assert 'course_id' in response.json
    assert 'course_title' in response.json
    assert 'weeks' in response.json