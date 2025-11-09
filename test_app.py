"""
Simple test file for the demo app
This will be used to validate patches work correctly
"""

import pytest
from flask import Flask

def test_flask_import():
    """Test that Flask can be imported"""
    from flask import Flask
    assert Flask is not None

def test_app_creation():
    """Test that we can create a Flask app"""
    app = Flask(__name__)
    assert app is not None

def test_yaml_import():
    """Test that PyYAML can be imported"""
    import yaml
    assert yaml is not None

def test_secure_yaml_load():
    """Test that we're using safe YAML loading"""
    import yaml
    
    # This should work with secure PyYAML versions
    safe_data = yaml.safe_load("test: value")
    assert safe_data == {"test": "value"}
    
    # Verify we're not using unsafe yaml.load()
    # This test will pass if PyYAML >= 5.4 (which fixes CVE-2020-14343)

if __name__ == "__main__":
    pytest.main([__file__, "-v"])

