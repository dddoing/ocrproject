# CLAUDE.md

이 파일은 이 저장소의 코드 작업 시 Claude Code (claude.ai/code)를 위한 지침을 제공합니다.

## 프로젝트 개요

**Universal Document Translator** (다국어 문서 번역 & 해석기)는 OCR 텍스트 추출과 LLM 기반 번역 및 문맥 분석을 결합한 AI 기반 문서 분석 도구입니다. 이 시스템은 단순 번역을 넘어 다양한 문서 유형(메뉴, 표지판, 계약서, 영수증, 의료 문서 등)에 대한 문맥적 이해, 핵심 정보 추출 및 실용적인 조언을 제공합니다.

**대상 사용자**: 해외 여행자, 언어 학습자, 비즈니스 전문가 및 문서 번역 및 분석이 필요한 일반 사용자.

## 기술 스택

### 백엔드
- **언어**: Python 3.10+
- **프레임워크**: FastAPI
- **OCR 엔진**: EasyOCR (또는 Tesseract)
- **LLM**: Claude API (Anthropic) 또는 OpenAI GPT-4
- **이미지 처리**: OpenCV, Pillow

### 프론트엔드
- **프레임워크**: Next.js 14+ (TypeScript)
- **UI**: Tailwind CSS, shadcn/ui
- **상태 관리**: Zustand 또는 Redux Toolkit

### 인프라
- **데이터베이스**: PostgreSQL (사용자 데이터, 히스토리)
- **캐시**: Redis (세션, 번역 결과)
- **스토리지**: AWS S3 또는 Cloudinary (이미지)
- **배포**: Docker, AWS/GCP/Vercel

## 아키텍처

### 프로젝트 구조

```
universal-doc-translator/
├── backend/            # Python FastAPI 백엔드
│   ├── app/
│   │   ├── main.py                 # FastAPI 진입점
│   │   ├── api/
│   │   │   ├── routes.py           # API 엔드포인트
│   │   │   └── dependencies.py
│   │   ├── core/
│   │   │   ├── config.py           # 설정 관리
│   │   │   └── security.py         # 인증 & 보안
│   │   ├── services/
│   │   │   ├── ocr_service.py      # OCR 텍스트 추출
│   │   │   ├── llm_service.py      # LLM 분석 & 번역
│   │   │   ├── image_service.py    # 이미지 전처리
│   │   │   └── document_service.py # 문서 유형 분류
│   │   ├── models/
│   │   │   ├── database.py         # SQLAlchemy 모델
│   │   │   └── schemas.py          # Pydantic 스키마
│   │   └── utils/
│   ├── tests/
│   └── requirements.txt
│
└── frontend/           # Next.js 프론트엔드
    ├── src/
    │   ├── app/                    # Next.js 14 app router
    │   ├── components/
    │   │   ├── ImageUploader.tsx
    │   │   ├── ResultViewer.tsx
    │   │   ├── DocumentAnalysis.tsx
    │   │   └── HistoryList.tsx
    │   ├── lib/
    │   │   └── api.ts              # 백엔드 API 클라이언트
    │   ├── hooks/
    │   │   └── useDocumentAnalysis.ts
    │   └── types/
    └── package.json
```

### 핵심 처리 파이프라인

1. **이미지 업로드**: 사용자가 문서 이미지 업로드/캡처
2. **이미지 전처리** (`image_service.py`): 회전 보정, 노이즈 제거, 대비 향상
3. **OCR 추출** (`ocr_service.py`): 신뢰도 점수 및 바운딩 박스와 함께 다국어 텍스트 인식
4. **문서 분류** (`document_service.py`): 문서 유형 자동 감지 (메뉴, 계약서, 영수증 등)
5. **LLM 분석** (`llm_service.py`): 번역, 요약, 핵심 정보 추출, 문맥적 조언
6. **결과 표시**: 원본 텍스트, 번역, 핵심 정보 카드 및 권장사항이 포함된 구조화된 응답

### 주요 API 엔드포인트

**POST /api/analyze**
- 입력: 이미지 파일, 목표 언어, 문서 유형 (선택사항)
- 출력: OCR 결과, 번역, 문서 유형, 요약, 추출된 핵심 정보 (날짜, 금액, 이름), 문맥적 조언
- 성능 목표: 전체 < 8초 (OCR < 3초, LLM < 5초)

## 개발 명령어

### 백엔드 설정 및 개발

```bash
# 초기 설정
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# EasyOCR 모델 다운로드 (첫 실행 시 자동)
python -c "import easyocr; reader = easyocr.Reader(['ko', 'en'])"

# 개발 서버 실행
uvicorn app.main:app --reload --port 8000

# 테스트 실행
pytest

# Docker로 실행
docker build -t doc-translator-backend .
docker run -p 8000:8000 doc-translator-backend
```

### 프론트엔드 설정 및 개발

```bash
# 초기 설정
cd frontend
npm install

# 개발 서버 실행
npm run dev
# http://localhost:3000 접속

# 프로덕션 빌드
npm run build

# 프로덕션 빌드 실행
npm start

# 테스트 실행
npm test

# 타입 체킹
npm run type-check

# 린팅
npm run lint
```

### 환경 변수

다음 내용으로 `.env` 파일 생성:
```bash
# 필수
ANTHROPIC_API_KEY=your_claude_api_key
DATABASE_URL=postgresql://user:password@localhost:5432/docdb
REDIS_URL=redis://localhost:6379

# AWS (S3 사용 시)
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
AWS_S3_BUCKET=your_bucket_name

# 선택사항
OPENAI_API_KEY=your_openai_key  # GPT-4 사용 시
DEEPL_API_KEY=your_deepl_key    # 번역 품질 비교용

# MCP 서버 (Claude Code 통합용)
GITHUB_PERSONAL_ACCESS_TOKEN=ghp_your_token  # GitHub MCP 서버용
```

전체 템플릿은 `.env.example`을 참조하세요.

### MCP 서버 설정

이 프로젝트는 Model Context Protocol (MCP) 서버를 사용하여 Claude Code의 기능을 향상시킵니다:

**설정된 서버** (`.mcp.json` 참조):

1. **GitHub MCP 서버**: 저장소 관리, PR 생성, 이슈 추적 가능
   - 필요: `GITHUB_PERSONAL_ACCESS_TOKEN` 환경 변수
   - 토큰 생성: https://github.com/settings/tokens (범위: `repo`, `workflow`, `read:user`)

2. **Filesystem MCP 서버**: 프로젝트 디렉토리 내에서 파일 작업 제공
   - 액세스 제한: `/Users/yoo/study/alProject`
   - 추가 자격 증명 불필요

3. **PostgreSQL MCP 서버**: 데이터베이스 쿼리 및 관리
   - 애플리케이션과 동일한 `DATABASE_URL` 사용
   - 직접 데이터베이스 검사 및 쿼리 가능

**Docker로 PostgreSQL 설정**:
```bash
# PostgreSQL 컨테이너 시작
docker run --name doc-translator-db \
  -e POSTGRES_USER=docuser \
  -e POSTGRES_PASSWORD=yourpassword \
  -e POSTGRES_DB=docdb \
  -p 5432:5432 \
  -d postgres:15

# 환경 변수 설정
export DATABASE_URL="postgresql://docuser:yourpassword@localhost:5432/docdb"
```

**MCP 서버 관리**:
```bash
# 설정된 서버 나열
claude mcp list

# 서버 세부 정보 보기
claude mcp get github

# Claude Code에서 서버 상태 확인
/mcp
```

**MCP 서버가 가능하게 하는 것**:
- GitHub: PR 생성 자동화, 이슈 관리, 코드 리뷰 실행
- Filesystem: 향상된 파일 작업, 프로젝트 구조 분석
- PostgreSQL: 번역 히스토리 쿼리, 사용자 데이터 분석, 데이터베이스 스키마 관리

### Docker Compose (전체 스택)

```bash
# 모든 서비스 시작 (백엔드, 프론트엔드, PostgreSQL, Redis)
docker-compose up -d

# 로그 보기
docker-compose logs -f

# 모든 서비스 중지
docker-compose down
```

## 문서 유형별 특화

LLM 분석은 감지된 문서 유형에 따라 조정됩니다:

- **메뉴**: 설명이 포함된 요리 번역, 알레르기 성분 감지, 통화 환산, 추천
- **표지판/안내문**: 긴급 정보 우선순위 지정, 방향 안내, 경고 강조
- **계약서/법률 문서**: 전문 용어 설명, 주요 조항 강조, 위험 분석, 체크리스트 생성
- **영수증/청구서**: 항목 자동 분류, 총액/세금 검증, 지출 태깅
- **의료 문서**: 약물명 번역, 복용법 정리, 부작용 경고, 상담 질문 생성
- **교육 자료**: 번역 및 요약, 어려운 개념 설명, 참고 자료 제안

## 성능 요구사항

- **OCR 정확도**: 인쇄 문서 > 90%
- **번역 품질**: 원어민 수준 유창성
- **문서 분류**: > 85% 정확도
- **응답 시간**: 종단간 < 8초
- **이미지 크기 제한**: 10MB
- **지원 형식**: JPG, PNG, PDF
- **동시 사용자**: 100명 (초기 목표)

## 보안 고려사항

- 암호화하여 업로드된 이미지 저장
- 24시간 후 임시 파일 자동 삭제
- 사용자 인증에 JWT 사용
- API 속도 제한 구현
- API 키는 환경 변수에만 보관
- 모든 통신에 HTTPS 필수
- 사용자 데이터에 대한 GDPR 준수
- 의료/법률 조언 면책 조항 표시

## OCR 언어 지원

EasyOCR 지원: 한국어 (ko), 영어 (en), 일본어 (ja), 중국어 간체 (ch_sim), 중국어 번체 (ch_tra), 스페인어 (es), 프랑스어 (fr), 독일어 (de) 등. `ocr_service.py`에서 설정:

```python
reader = easyocr.Reader(['ko', 'en', 'ja', 'ch_sim'])  # 필요한 언어 추가
```

## LLM 통합 노트

### 프롬프트 엔지니어링 전략

`llm_service.py`는 다음을 위해 프롬프트를 구조화해야 합니다:
1. 감지된 언어와 함께 추출된 OCR 텍스트 제공
2. 목표 번역 언어 지정
3. 문서 유형 분류 요청
4. 구조화된 핵심 정보 추출 요청 (JSON 형식)
5. 문서 유형에 따른 문맥적 조언 요청

### 토큰 관리

- 평균 입력: 요청당 ~1,000 토큰
- 평균 출력: 요청당 ~500 토큰
- 예상 비용: 1,000 요청당 월 $15-30

## 테스트 전략

### 백엔드 테스트
- 각 서비스에 대한 단위 테스트 (OCR, LLM, 이미지 전처리)
- 전체 파이프라인에 대한 통합 테스트
- 다양한 문서 유형 및 언어로 테스트
- 이미지 품질 엣지 케이스 테스트 (흐림, 회전, 조명 불량)

### 프론트엔드 테스트
- 업로드 UI에 대한 컴포넌트 테스트
- API 호출에 대한 통합 테스트
- 전체 사용자 흐름에 대한 E2E 테스트

### 테스트 데이터
포괄적인 테스트를 위해 지원되는 모든 유형과 언어의 다양한 문서 샘플 수집

## 일반적인 개발 패턴

### 새 문서 유형 추가

1. `document_service.py` 분류 로직 업데이트
2. `llm_service.py`에 특화된 프롬프트 템플릿 추가
3. `models/schemas.py`에 구조화된 출력용 Pydantic 스키마 정의
4. 유형별 정보 표시를 위해 프론트엔드 `DocumentAnalysis.tsx` 컴포넌트 업데이트
5. 샘플 문서로 테스트 추가

### 새 언어 추가

1. EasyOCR Reader 초기화에 언어 코드 추가
2. `ocr_service.py`에서 언어 감지 로직 업데이트
3. 샘플 문서로 번역 품질 테스트
4. 프론트엔드 언어 선택 UI 업데이트

## MVP 개발 단계

**1단계 (4-6주)**: 기본 이미지 업로드, OCR 추출, 단순 번역, 결과 표시
**2단계 (4-6주)**: 문서 유형별 특화, 사용자 히스토리, 테이블 추출, PDF 지원
**3단계 (진행 중)**: 손글씨 인식, 실시간 카메라 모드, TTS, 모바일 앱, 오프라인 모드

## 알려진 제한사항

- OCR 정확도는 이미지 품질에 크게 의존
- 손글씨 인식은 인쇄 텍스트보다 정확도가 낮음
- 복잡한 레이아웃 (다단, 표)은 추가 처리 필요
- LLM 응답 시간은 프롬프트 길이에 비례
- 의료/법률 조언은 참고용이며 전문적인 지침이 아님

전체 프로젝트 요구사항 및 로드맵은 `PROJECT_SPEC.md`를 참조하세요.
