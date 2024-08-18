## Test cases for the programming assignments endpoints

def test_get_all_prog_assignments(test_client, auth_token):
    """Test that the endpoint for getting all programming assignments works correctly."""

    response = test_client.get('/programming_assignments/', 
                               headers={'Authorization': f'Bearer {auth_token}'})
    
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_get_single_prog_assignment(test_client, auth_token):
    """Test that the endpoint for getting a single programming assignment works correctly."""

    response = test_client.get('/programming_assignments/1', 
                               headers={'Authorization': f'Bearer {auth_token}'})
    assert response.status_code == 200

    # Test that the endpoint returns a 404 error for a nonexistent programming assignment
    response = test_client.get('/programming_assignments/100', 
                               headers={'Authorization': f'Bearer {auth_token}'})
    assert response.status_code == 404
    assert response.json['message'] == "Programming assignment 100 doesn't exist"

def test_submit_prog_assignment(test_client, auth_token):
    """Test that the endpoint for submitting a programming assignment works correctly."""

    new_submission = {
        'code' : 'def main(l):\n\t return sorted(l)',
    }

    # this assignment tests whether the user written function sorts the list
    response = test_client.post('/programming_assignments/1/submit', 
                                json=new_submission,
                                headers={'Authorization': f'Bearer {auth_token}'})
    assert response.status_code == 201
    assert response.json['prog_assignment_id'] == 1
    assert response.json['code'] == new_submission['code']
    assert 'score' in response.json    

def test_submit_prog_assignment_invalid_code(test_client, auth_token):
    """Test that an invalid code submission is rejected and errors out"""

    new_submission = {
        'code' : 'def main(n):\n\t return in#val!d_code', # this will obviously fail
    }

    # this assignment tests whether the user written function calculates the factorial of a number
    response = test_client.post('/programming_assignments/2/submit', 
                                json=new_submission,
                                headers={'Authorization': f'Bearer {auth_token}'})
    assert response.status_code == 400
    assert 'message' in response.json # error message should be present

def test_get_all_submissions(test_client, auth_token):
    """Test that the endpoint for getting all the user assignment submissions works correctly."""
    
    response = test_client.get('/programming_assignments/grades', 
                               headers={'Authorization': f'Bearer {auth_token}'})
    assert response.status_code == 200
    assert isinstance(response.json, list)