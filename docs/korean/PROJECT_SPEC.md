# 다국어 문서 번역 & 해석기 (Universal Document Translator)

## 프로젝트 개요

### 프로젝트 목적
모든 종류의 문서(메뉴판, 안내문, 계약서, 영수증 등)를 촬영하거나 업로드하면 OCR로 텍스트를 추출하고, LLM이 번역과 함께 문맥 이해, 핵심 정보 추출, 실용적 조언을 제공하는 AI 기반 문서 분석 도구

### 타겟 사용자
- 해외 여행자 (실시간 문서 번역 필요)
- 외국어 학습자 (교재 및 자료 번역)
- 비즈니스맨 (계약서, 법률 문서 분석)
- 일반 사용자 (일상 문서 관리 및 정리)

### 핵심 가치
- **단순 번역을 넘어선 이해**: 문맥과 문화적 배경 고려
- **즉시 실행 가능한 인사이트**: 핵심 정보 추출 및 조언 제공
- **다양한 문서 타입 지원**: 범용적 활용 가능

---

## 기능 요구사항

### 1. 핵심 기능 (MVP)

#### 1.1 이미지 업로드 및 처리
- [ ] 카메라로 직접 촬영
- [ ] 갤러리에서 이미지 선택
- [ ] 드래그 앤 드롭 업로드 (웹)
- [ ] 이미지 전처리 (회전 보정, 노이즈 제거, 대비 강화)

#### 1.2 OCR 텍스트 추출
- [ ] 다국어 텍스트 인식 (한국어, 영어, 일본어, 중국어, 스페인어, 프랑스어, 독일어)
- [ ] 자동 언어 감지
- [ ] 텍스트 영역 좌표 정보 추출
- [ ] 신뢰도(Confidence) 점수 제공

#### 1.3 LLM 기반 분석
- [ ] 목표 언어로 정확한 번역
- [ ] 문서 타입 자동 분류
- [ ] 핵심 내용 요약
- [ ] 중요 정보 구조화 추출 (날짜, 금액, 이름, 연락처 등)
- [ ] 문맥 기반 실용적 조언 생성

#### 1.4 결과 표시
- [ ] 원본 이미지와 추출된 텍스트 비교 뷰
- [ ] 번역 결과 표시
- [ ] 핵심 정보 카드 형태로 표시
- [ ] 조언 및 주의사항 하이라이트

### 2. 문서 타입별 특화 기능

#### 2.1 메뉴판
- [ ] 요리명 번역 + 상세 설명
- [ ] 알레르기 유발 성분 감지 및 경고
- [ ] 가격 통화 환산
- [ ] 추천 메뉴 제안

#### 2.2 안내문/표지판
- [ ] 긴급 정보 우선 표시
- [ ] 방향 안내 시각화
- [ ] 주의사항 강조

#### 2.3 계약서/법률 문서
- [ ] 전문 용어 쉬운 설명
- [ ] 핵심 조항 하이라이트
- [ ] 리스크 포인트 분석
- [ ] 체크리스트 자동 생성

#### 2.4 영수증/청구서
- [ ] 항목별 자동 분류
- [ ] 총액 및 세금 계산 검증
- [ ] 지출 카테고리 태깅
- [ ] 월별 통계 (추후 기능)

#### 2.5 의료 문서
- [ ] 약물명 번역 및 설명
- [ ] 복용법 정리
- [ ] 부작용 경고
- [ ] 의사 상담용 질문 리스트

#### 2.6 학습 자료
- [ ] 텍스트 번역 및 요약
- [ ] 어려운 개념 쉬운 설명
- [ ] 관련 참고자료 추천

### 3. 추가 기능 (Post-MVP)

#### 3.1 고급 OCR
- [ ] 테이블 구조 인식 및 데이터 추출
- [ ] 다단 레이아웃 분석
- [ ] 손글씨 인식
- [ ] PDF 다중 페이지 처리

#### 3.2 사용자 경험
- [ ] 오프라인 모드 (경량 OCR)
- [ ] 실시간 카메라 프리뷰 번역
- [ ] 음성 출력 (TTS)
- [ ] 번역 결과 편집 기능

#### 3.3 데이터 관리
- [ ] 번역 히스토리 저장
- [ ] 즐겨찾기 기능
- [ ] 다중 문서 배치 처리
- [ ] 결과 내보내기 (PDF, TXT, JSON)

#### 3.4 개인화
- [ ] 자주 사용하는 언어 쌍 설정
- [ ] 선호하는 번역 스타일
- [ ] 특정 용어 사용자 정의 사전

---

## 기술 요구사항

### 1. 기술 스택

#### 1.1 백엔드
```
언어: Python 3.10+
프레임워크: FastAPI
OCR 엔진: EasyOCR (또는 Tesseract)
LLM API: Claude API (Anthropic) 또는 OpenAI GPT-4
이미지 처리: OpenCV, Pillow
```

#### 1.2 프론트엔드
```
웹: Next.js 14+ (TypeScript)
모바일: React Native (선택사항)
UI 라이브러리: Tailwind CSS, shadcn/ui
상태 관리: Zustand 또는 Redux Toolkit
```

#### 1.3 인프라
```
데이터베이스: PostgreSQL (사용자 데이터, 히스토리)
캐시: Redis (세션, 번역 결과 캐싱)
스토리지: AWS S3 또는 Cloudinary (이미지 저장)
배포: Docker, AWS/GCP/Vercel
```

### 2. API 설계

#### 2.1 엔드포인트

**POST /api/analyze**
- 요청: 이미지 파일, 목표 언어, 문서 타입(선택)
- 응답: OCR 결과, 번역, 분석 정보

```json
{
  "ocr_result": {
    "full_text": "추출된 전체 텍스트",
    "segments": [
      {
        "text": "텍스트 조각",
        "bbox": [x1, y1, x2, y2],
        "confidence": 0.95
      }
    ],
    "detected_languages": ["en", "ko"]
  },
  "analysis": {
    "document_type": "menu",
    "translation": "번역된 텍스트",
    "summary": "핵심 요약",
    "key_info": {
      "items": ["항목1", "항목2"],
      "prices": ["10000원", "15000원"],
      "dates": [],
      "contacts": []
    },
    "advice": "실용적 조언 및 주의사항"
  },
  "metadata": {
    "processing_time": 2.5,
    "confidence_score": 0.92
  }
}
```

**GET /api/history**
- 사용자의 번역 히스토리 조회

**POST /api/feedback**
- 번역 품질 피드백 제출

#### 2.2 외부 API 통합
- Claude API (Anthropic)
- EasyOCR (로컬) 또는 Google Cloud Vision API
- (선택) DeepL API (번역 품질 비교용)

### 3. 성능 요구사항

#### 3.1 응답 시간
- OCR 처리: < 3초 (이미지당)
- LLM 분석: < 5초
- 전체 프로세스: < 8초

#### 3.2 정확도
- OCR 정확도: > 90% (일반 인쇄물 기준)
- 번역 품질: 원어민 수준 자연스러움
- 문서 타입 분류 정확도: > 85%

#### 3.3 확장성
- 동시 사용자: 100명 (초기)
- 이미지 크기 제한: 10MB
- 지원 파일 형식: JPG, PNG, PDF

### 4. 보안 요구사항

#### 4.1 데이터 보호
- [ ] 업로드된 이미지 암호화 저장
- [ ] 사용자 데이터 익명화
- [ ] HTTPS 통신 강제
- [ ] API 키 환경변수 관리

#### 4.2 개인정보 처리
- [ ] 사용자 동의 없이 데이터 보관하지 않음
- [ ] 임시 파일 자동 삭제 (24시간)
- [ ] GDPR 준수

#### 4.3 접근 제어
- [ ] 사용자 인증 (JWT)
- [ ] API 요청 Rate Limiting
- [ ] 비용 관리를 위한 사용량 제한

---

## 개발 로드맵

### Phase 1: MVP 개발 (4-6주)

#### Week 1-2: 백엔드 기초
- [ ] FastAPI 프로젝트 초기 설정
- [ ] EasyOCR 통합 및 테스트
- [ ] 이미지 전처리 파이프라인 구축
- [ ] Claude API 연동

#### Week 3-4: 프론트엔드 기초
- [ ] Next.js 프로젝트 초기 설정
- [ ] 이미지 업로드 UI 구현
- [ ] 결과 표시 페이지 구현
- [ ] API 연동

#### Week 5-6: 통합 및 테스트
- [ ] End-to-End 테스트
- [ ] 다양한 문서 타입 테스트
- [ ] 성능 최적화
- [ ] 버그 수정

### Phase 2: 기능 확장 (4-6주)

- [ ] 문서 타입별 특화 기능 구현
- [ ] 히스토리 및 사용자 관리
- [ ] 테이블 추출 기능
- [ ] PDF 다중 페이지 지원

### Phase 3: 고도화 (진행중)

- [ ] 손글씨 인식
- [ ] 실시간 번역 (카메라 모드)
- [ ] 음성 출력 (TTS)
- [ ] 모바일 앱 개발
- [ ] 오프라인 모드

---

## 프로젝트 구조

```
universal-doc-translator/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                 # FastAPI 앱
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py           # API 라우트
│   │   │   └── dependencies.py     # 의존성
│   │   ├── core/
│   │   │   ├── config.py           # 설정
│   │   │   └── security.py         # 인증/보안
│   │   ├── services/
│   │   │   ├── ocr_service.py      # OCR 처리
│   │   │   ├── llm_service.py      # LLM 분석
│   │   │   ├── image_service.py    # 이미지 전처리
│   │   │   └── document_service.py # 문서 분류
│   │   ├── models/
│   │   │   ├── database.py         # DB 모델
│   │   │   └── schemas.py          # Pydantic 스키마
│   │   └── utils/
│   │       ├── helpers.py
│   │       └── validators.py
│   ├── tests/
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   │   ├── page.tsx            # 메인 페이지
│   │   │   ├── layout.tsx
│   │   │   └── api/                # API 라우트
│   │   ├── components/
│   │   │   ├── ImageUploader.tsx
│   │   │   ├── ResultViewer.tsx
│   │   │   ├── DocumentAnalysis.tsx
│   │   │   └── HistoryList.tsx
│   │   ├── lib/
│   │   │   ├── api.ts              # API 클라이언트
│   │   │   └── utils.ts
│   │   ├── hooks/
│   │   │   └── useDocumentAnalysis.ts
│   │   └── types/
│   │       └── index.ts
│   ├── public/
│   ├── package.json
│   └── next.config.js
│
├── docker-compose.yml
├── .env.example
└── README.md
```

---

## 초기 설정 가이드

### 1. 환경 설정

#### 필수 도구 설치
```bash
# Python 3.10+
# Node.js 18+
# Docker (선택사항)
```

#### 백엔드 설정
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# EasyOCR 모델 다운로드 (첫 실행시 자동)
python -c "import easyocr; reader = easyocr.Reader(['ko', 'en'])"
```

#### 프론트엔드 설정
```bash
cd frontend
npm install
```

#### 환경 변수 설정
```bash
# .env 파일 생성
cp .env.example .env

# 필수 환경 변수
ANTHROPIC_API_KEY=your_claude_api_key
DATABASE_URL=postgresql://user:password@localhost:5432/docdb
REDIS_URL=redis://localhost:6379
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
```

### 2. 개발 서버 실행

#### 백엔드
```bash
cd backend
uvicorn app.main:app --reload --port 8000
```

#### 프론트엔드
```bash
cd frontend
npm run dev
```

접속: http://localhost:3000

### 3. 테스트

```bash
# 백엔드 테스트
cd backend
pytest

# 프론트엔드 테스트
cd frontend
npm test
```

---

## 예상 비용 및 리소스

### API 사용 비용 (월 추정)

#### Claude API
- 입력: 평균 1,000 토큰/요청
- 출력: 평균 500 토큰/요청
- 예상 사용량: 1,000 요청/월
- 비용: ~$15-30/월

#### 클라우드 호스팅
- AWS EC2 t3.medium: ~$30/월
- S3 스토리지: ~$5/월
- Redis Cache: ~$15/월
- 총: ~$50/월

#### OCR (EasyOCR 자체 호스팅)
- 무료 (로컬 처리)
- GPU 추천: NVIDIA T4 이상

### 개발 시간 추정
- MVP: 150-200 시간
- Phase 2: 100-150 시간
- Phase 3: 200+ 시간

---

## 주의사항 및 제약

### 1. 기술적 제약
- OCR 정확도는 이미지 품질에 크게 의존
- 손글씨 인식은 인쇄물보다 정확도 낮음
- 복잡한 레이아웃(다단, 표)은 추가 처리 필요
- LLM 응답 시간은 프롬프트 길이와 비례

### 2. 법률적 고려사항
- 의료/법률 조언은 참고용으로만 표시
- 면책 조항 명시 필수
- 사용자 데이터 처리 관련 개인정보보호법 준수

### 3. 윤리적 고려사항
- 저작권 있는 문서 처리 주의
- 민감한 정보 처리 시 사용자 동의 필요
- AI 번역의 한계 명시

---

## 성공 지표 (KPI)

### 정량적 지표
- [ ] 일일 활성 사용자 (DAU)
- [ ] 문서 처리 성공률 > 95%
- [ ] 평균 처리 시간 < 8초
- [ ] 사용자 재방문율 > 40%

### 정성적 지표
- [ ] 사용자 만족도 점수 > 4.0/5.0
- [ ] 번역 품질 피드백 긍정 비율 > 80%
- [ ] 기능 요청 및 개선 피드백 수집

---

## 다음 단계

1. **개발 환경 구축**: 로컬 개발 환경 설정 완료
2. **API 키 발급**: Anthropic Claude API 키 획득
3. **MVP 개발 시작**: 이미지 업로드 + OCR + 기본 번역 기능 구현
4. **테스트 데이터 준비**: 다양한 문서 샘플 수집
5. **프로토타입 테스트**: 실제 사용자 피드백 수집

---

## 참고 자료

### 기술 문서
- [FastAPI 공식 문서](https://fastapi.tiangolo.com/)
- [EasyOCR GitHub](https://github.com/JaidedAI/EasyOCR)
- [Anthropic Claude API 문서](https://docs.anthropic.com/)
- [Next.js 공식 문서](https://nextjs.org/docs)

### 유용한 라이브러리
- OpenCV: 이미지 전처리
- Pillow: 이미지 조작
- LangChain: LLM 체이닝
- Pydantic: 데이터 검증

---

**문서 작성일**: 2025-11-19
**버전**: 1.0
**작성자**: Project Team
