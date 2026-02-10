"""
Claude AI Assistant Integration for AlienPC
Provides AI-powered insights for genomic data analysis.
"""

import os
import json
import logging
from typing import Dict, Any, Optional
from flask import Blueprint, request, jsonify
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create Blueprint
claude_bp = Blueprint('claude', __name__, url_prefix='/api/claude')

# Environment variables
CLAUDE_API_KEY = os.getenv('CLAUDE_API_KEY', '')
CLAUDE_MODE = os.getenv('CLAUDE_MODE', 'cloud')  # 'cloud', 'local', or 'hybrid'
LUMO_PRIVACY_MODE = os.getenv('LUMO_PRIVACY_MODE', 'offline')  # 'offline', 'hybrid', 'cloud'

class DataSanitizer:
    """Sanitize sensitive data before sending to Claude API."""
    
    SENSITIVE_FIELDS = {
        'patient_id', 'patient_name', 'email', 'phone', 'ssn',
        'raw_sequence', 'dna_sequence', 'rna_sequence',
        'medical_record', 'diagnosis', 'treatment'
    }
    
    @staticmethod
    def sanitize_payload(data: Dict[str, Any]) -> Dict[str, Any]:
        """Remove sensitive fields from payload."""
        sanitized = {}
        for key, value in data.items():
            if key.lower() not in DataSanitizer.SENSITIVE_FIELDS:
                sanitized[key] = value
            else:
                logger.warning(f"Sanitized sensitive field: {key}")
        return sanitized
    
    @staticmethod
    def sanitize_query(query: str) -> str:
        """Remove sensitive patterns from query text."""
        # Remove common PII patterns (simplified)
        import re
        query = re.sub(r'\b\d{3}-\d{2}-\d{4}\b', '[SSN]', query)  # SSN
        query = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '[EMAIL]', query)  # Email
        return query


@claude_bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'ok',
        'mode': CLAUDE_MODE,
        'privacy_mode': LUMO_PRIVACY_MODE,
        'timestamp': datetime.utcnow().isoformat()
    }), 200


@claude_bp.route('/assist', methods=['POST'])
def assist():
    """
    Main Claude AI assistance endpoint.
    Accepts a query and returns AI-powered insights.
    """
    try:
        # Parse request
        data = request.get_json()
        if not data or 'query' not in data:
            return jsonify({'error': 'Missing query field'}), 400
        
        query = data.get('query', '').strip()
        context = data.get('context', {})
        
        # Sanitize inputs
        sanitized_query = DataSanitizer.sanitize_query(query)
        sanitized_context = DataSanitizer.sanitize_payload(context)
        
        # Check privacy mode
        if LUMO_PRIVACY_MODE == 'offline':
            return jsonify({
                'response': 'Local mode: Claude API is disabled for privacy. Use local LLM fallback.',
                'mode': 'offline',
                'timestamp': datetime.utcnow().isoformat()
            }), 200
        
        # Call Claude API (placeholder)
        response = call_claude_api(sanitized_query, sanitized_context)
        
        return jsonify({
            'response': response,
            'mode': CLAUDE_MODE,
            'timestamp': datetime.utcnow().isoformat()
        }), 200
    
    except Exception as e:
        logger.error(f"Error in /assist endpoint: {str(e)}")
        return jsonify({'error': str(e)}), 500


@claude_bp.route('/genomics-insight', methods=['POST'])
def genomics_insight():
    """
    Specialized endpoint for genomic data analysis.
    """
    try:
        data = request.get_json()
        if not data or 'data' not in data:
            return jsonify({'error': 'Missing data field'}), 400
        
        genomic_data = data.get('data', {})
        analysis_type = data.get('analysis_type', 'general')
        
        # Sanitize genomic data
        sanitized_data = DataSanitizer.sanitize_payload(genomic_data)
        
        # Build context-specific query
        query = f"Analyze {analysis_type} genomic data: {json.dumps(sanitized_data)}"
        
        # Get insight from Claude
        response = call_claude_api(query, {})
        
        return jsonify({
            'insight': response,
            'analysis_type': analysis_type,
            'timestamp': datetime.utcnow().isoformat()
        }), 200
    
    except Exception as e:
        logger.error(f"Error in /genomics-insight endpoint: {str(e)}")
        return jsonify({'error': str(e)}), 500


def call_claude_api(query: str, context: Dict[str, Any]) -> str:
    """
    Call Claude API (or local LLM fallback).
    Placeholder implementation.
    """
    if CLAUDE_MODE == 'local':
        return call_local_llm(query, context)
    elif CLAUDE_MODE == 'cloud' and CLAUDE_API_KEY:
        return call_cloud_claude(query, context)
    else:
        return "Claude API not configured. Please set CLAUDE_API_KEY and CLAUDE_MODE."


def call_cloud_claude(query: str, context: Dict[str, Any]) -> str:
    """Call OpenAI-compatible Claude API."""
    try:
        from openai import OpenAI
        
        client = OpenAI(api_key=CLAUDE_API_KEY)
        
        system_prompt = """You are an expert genomics analyst assistant for AlienPC.
        Provide clear, concise insights on genomic data.
        Always prioritize data privacy and security."""
        
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query}
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        logger.error(f"Error calling cloud Claude: {str(e)}")
        return f"Error: {str(e)}"


def call_local_llm(query: str, context: Dict[str, Any]) -> str:
    """Call local LLM (e.g., Ollama fallback)."""
    try:
        import requests
        
        response = requests.post(
            'http://localhost:11434/api/generate',
            json={
                'model': 'mistral',
                'prompt': query,
                'stream': False
            },
            timeout=30
        )
        
        if response.status_code == 200:
            return response.json().get('response', 'No response from local LLM')
        else:
            return f"Local LLM error: {response.status_code}"
    
    except Exception as e:
        logger.error(f"Error calling local LLM: {str(e)}")
        return f"Local LLM unavailable: {str(e)}"
