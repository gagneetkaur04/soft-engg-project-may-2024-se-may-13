## Test cases for notes related routes

def test_create_note(test_client, auth_token):
    """Test that the endpoint for creating a note works correctly."""

    new_note = {
        'note_content': 'This is a test note'
    }

    response = test_client.post('/notes/', 
                                json=new_note,
                                headers={'Authorization': f'Bearer {auth_token}'})
    
    assert response.status_code == 201
    assert response.json['note_content'] == 'This is a test note'

def test_get_notes(test_client, auth_token):
    """Test that the endpoint for getting notes returns a list of notes."""

    response = test_client.get('/notes/', 
                               headers={'Authorization': f'Bearer {auth_token}'})
    
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_get_single_note(test_client, auth_token):
    """Test that the endpoint for getting a single note works correctly."""

    response = test_client.get('/notes/1', 
                               headers={'Authorization': f'Bearer {auth_token}'})
    
    assert response.status_code == 200
    assert response.json['note_content'] == 'This is a test note'

    # Test that the endpoint returns a 404 error for a nonexistent note
    response = test_client.get('/notes/2',
                                 headers={'Authorization': f'Bearer {auth_token}'})
    assert response.status_code == 404
    assert response.json['message'] == 'Note with ID: 2 not found'

def test_update_note(test_client, auth_token):
    """Test that the endpoint for updating a note works correctly."""

    updated_note = {
        'note_content': 'This is an updated test note'
    }

    response = test_client.put('/notes/1', 
                               json=updated_note,
                               headers={'Authorization': f'Bearer {auth_token}'})
    
    assert response.status_code == 200
    assert response.json['note_content'] == 'This is an updated test note'

    # Test that the endpoint returns a 404 error for a nonexistent note
    response = test_client.put('/notes/2', 
                               json=updated_note,
                               headers={'Authorization': f'Bearer {auth_token}'})
    assert response.status_code == 404
    assert response.json['message'] == 'Note with ID: 2 not found'


def test_delete_note(test_client, auth_token):
    """Test that the endpoint for deleting a note works correctly."""
    
    response = test_client.delete('/notes/1',
                                  headers={'Authorization': f'Bearer {auth_token}'})
    assert response.status_code == 200

    # Test that the endpoint returns a 404 error for a nonexistent note
    response = test_client.delete('/notes/2',
                                  headers={'Authorization': f'Bearer {auth_token}'})
    assert response.status_code == 404
    assert response.json['message'] == 'Note with ID: 2 not found'