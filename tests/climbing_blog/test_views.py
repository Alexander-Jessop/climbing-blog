'''
A test module for the views of the climbing blog.
'''


def test_index_ok(client):
    '''
    Test that the index page loads and returns a 200.
    '''
    response = client.get('/')
    assert response.status_code == 200
