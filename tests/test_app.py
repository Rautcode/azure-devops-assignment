import pytest
import json
from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    """Test the main route returns Hello World message."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello World' in response.data
    assert b'Azure DevOps' in response.data

def test_health_check(client):
    """Test the health check endpoint."""
    response = client.get('/health')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['status'] == 'healthy'
    assert 'message' in data

def test_app_info(client):
    """Test the app info endpoint."""
    response = client.get('/info')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['app'] == 'Hello World Flask App'
    assert data['version'] == '1.0.0'
    assert 'environment' in data

def test_invalid_route(client):
    """Test that invalid routes return 404."""
    response = client.get('/nonexistent')
    assert response.status_code == 404

class TestAdvancedScenarios:
    """Advanced test scenarios for comprehensive coverage."""
    
    def test_environment_variable_handling(self, client, monkeypatch):
        """Test environment variable is properly handled."""
        monkeypatch.setenv('ENVIRONMENT', 'testing')
        response = client.get('/info')
        data = json.loads(response.data)
        assert data['environment'] == 'testing'
    
    def test_json_response_format(self, client):
        """Test JSON responses have correct content type."""
        response = client.get('/health')
        assert response.content_type == 'application/json'
        
        response = client.get('/info')
        assert response.content_type == 'application/json'
    
    def test_cors_headers(self, client):
        """Test CORS headers are not present (security best practice)."""
        response = client.get('/')
        assert 'Access-Control-Allow-Origin' not in response.headers
