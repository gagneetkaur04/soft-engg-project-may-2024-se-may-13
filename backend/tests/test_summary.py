## Test cases for AI summary endpoints

def test_generate_lecture_summary(test_client, auth_token):
    """Test that the endpoint for generating a summary of a lecture works correctly."""

    response = test_client.get('/summary/1',
                                headers={'Authorization': f'Bearer {auth_token}'})
    assert response.status_code == 200
    assert 'summary' in response.json

    # Test that the endpoint returns a 404 error when a lecture transcript is not found
    response = test_client.get('/summary/1000',
                                headers={'Authorization': f'Bearer {auth_token}'})
    assert response.status_code == 404
    assert response.json['message'] == 'Lecture transcript unavailable, summary generation failed'
