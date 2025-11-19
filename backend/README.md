# Universal Document Translator - Backend

FastAPI backend for OCR and document translation.

## Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
cp ../.env.example .env
# Edit .env with your API keys

# Run development server
uvicorn app.main:app --reload --port 8000
```

## API Documentation

Once running, visit:
- Swagger UI: http://localhost:8000/api/docs
- ReDoc: http://localhost:8000/api/redoc

## Testing

```bash
pytest
```

## Docker

```bash
docker build -t doc-translator-backend .
docker run -p 8000:8000 doc-translator-backend
```
