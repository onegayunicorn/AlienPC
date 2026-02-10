# AlienPC Lumo AI Integration

## Overview

AlienPC v1.0.1 integrates **Lumo AI** (Claude-powered) for on-device writing assistance and genomic insights. This document outlines the integration architecture, privacy guarantees, and usage instructions.

## Architecture

### Backend Components

**Claude AI Assistant Module** (`genomics/src/api/claude_assistant.py`)
- Flask Blueprint providing `/api/claude/*` endpoints
- Data sanitization layer to remove PII before API calls
- Support for cloud, local, and hybrid privacy modes
- Error handling and logging

**REST Server Integration** (`genomics/src/api/rest_server.py`)
- Registers Claude Blueprint
- Exposes health check and genomics-specific endpoints
- Version tracking (v1.0.1+)

### Frontend Components

**Dashboard Widget** (`apps/web-dashboard/index.html`)
- Vue.js-based chat interface
- Consent modal for privacy acknowledgment
- Real-time message streaming
- Privacy mode indicator

## Privacy Modes

AlienPC supports three privacy modes controlled by the `LUMO_PRIVACY_MODE` environment variable:

| Mode | Description | Use Case |
|------|-------------|----------|
| `offline` | All processing local; no external API calls | Highly regulated labs, air-gapped systems |
| `hybrid` | Sanitized data sent to Claude; user can review before sending | Standard research environments |
| `cloud` | Full cloud integration; assumes user accepts cloud processing | Development, non-sensitive data |

### Data Sanitization

The `DataSanitizer` class removes sensitive fields before any API call:

**Removed Fields:**
- `patient_id`, `patient_name`
- `email`, `phone`, `ssn`
- `raw_sequence`, `dna_sequence`, `rna_sequence`
- `medical_record`, `diagnosis`, `treatment`

**Sanitized Patterns:**
- Social Security Numbers (XXX-XX-XXXX)
- Email addresses
- Phone numbers

## API Endpoints

### Health Check
```bash
GET /api/claude/health
```
Response:
```json
{
  "status": "ok",
  "mode": "cloud",
  "privacy_mode": "offline",
  "timestamp": "2026-02-10T12:34:56.789Z"
}
```

### General Assistance
```bash
POST /api/claude/assist
Content-Type: application/json

{
  "query": "Summarize the synthetic base detection results",
  "context": {
    "synthetic_bases": 42,
    "confidence": 0.95
  }
}
```

Response:
```json
{
  "response": "Based on your data, the synthetic base detection shows...",
  "mode": "cloud",
  "timestamp": "2026-02-10T12:34:56.789Z"
}
```

### Genomic Analysis
```bash
POST /api/claude/genomics-insight
Content-Type: application/json

{
  "data": {
    "read_count": 5000,
    "average_quality": 25.3,
    "gc_content": 0.48
  },
  "analysis_type": "quality_assessment"
}
```

Response:
```json
{
  "insight": "Your sequencing run shows good quality metrics...",
  "analysis_type": "quality_assessment",
  "timestamp": "2026-02-10T12:34:56.789Z"
}
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `CLAUDE_API_KEY` | (empty) | OpenAI API key for Claude access |
| `CLAUDE_MODE` | `cloud` | Mode: `cloud`, `local`, or `hybrid` |
| `LUMO_PRIVACY_MODE` | `offline` | Privacy mode: `offline`, `hybrid`, or `cloud` |

## Setup Instructions

### 1. Set Environment Variables
```bash
export CLAUDE_API_KEY="your-api-key-here"
export CLAUDE_MODE="cloud"
export LUMO_PRIVACY_MODE="offline"
```

### 2. Start the API Server
```bash
python3 /opt/alienpc/genomics/src/api/rest_server.py
```

### 3. Access the Dashboard
Open your browser to `http://localhost:8080` and use the Claude AI widget.

## Local LLM Fallback (Optional)

For completely offline operation, you can use Ollama with a local model:

### Install Ollama
```bash
curl https://ollama.ai/install.sh | sh
ollama pull mistral
ollama serve
```

### Configure AlienPC
```bash
export CLAUDE_MODE="local"
export LUMO_PRIVACY_MODE="offline"
```

The API will automatically fall back to `http://localhost:11434/api/generate` for local inference.

## Security Best Practices

1. **Always sanitize inputs** before sending to external APIs
2. **Use offline mode** for sensitive genomic data
3. **Review consent dialogs** before enabling cloud features
4. **Rotate API keys** regularly
5. **Monitor API logs** for suspicious activity

## Testing

### Unit Tests
```bash
python3 -m pytest genomics/tests/test_claude_assistant.py
```

### Integration Tests
```bash
# Health check
curl http://localhost:5000/api/claude/health

# Test query
curl -X POST http://localhost:5000/api/claude/assist \
  -H "Content-Type: application/json" \
  -d '{"query": "Test query", "context": {}}'
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "Claude API not configured" | Set `CLAUDE_API_KEY` and `CLAUDE_MODE` |
| "Local LLM unavailable" | Ensure Ollama is running on port 11434 |
| "Privacy mode: offline" | Change `LUMO_PRIVACY_MODE` to enable cloud features |
| Widget not appearing | Check browser console for errors; verify API is running |

## Future Enhancements

- [ ] Real-time streaming responses
- [ ] Custom model fine-tuning for genomics
- [ ] Multi-language support
- [ ] Advanced caching for common queries
- [ ] Integration with external genomics databases

## Support

For Lumo-specific questions: https://proton.me/support/lumo
For AlienPC issues: https://github.com/onegayunicorn/AlienPC/issues
