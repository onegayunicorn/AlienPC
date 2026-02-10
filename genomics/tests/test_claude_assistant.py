"""
Unit tests for Claude AI Assistant integration.
"""

import pytest
import json
from genomics.src.api.claude_assistant import DataSanitizer, claude_bp
from flask import Flask


class TestDataSanitizer:
    """Test the DataSanitizer class."""
    
    def test_sanitize_payload_removes_sensitive_fields(self):
        """Test that sensitive fields are removed from payload."""
        payload = {
            'patient_id': '12345',
            'patient_name': 'John Doe',
            'analysis_type': 'quality_assessment',
            'read_count': 5000
        }
        
        sanitized = DataSanitizer.sanitize_payload(payload)
        
        assert 'patient_id' not in sanitized
        assert 'patient_name' not in sanitized
        assert 'analysis_type' in sanitized
        assert 'read_count' in sanitized
    
    def test_sanitize_payload_preserves_safe_fields(self):
        """Test that safe fields are preserved."""
        payload = {
            'gc_content': 0.48,
            'average_quality': 25.3,
            'read_count': 5000
        }
        
        sanitized = DataSanitizer.sanitize_payload(payload)
        
        assert sanitized == payload
    
    def test_sanitize_query_removes_ssn(self):
        """Test that SSN patterns are removed from query."""
        query = "Patient SSN is 123-45-6789 and needs analysis"
        sanitized = DataSanitizer.sanitize_query(query)
        
        assert '[SSN]' in sanitized
        assert '123-45-6789' not in sanitized
    
    def test_sanitize_query_removes_email(self):
        """Test that email patterns are removed from query."""
        query = "Contact patient at john.doe@example.com for results"
        sanitized = DataSanitizer.sanitize_query(query)
        
        assert '[EMAIL]' in sanitized
        assert 'john.doe@example.com' not in sanitized


class TestClaudeBlueprint:
    """Test the Claude AI Blueprint endpoints."""
    
    @pytest.fixture
    def client(self):
        """Create a Flask test client."""
        app = Flask(__name__)
        app.register_blueprint(claude_bp)
        app.config['TESTING'] = True
        return app.test_client()
    
    def test_health_check_endpoint(self, client):
        """Test the health check endpoint."""
        response = client.get('/api/claude/health')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['status'] == 'ok'
        assert 'mode' in data
        assert 'privacy_mode' in data
        assert 'timestamp' in data
    
    def test_assist_endpoint_missing_query(self, client):
        """Test assist endpoint with missing query."""
        response = client.post(
            '/api/claude/assist',
            data=json.dumps({}),
            content_type='application/json'
        )
        
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data
    
    def test_assist_endpoint_with_query(self, client):
        """Test assist endpoint with valid query."""
        response = client.post(
            '/api/claude/assist',
            data=json.dumps({
                'query': 'Summarize the results',
                'context': {}
            }),
            content_type='application/json'
        )
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'response' in data
        assert 'timestamp' in data
    
    def test_genomics_insight_endpoint_missing_data(self, client):
        """Test genomics insight endpoint with missing data."""
        response = client.post(
            '/api/claude/genomics-insight',
            data=json.dumps({}),
            content_type='application/json'
        )
        
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data
    
    def test_genomics_insight_endpoint_with_data(self, client):
        """Test genomics insight endpoint with valid data."""
        response = client.post(
            '/api/claude/genomics-insight',
            data=json.dumps({
                'data': {
                    'read_count': 5000,
                    'average_quality': 25.3
                },
                'analysis_type': 'quality_assessment'
            }),
            content_type='application/json'
        )
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'insight' in data
        assert 'analysis_type' in data


class TestPrivacyModes:
    """Test privacy mode handling."""
    
    @pytest.fixture
    def client(self):
        """Create a Flask test client."""
        app = Flask(__name__)
        app.register_blueprint(claude_bp)
        app.config['TESTING'] = True
        return app.test_client()
    
    def test_offline_mode_disables_api(self, client, monkeypatch):
        """Test that offline mode disables external API calls."""
        monkeypatch.setenv('LUMO_PRIVACY_MODE', 'offline')
        
        response = client.post(
            '/api/claude/assist',
            data=json.dumps({
                'query': 'Test query',
                'context': {}
            }),
            content_type='application/json'
        )
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'offline' in data['response'].lower() or data['mode'] == 'offline'


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
