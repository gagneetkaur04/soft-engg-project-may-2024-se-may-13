## Test cases for assignment routes

def test_get_all_course_assignments(test_client, auth_token):
    """Test that the endpoint for getting all assignments for a course works correctly."""

    response = test_client.get('/assignments/course/MA1002',
                                headers={'Authorization': f'Bearer {auth_token}'})
    assert response.status_code == 200
    assert isinstance(response.json, list)

    # Test that the endpoint returns a 404 error for a nonexistent course
    response = test_client.get('/assignments/course/CS9999',
                                headers={'Authorization': f'Bearer {auth_token}'})
    assert response.status_code == 404
    assert response.json['message'] == 'Course not found'


def test_get_assignments_by_course_and_week(test_client, auth_token):
    """Test that the endpoint for getting all assignments for a given week of a course works correctly."""

    response = test_client.get('/assignments/course/MA1002/week/1',
                                headers={'Authorization': f'Bearer {auth_token}'})
    assert response.status_code == 200
    assert isinstance(response.json, list)

    # Test that the endpoint returns a 404 error for a nonexistent week
    response = test_client.get('/assignments/course/MA1002/week/100',
                                headers={'Authorization': f'Bearer {auth_token}'})
    assert response.status_code == 404
    assert response.json['message'] == 'No assignments found for this week'


def test_assignment_submission(test_client, auth_token):
    """Test that the endpoint for submitting an assignment works correctly."""

    new_submission = {
        'assignment_id': 1,
        'answers' : {"1" : "a", "2" : "b", "3" : "c", "4" : "d", "5" : "c"}
    }

    response = test_client.post('/assignments/submit',
                                json=new_submission,
                                headers={'Authorization': f'Bearer {auth_token}'})    
    assert response.status_code == 201
    assert response.json['assignment_id'] == 1
    assert 'score' in response.json


def test_repeat_assignment_submission(test_client, auth_token):
    """Test that assignments are not allowed to be submitted more than once."""

    new_submission = {
        'assignment_id': 1,
        'answers' : {"1" : "a", "2" : "b", "3" : "c", "4" : "d", "5" : "c"}
    }

    response = test_client.post('/assignments/submit',
                                json=new_submission,
                                headers={'Authorization': f'Bearer {auth_token}'})    
    assert response.status_code == 400
    assert response.json['message'] == 'Assignment already submitted'


def test_get_assignment_submissions(test_client, auth_token):
    """Test that the endpoint for getting the submission of an assignment works correctly."""

    response = test_client.get('/assignments/submission/1',
                                headers={'Authorization': f'Bearer {auth_token}'})
    
    assert response.status_code == 200
    assert isinstance(response.json, list)

    # Test that the endpoint returns a 404 error for a nonexistent assignment
    response = test_client.get('/assignments/submission/100',
                                headers={'Authorization': f'Bearer {auth_token}'})
    assert response.status_code == 404
    assert response.json['message'] == 'Assignment not found'


def test_get_assignment_grades_by_course(test_client, auth_token):
    """Test that the endpoint for getting all of a student's grades for a course works correctly."""

    response = test_client.get('/assignments/course/MA1002/grades',
                                headers={'Authorization': f'Bearer {auth_token}'})
    
    assert response.status_code == 200
    assert isinstance(response.json, list)

    # Test that the endpoint returns a 404 error for a nonexistent course
    response = test_client.get('/assignments/course/CS9999/grades',
                                headers={'Authorization': f'Bearer {auth_token}'})
    assert response.status_code == 404
    assert response.json['message'] == 'Course not found'