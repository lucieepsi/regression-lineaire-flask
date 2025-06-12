# tests_api/conftest.py

import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from app import app as flask_app

@pytest.fixture
def client():
    # Configure Flask en mode test
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client
        
        
        #marche pas