# Quick Setup Guide

## Prerequisites

- Python 3.10+
- Node.js 18+
- Docker & Docker Compose (optional but recommended)

## Option 1: Docker Compose (Easiest)

```bash
# 1. Set up environment variables
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY

# 2. Start all services
docker-compose up -d

# 3. Access the application
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/api/docs
```

## Option 2: Manual Setup

### Backend

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start database services (using Docker)
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

### Frontend

```bash
# Navigate to frontend (in new terminal)
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

Access at http://localhost:3000

## Required Environment Variables

Edit `.env` file:

```bash
# REQUIRED - Get from https://console.anthropic.com/
ANTHROPIC_API_KEY=your_key_here

# DATABASE (auto-configured in docker-compose)
DATABASE_URL=postgresql://docuser:yourpassword@localhost:5432/docdb
REDIS_URL=redis://localhost:6379
```

## Verification

1. Backend health check:
   ```bash
   curl http://localhost:8000/health
   ```

2. Upload a test image at http://localhost:3000

## Troubleshooting

### Backend won't start
- Check Python version: `python --version` (should be 3.10+)
- Check PostgreSQL is running: `docker ps | grep postgres`
- Verify API key in `.env`

### Frontend won't start
- Check Node version: `node --version` (should be 18+)
- Clear cache: `rm -rf frontend/.next`
- Reinstall: `cd frontend && rm -rf node_modules && npm install`

### OCR not working
- EasyOCR models download automatically on first run
- This may take several minutes initially
- Check backend logs: `docker-compose logs backend`

## Next Steps

1. Read `README.md` for complete documentation
2. See `CLAUDE.md` for development guide
3. Visit API docs at http://localhost:8000/api/docs
4. Check `PROJECT_SPEC.md` for feature roadmap
