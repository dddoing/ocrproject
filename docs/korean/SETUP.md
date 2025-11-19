# 빠른 설정 가이드

## 사전 요구사항

- Python 3.10+
- Node.js 18+
- Docker & Docker Compose (선택사항이지만 권장)

## 옵션 1: Docker Compose (가장 쉬움)

```bash
# 1. 환경 변수 설정
cp .env.example .env
# .env 파일을 편집하여 ANTHROPIC_API_KEY를 추가하세요

# 2. 모든 서비스 시작
docker-compose up -d

# 3. 애플리케이션 접속
# 프론트엔드: http://localhost:3000
# 백엔드 API: http://localhost:8000
# API 문서: http://localhost:8000/api/docs
```

## 옵션 2: 수동 설정

### 백엔드

```bash
# 백엔드 디렉토리로 이동
cd backend

# 가상 환경 생성
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt

# 데이터베이스 서비스 시작 (Docker 사용)
docker run --name doc-translator-db \
  -e POSTGRES_USER=docuser \
  -e POSTGRES_PASSWORD=yourpassword \
  -e POSTGRES_DB=docdb \
  -p 5432:5432 -d postgres:15

docker run --name doc-translator-redis \
  -p 6379:6379 -d redis:7-alpine

# 백엔드 실행
uvicorn app.main:app --reload --port 8000
```

### 프론트엔드

```bash
# 프론트엔드로 이동 (새 터미널에서)
cd frontend

# 의존성 설치
npm install

# 개발 서버 실행
npm run dev
```

http://localhost:3000 에서 접속

## 필수 환경 변수

`.env` 파일 편집:

```bash
# 필수 - https://console.anthropic.com/ 에서 발급
ANTHROPIC_API_KEY=your_key_here

# DATABASE (docker-compose에서 자동 설정)
DATABASE_URL=postgresql://docuser:yourpassword@localhost:5432/docdb
REDIS_URL=redis://localhost:6379
```

## 검증

1. 백엔드 헬스 체크:
   ```bash
   curl http://localhost:8000/health
   ```

2. http://localhost:3000 에서 테스트 이미지 업로드

## 문제 해결

### 백엔드가 시작되지 않음
- Python 버전 확인: `python --version` (3.10+ 이어야 함)
- PostgreSQL이 실행 중인지 확인: `docker ps | grep postgres`
- `.env` 파일에서 API 키 확인

### 프론트엔드가 시작되지 않음
- Node 버전 확인: `node --version` (18+ 이어야 함)
- 캐시 삭제: `rm -rf frontend/.next`
- 재설치: `cd frontend && rm -rf node_modules && npm install`

### OCR이 작동하지 않음
- EasyOCR 모델은 첫 실행 시 자동으로 다운로드됩니다
- 처음에는 몇 분이 걸릴 수 있습니다
- 백엔드 로그 확인: `docker-compose logs backend`

## 다음 단계

1. 전체 문서는 `README.md` 참조
2. 개발 가이드는 `CLAUDE.md` 참조
3. API 문서는 http://localhost:8000/api/docs 방문
4. 기능 로드맵은 `PROJECT_SPEC.md` 확인
