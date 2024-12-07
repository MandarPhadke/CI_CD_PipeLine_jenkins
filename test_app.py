import pytest
from app import app  # Adjust if your main Flask file has a different name

@pytest.fixture
def client():
    # Create a test client for the Flask app
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Test the home route to ensure it returns the correct template and content"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Login" in response.data  # Ensure the HTML content is correct