## Tests cases for the chat endpoints

def test_create_chat(test_client, auth_token):
    """Test that the endpoint for starting a chat works correctly."""

    new_chat = {
        'message': 'hello! tell me a cool fact that i may not know'
    }

    response = test_client.post('/chat/start', 
                                json=new_chat,
                                headers={'Authorization': f'Bearer {auth_token}'})
    
    assert response.status_code == 201
    assert response.json['user_message']['message_text'] == new_chat['message']

def test_continue_chat(test_client, auth_token):
    """Test that the endpoint for continuing an existing chat works correctly."""

    continue_chat = {
        'message': 'now tell me another cool fact!'
    }

    response = test_client.post('/chat/continue/1',
                                json=continue_chat,
                                headers={'Authorization': f'Bearer {auth_token}'}) 
    assert response.status_code == 200
    assert response.json['user_message']['message_text'] == continue_chat['message']

    # Test that the endpoint returns a 404 error for a nonexistent conversation
    response = test_client.post('/chat/continue/2',
                                json=continue_chat,
                                headers={'Authorization': f'Bearer {auth_token}'})
    assert response.status_code == 404
    assert response.json['message'] == 'Conversation not found'


def test_get_all_chats(test_client, auth_token):
    """Test that the endpoint for getting all chats works correctly."""

    response = test_client.get('/chat/conversations',
                               headers={'Authorization': f'Bearer {auth_token}'})
    
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_get_single_chat(test_client, auth_token):
    """Test that the endpoint for getting a single chat works correctly."""

    response = test_client.get('/chat/conversations/1',
                               headers={'Authorization': f'Bearer {auth_token}'})
    assert response.status_code == 200

    # Test that the endpoint returns a 404 error for a nonexistent conversation
    response = test_client.get('/chat/conversations/2',
                               headers={'Authorization': f'Bearer {auth_token}'})
    assert response.status_code == 404
    assert response.json['message'] == 'Conversation not found'


def test_delete_chat(test_client, auth_token):
    """Test that the endpoint for deleting a chat works correctly."""
    
    response = test_client.delete('/chat/conversations/1',
                                  headers={'Authorization': f'Bearer {auth_token}'})
    assert response.status_code == 200

    # Test that the endpoint returns a 404 error for a nonexistent conversation
    response = test_client.delete('/chat/conversations/2',
                                  headers={'Authorization': f'Bearer {auth_token}'})
    assert response.status_code == 404
    assert response.json['message'] == 'Conversation not found'