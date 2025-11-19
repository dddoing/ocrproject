# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Universal Document Translator** (다국어 문서 번역 & 해석기) is an AI-powered document analysis tool that combines OCR text extraction with LLM-based translation and contextual analysis. The system goes beyond simple translation to provide contextual understanding, key information extraction, and practical advice for various document types (menus, signs, contracts, receipts, medical documents, etc.).

**Target Users**: International travelers, language learners, business professionals, and general users needing document translation and analysis.

## Tech Stack

### Backend
- **Language**: Python 3.10+
- **Framework**: FastAPI
- **OCR Engine**: EasyOCR (or Tesseract)
- **LLM**: Claude API (Anthropic) or OpenAI GPT-4
- **Image Processing**: OpenCV, Pillow

### Frontend
- **Framework**: Next.js 14+ (TypeScript)
- **UI**: Tailwind CSS, shadcn/ui
- **State Management**: Zustand or Redux Toolkit

### Infrastructure
- **Database**: PostgreSQL (user data, history)
- **Cache**: Redis (sessions, translation results)
- **Storage**: AWS S3 or Cloudinary (images)
- **Deployment**: Docker, AWS/GCP/Vercel

## Architecture

### Project Structure

```
universal-doc-translator/
├── backend/            # Python FastAPI backend
│   ├── app/
│   │   ├── main.py                 # FastAPI entry point
│   │   ├── api/
│   │   │   ├── routes.py           # API endpoints
│   │   │   └── dependencies.py
│   │   ├── core/
│   │   │   ├── config.py           # Configuration management
│   │   │   └── security.py         # Auth & security
│   │   ├── services/
│   │   │   ├── ocr_service.py      # OCR text extraction
│   │   │   ├── llm_service.py      # LLM analysis & translation
│   │   │   ├── image_service.py    # Image preprocessing
│   │   │   └── document_service.py # Document type classification
│   │   ├── models/
│   │   │   ├── database.py         # SQLAlchemy models
│   │   │   └── schemas.py          # Pydantic schemas
│   │   └── utils/
│   ├── tests/
│   └── requirements.txt
│
└── frontend/           # Next.js frontend
    ├── src/
    │   ├── app/                    # Next.js 14 app router
    │   ├── components/
    │   │   ├── ImageUploader.tsx
    │   │   ├── ResultViewer.tsx
    │   │   ├── DocumentAnalysis.tsx
    │   │   └── HistoryList.tsx
    │   ├── lib/
    │   │   └── api.ts              # Backend API client
    │   ├── hooks/
    │   │   └── useDocumentAnalysis.ts
    │   └── types/
    └── package.json
```

### Core Processing Pipeline

1. **Image Upload**: User uploads/captures document image
2. **Image Preprocessing** (`image_service.py`): Rotation correction, noise removal, contrast enhancement
3. **OCR Extraction** (`ocr_service.py`): Multi-language text recognition with confidence scores and bounding boxes
4. **Document Classification** (`document_service.py`): Automatically detect document type (menu, contract, receipt, etc.)
5. **LLM Analysis** (`llm_service.py`): Translation, summarization, key info extraction, contextual advice
6. **Result Display**: Structured response with original text, translation, key information cards, and recommendations

### Key API Endpoint

**POST /api/analyze**
- Input: Image file, target language, document type (optional)
- Output: OCR results, translation, document type, summary, extracted key info (dates, amounts, names), contextual advice
- Performance target: < 8 seconds total (OCR < 3s, LLM < 5s)

## Development Commands

### Backend Setup & Development

```bash
# Initial setup
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Download EasyOCR models (happens automatically on first run)
python -c "import easyocr; reader = easyocr.Reader(['ko', 'en'])"

# Run development server
uvicorn app.main:app --reload --port 8000

# Run tests
pytest

# Run with Docker
docker build -t doc-translator-backend .
docker run -p 8000:8000 doc-translator-backend
```

### Frontend Setup & Development

```bash
# Initial setup
cd frontend
npm install

# Run development server
npm run dev
# Access at http://localhost:3000

# Build for production
npm run build

# Run production build
npm start

# Run tests
npm test

# Type checking
npm run type-check

# Linting
npm run lint
```

### Environment Variables

Create `.env` file with:
```bash
# Required
ANTHROPIC_API_KEY=your_claude_api_key
DATABASE_URL=postgresql://user:password@localhost:5432/docdb
REDIS_URL=redis://localhost:6379

# AWS (if using S3)
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
AWS_S3_BUCKET=your_bucket_name

# Optional
OPENAI_API_KEY=your_openai_key  # If using GPT-4 instead
DEEPL_API_KEY=your_deepl_key    # For translation quality comparison

# MCP Servers (for Claude Code integration)
GITHUB_PERSONAL_ACCESS_TOKEN=ghp_your_token  # For GitHub MCP server
```

See `.env.example` for a complete template.

### MCP Server Configuration

This project uses Model Context Protocol (MCP) servers to enhance Claude Code's capabilities:

**Configured Servers** (see `.mcp.json`):

1. **GitHub MCP Server**: Enables repository management, PR creation, issue tracking
   - Requires: `GITHUB_PERSONAL_ACCESS_TOKEN` environment variable
   - Generate token at: https://github.com/settings/tokens (scopes: `repo`, `workflow`, `read:user`)

2. **Filesystem MCP Server**: Provides file operations within the project directory
   - Access restricted to: `/Users/yoo/study/alProject`
   - No additional credentials needed

3. **PostgreSQL MCP Server**: Database queries and management
   - Uses the same `DATABASE_URL` as the application
   - Enables direct database inspection and queries

**Setup PostgreSQL with Docker**:
```bash
# Start PostgreSQL container
docker run --name doc-translator-db \
  -e POSTGRES_USER=docuser \
  -e POSTGRES_PASSWORD=yourpassword \
  -e POSTGRES_DB=docdb \
  -p 5432:5432 \
  -d postgres:15

# Set environment variable
export DATABASE_URL="postgresql://docuser:yourpassword@localhost:5432/docdb"
```

**MCP Server Management**:
```bash
# List configured servers
claude mcp list

# View server details
claude mcp get github

# Check server status in Claude Code
/mcp
```

**What MCP Servers Enable**:
- GitHub: Automate PR creation, manage issues, run code reviews
- Filesystem: Enhanced file operations, project structure analysis
- PostgreSQL: Query translation history, analyze user data, manage database schema

### Docker Compose (Full Stack)

```bash
# Start all services (backend, frontend, PostgreSQL, Redis)
docker-compose up -d

# View logs
docker-compose logs -f

# Stop all services
docker-compose down
```

## Document Type Specializations

The LLM analysis adapts based on detected document type:

- **Menu**: Dish translations with descriptions, allergen detection, currency conversion, recommendations
- **Signs/Notices**: Prioritize urgent info, directional guidance, highlight warnings
- **Contracts/Legal**: Explain technical terms, highlight key clauses, risk analysis, generate checklist
- **Receipts/Invoices**: Auto-categorize items, verify totals/taxes, expense tagging
- **Medical Documents**: Translate medication names, organize dosage instructions, side effect warnings, generate consultation questions
- **Educational Materials**: Translate & summarize, explain difficult concepts, suggest references

## Performance Requirements

- **OCR Accuracy**: > 90% for printed documents
- **Translation Quality**: Native-level fluency
- **Document Classification**: > 85% accuracy
- **Response Time**: < 8 seconds end-to-end
- **Image Size Limit**: 10MB
- **Supported Formats**: JPG, PNG, PDF
- **Concurrent Users**: 100 (initial target)

## Security Considerations

- Store uploaded images with encryption
- Auto-delete temporary files after 24 hours
- Use JWT for user authentication
- Implement API rate limiting
- Keep API keys in environment variables only
- HTTPS required for all communications
- GDPR compliance for user data
- Display medical/legal advice disclaimers

## OCR Language Support

EasyOCR supports: Korean (ko), English (en), Japanese (ja), Chinese Simplified (ch_sim), Chinese Traditional (ch_tra), Spanish (es), French (fr), German (de), and many more. Configure in `ocr_service.py`:

```python
reader = easyocr.Reader(['ko', 'en', 'ja', 'ch_sim'])  # Add needed languages
```

## LLM Integration Notes

### Prompt Engineering Strategy

The `llm_service.py` should structure prompts to:
1. Provide extracted OCR text with detected language
2. Specify target translation language
3. Request document type classification
4. Ask for structured key information extraction (JSON format)
5. Request contextual advice based on document type

### Token Management

- Average input: ~1,000 tokens per request
- Average output: ~500 tokens per request
- Estimated cost: $15-30/month for 1,000 requests

## Testing Strategy

### Backend Tests
- Unit tests for each service (OCR, LLM, image preprocessing)
- Integration tests for full pipeline
- Test with various document types and languages
- Test image quality edge cases (blur, rotation, poor lighting)

### Frontend Tests
- Component tests for upload UI
- Integration tests for API calls
- E2E tests for complete user flow

### Test Data
Collect diverse document samples across all supported types and languages for comprehensive testing.

## Common Development Patterns

### Adding a New Document Type

1. Update `document_service.py` classification logic
2. Add specialized prompt template in `llm_service.py`
3. Define Pydantic schema for structured output in `models/schemas.py`
4. Update frontend `DocumentAnalysis.tsx` component to display type-specific info
5. Add tests with sample documents

### Adding a New Language

1. Add language code to EasyOCR Reader initialization
2. Update language detection logic in `ocr_service.py`
3. Test translation quality with sample documents
4. Update frontend language selector UI

## MVP Development Phases

**Phase 1 (4-6 weeks)**: Basic image upload, OCR extraction, simple translation, result display
**Phase 2 (4-6 weeks)**: Document-type specializations, user history, table extraction, PDF support
**Phase 3 (ongoing)**: Handwriting recognition, real-time camera mode, TTS, mobile app, offline mode

## Known Limitations

- OCR accuracy depends heavily on image quality
- Handwriting recognition is less accurate than printed text
- Complex layouts (multi-column, tables) require additional processing
- LLM response time scales with prompt length
- Medical/legal advice is reference only, not professional guidance

See `PROJECT_SPEC.md` for complete project requirements and roadmap.
