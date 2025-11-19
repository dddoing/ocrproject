# Universal Document Translator

AI-powered document OCR, translation, and analysis tool that goes beyond simple translation to provide contextual understanding and practical insights.

## Features

- **Multi-language OCR**: Extract text from documents in Korean, English, Japanese, Chinese, and more
- **Intelligent Translation**: Context-aware translation with cultural considerations
- **Document Classification**: Automatically detect document types (menus, contracts, receipts, etc.)
- **Key Information Extraction**: Automatically extract dates, amounts, contacts, and other structured data
- **Contextual Advice**: Get practical advice based on document type and content
- **Document-Type Specializations**: Tailored analysis for menus, contracts, medical documents, and more

## Tech Stack

### Backend
- Python 3.10+ with FastAPI
- EasyOCR for text extraction
- Claude API (Anthropic) for LLM analysis
- PostgreSQL for data storage
- Redis for caching

### Frontend
- Next.js 14 with TypeScript
- React for UI components
- Tailwind CSS for styling
- Axios for API communication

## Quick Start

### Using Docker Compose (Recommended)

```bash
# Clone the repository
git clone https://github.com/dddoing/ocrproject.git
cd ocrproject

# Copy environment variables
cp .env.example .env
# Edit .env with your API keys

# Start all services
docker-compose up -d

# View logs
docker-compose logs -f
```

Access the app at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/api/docs

### Manual Setup

#### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Start PostgreSQL and Redis (or use Docker)
docker run --name doc-translator-db \
  -e POSTGRES_USER=docuser \
  -e POSTGRES_PASSWORD=yourpassword \
  -e POSTGRES_DB=docdb \
  -p 5432:5432 -d postgres:15

docker run --name doc-translator-redis \
  -p 6379:6379 -d redis:7-alpine

# Run backend
uvicorn app.main:app --reload --port 8000
```

#### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Environment Variables

Create a `.env` file in the project root with:

```bash
# Required
ANTHROPIC_API_KEY=your_claude_api_key
DATABASE_URL=postgresql://docuser:yourpassword@localhost:5432/docdb
REDIS_URL=redis://localhost:6379

# Optional
OPENAI_API_KEY=your_openai_key
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
```

See `.env.example` for all available options.

## API Usage

### Analyze Document

```bash
curl -X POST "http://localhost:8000/api/analyze" \
  -F "file=@document.jpg" \
  -F "target_language=en" \
  -F "document_type=menu"
```

Response:
```json
{
  "ocr_result": {
    "full_text": "Extracted text...",
    "segments": [...],
    "detected_languages": ["ko", "en"],
    "confidence": 0.95
  },
  "analysis": {
    "document_type": "menu",
    "translation": "Translated text...",
    "summary": "Summary...",
    "key_info": {
      "items": ["Item 1", "Item 2"],
      "prices": ["$10", "$15"]
    },
    "advice": "Practical advice..."
  }
}
```

## Document Types Supported

- **Menu**: Dish translations, allergen detection, price conversion
- **Contract**: Legal term explanations, key clause highlights, risk analysis
- **Receipt/Invoice**: Item categorization, total verification, expense tagging
- **Medical**: Medication translation, dosage instructions, side effect warnings
- **Signs/Notices**: Emergency info prioritization, directional guidance
- **Educational**: Content translation, concept explanations, reference suggestions

## Development

### Backend Tests

```bash
cd backend
pytest
```

### Frontend Tests

```bash
cd frontend
npm test
```

### Linting

```bash
# Backend
cd backend
flake8 app/

# Frontend
cd frontend
npm run lint
```

## Project Structure

```
ocrproject/
├── backend/              # Python FastAPI backend
│   ├── app/
│   │   ├── api/          # API routes
│   │   ├── core/         # Configuration & security
│   │   ├── services/     # Business logic (OCR, LLM, etc.)
│   │   ├── models/       # Database models & schemas
│   │   └── utils/        # Helper functions
│   ├── tests/            # Backend tests
│   └── requirements.txt
│
├── frontend/             # Next.js frontend
│   ├── src/
│   │   ├── app/          # Next.js 14 app router
│   │   ├── components/   # React components
│   │   ├── lib/          # API client & utilities
│   │   ├── hooks/        # Custom React hooks
│   │   └── types/        # TypeScript types
│   └── package.json
│
├── docker-compose.yml    # Docker Compose configuration
├── .env.example          # Environment variables template
└── CLAUDE.md             # Claude Code development guide
```

## Performance

- **OCR Processing**: < 3 seconds per image
- **LLM Analysis**: < 5 seconds
- **Total Response Time**: < 8 seconds end-to-end
- **OCR Accuracy**: > 90% for printed documents
- **Image Size Limit**: 10MB
- **Supported Formats**: JPG, PNG, PDF

## Security

- Images encrypted at rest
- Temporary files auto-deleted after 24 hours
- JWT authentication for user endpoints
- API rate limiting
- GDPR compliant data handling

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## License

MIT License - see LICENSE file for details

## Support

- Documentation: See `CLAUDE.md` and `MCP_SETUP_GUIDE.md`
- Issues: https://github.com/dddoing/ocrproject/issues
- API Docs: http://localhost:8000/api/docs

## Acknowledgments

- EasyOCR for multi-language OCR
- Anthropic Claude for LLM capabilities
- FastAPI for the backend framework
- Next.js for the frontend framework
