# Universal Document Translator

단순 번역을 넘어 문맥적 이해와 실용적 인사이트를 제공하는 AI 기반 문서 OCR, 번역 및 분석 도구입니다.

## 주요 기능

- **다국어 OCR**: 한국어, 영어, 일본어, 중국어 등 다양한 언어의 문서에서 텍스트 추출
- **지능형 번역**: 문화적 고려사항을 포함한 문맥 인식 번역
- **문서 분류**: 메뉴, 계약서, 영수증 등 문서 유형 자동 감지
- **핵심 정보 추출**: 날짜, 금액, 연락처 등 구조화된 데이터 자동 추출
- **문맥 기반 조언**: 문서 유형과 내용에 기반한 실용적인 조언 제공
- **문서 유형별 특화**: 메뉴, 계약서, 의료 문서 등에 맞춤화된 분석

## 기술 스택

### 백엔드
- Python 3.10+ with FastAPI
- EasyOCR (텍스트 추출)
- Claude API (Anthropic) (LLM 분석)
- PostgreSQL (데이터 저장)
- Redis (캐싱)

### 프론트엔드
- Next.js 14 with TypeScript
- React (UI 컴포넌트)
- Tailwind CSS (스타일링)
- Axios (API 통신)

## 빠른 시작

### Docker Compose 사용 (권장)

```bash
# 저장소 클론
git clone https://github.com/dddoing/ocrproject.git
cd ocrproject

# 환경 변수 복사
cp .env.example .env
# API 키를 .env 파일에 입력하세요

# 모든 서비스 시작
docker-compose up -d

# 로그 확인
docker-compose logs -f
```

애플리케이션 접속:
- 프론트엔드: http://localhost:3000
- 백엔드 API: http://localhost:8000
- API 문서: http://localhost:8000/api/docs

### 수동 설정

#### 백엔드

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# PostgreSQL과 Redis 시작 (또는 Docker 사용)
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

#### 프론트엔드

```bash
cd frontend
npm install
npm run dev
```

## 환경 변수

프로젝트 루트에 `.env` 파일을 생성하세요:

```bash
# 필수
ANTHROPIC_API_KEY=your_claude_api_key
DATABASE_URL=postgresql://docuser:yourpassword@localhost:5432/docdb
REDIS_URL=redis://localhost:6379

# 선택사항
OPENAI_API_KEY=your_openai_key
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
```

사용 가능한 모든 옵션은 `.env.example` 파일을 참조하세요.

## API 사용법

### 문서 분석

```bash
curl -X POST "http://localhost:8000/api/analyze" \
  -F "file=@document.jpg" \
  -F "target_language=en" \
  -F "document_type=menu"
```

응답:
```json
{
  "ocr_result": {
    "full_text": "추출된 텍스트...",
    "segments": [...],
    "detected_languages": ["ko", "en"],
    "confidence": 0.95
  },
  "analysis": {
    "document_type": "menu",
    "translation": "번역된 텍스트...",
    "summary": "요약...",
    "key_info": {
      "items": ["항목 1", "항목 2"],
      "prices": ["$10", "$15"]
    },
    "advice": "실용적 조언..."
  }
}
```

## 지원하는 문서 유형

- **메뉴**: 요리 번역, 알레르기 성분 감지, 가격 환산
- **계약서**: 법률 용어 설명, 주요 조항 강조, 위험 분석
- **영수증/청구서**: 항목 분류, 총액 검증, 지출 태깅
- **의료 문서**: 약물명 번역, 복용법 설명, 부작용 경고
- **표지판/안내문**: 긴급 정보 우선순위 지정, 방향 안내
- **교육 자료**: 콘텐츠 번역, 개념 설명, 참고 자료 제안

## 개발

### 백엔드 테스트

```bash
cd backend
pytest
```

### 프론트엔드 테스트

```bash
cd frontend
npm test
```

### 린팅

```bash
# 백엔드
cd backend
flake8 app/

# 프론트엔드
cd frontend
npm run lint
```

## 프로젝트 구조

```
ocrproject/
├── backend/              # Python FastAPI 백엔드
│   ├── app/
│   │   ├── api/          # API 라우트
│   │   ├── core/         # 설정 및 보안
│   │   ├── services/     # 비즈니스 로직 (OCR, LLM 등)
│   │   ├── models/       # 데이터베이스 모델 및 스키마
│   │   └── utils/        # 헬퍼 함수
│   ├── tests/            # 백엔드 테스트
│   └── requirements.txt
│
├── frontend/             # Next.js 프론트엔드
│   ├── src/
│   │   ├── app/          # Next.js 14 app router
│   │   ├── components/   # React 컴포넌트
│   │   ├── lib/          # API 클라이언트 및 유틸리티
│   │   ├── hooks/        # 커스텀 React hooks
│   │   └── types/        # TypeScript 타입
│   └── package.json
│
├── docker-compose.yml    # Docker Compose 설정
├── .env.example          # 환경 변수 템플릿
└── CLAUDE.md             # Claude Code 개발 가이드
```

## 성능

- **OCR 처리**: 이미지당 < 3초
- **LLM 분석**: < 5초
- **전체 응답 시간**: 종단간 < 8초
- **OCR 정확도**: 인쇄 문서 > 90%
- **이미지 크기 제한**: 10MB
- **지원 형식**: JPG, PNG, PDF

## 보안

- 저장된 이미지 암호화
- 24시간 후 임시 파일 자동 삭제
- 사용자 엔드포인트에 JWT 인증
- API 속도 제한
- GDPR 준수 데이터 처리

## 기여하기

1. 저장소 포크
2. 기능 브랜치 생성
3. 변경사항 작성
4. 테스트 실행
5. Pull request 제출

## 라이선스

MIT License - 자세한 내용은 LICENSE 파일 참조

## 지원

- 문서: `CLAUDE.md` 및 `MCP_SETUP_GUIDE.md` 참조
- 이슈: https://github.com/dddoing/ocrproject/issues
- API 문서: http://localhost:8000/api/docs

## 감사의 말

- EasyOCR - 다국어 OCR 지원
- Anthropic Claude - LLM 기능
- FastAPI - 백엔드 프레임워크
- Next.js - 프론트엔드 프레임워크
