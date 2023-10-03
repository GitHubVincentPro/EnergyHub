import pytest
from app import create_app

@pytest.fixture
def client():
app = create_app()
app.config['TESTING'] = True
return app.test_client()

def test_predictions(client):
response = client.get('/predictions')
assert response.status_code == 200