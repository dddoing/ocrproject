# Universal Document Translator - 완전 가이드

**초급부터 전문가까지: OCR 및 AI 문서 번역 이해하기**

---

## 목차

1. [초등학생용 (8-12세)](#초등학생용-8-12세)
2. [중고등학생용 (13-18세)](#중고등학생용-13-18세)
3. [대학생 및 초보자용](#대학생-및-초보자용)
4. [개발자용](#개발자용)
5. [전문가 및 고급 사용자용](#전문가-및-고급-사용자용)

---

## 초등학생용 (8-12세)

### 이 프로젝트는 무엇인가요?

한국에서 휴가를 보내는데 한국어로 작성된 메뉴판을 본다고 상상해보세요. 음식이 무엇인지 모르겠죠! 이 프로젝트는 다음과 같은 **마법의 카메라**와 같습니다:

1. 📸 메뉴판 사진 촬영
2. 👀 모든 한국어 단어 읽기 (컴퓨터인데도!)
3. 🗣️ 모든 것을 영어로 번역
4. 💡 각 요리가 무엇인지 알려주고 선택을 도와줌!

### 어떻게 작동하나요?

3단계 게임처럼 생각하세요:

**1단계: 사진 찍기**
- 컴퓨터에서 웹사이트 열기
- 큰 업로드 버튼 클릭
- 글자가 있는 종이(메뉴, 표지판, 메모 등) 사진 찍기

**2단계: 마법의 컴퓨터 읽기**
- 컴퓨터가 사진을 봄
- 모든 단어를 찾음 (이것을 "OCR"이라고 함 - 로봇 눈 같은 것!)
- 단어가 어떤 언어인지 알아냄

**3단계: 번역 받기**
- 컴퓨터가 AI를 사용 (매우 똑똑한 로봇 두뇌처럼)
- 모든 단어를 영어로 번역
- 가격, 날짜, 경고 같은 중요한 정보를 알려줌

### 할 수 있는 멋진 일들

- 메뉴를 읽고 음식이 무엇인지 알려줌
- 여행할 때 거리 표지판 번역
- 약병을 읽고 사용법 알려줌
- 영수증을 구매 목록으로 변환
- 다른 언어로 된 숙제 설명

### 직접 해보기!

1. 컴퓨터에서 `http://localhost:3000` 접속
2. 텍스트가 있는 사진을 웹사이트에 드래그
3. "문서 분석" 클릭
4. 몇 초 기다림
5. 번역과 설명 보기!

**예시:**
- 일본 메뉴 사진 업로드
- 목표 언어로 "영어" 선택
- 결과: "라멘 - 돼지고기, 계란, 야채가 들어간 국수 수프"

---

## 중고등학생용 (13-18세)

### 프로젝트 개요

다음을 결합한 **AI 기반 문서 분석 시스템**입니다:
- **컴퓨터 비전** (컴퓨터가 이미지를 "보는" 방법)
- **광학 문자 인식** (OCR - 이미지에서 텍스트 추출)
- **자연어 처리** (텍스트 이해 및 번역)
- **기계 학습** (시간이 지남에 따라 똑똑해지는 AI)

### 배울 수 있는 것

이 프로젝트를 이해하면 다음을 배울 수 있습니다:
1. **이미지 처리** - 컴퓨터가 사진을 분석하는 방법
2. **패턴 인식** - AI가 이미지에서 텍스트를 찾는 방법
3. **언어 번역** - 컴퓨터가 다른 언어를 이해하는 방법
4. **웹 개발** - 웹사이트와 앱이 작동하는 방법
5. **데이터베이스** - 정보가 저장되고 검색되는 방법

### 작동 원리 (기술 개요)

```
이미지 → 이미지 처리 → 텍스트 감지 → 텍스트 인식 →
AI 분석 → 번역 → 구조화된 결과
```

**단계별 프로세스:**

1. **업로드 단계**
   - 이미지 업로드 (JPG, PNG 또는 PDF)
   - 서버가 파일을 받고 검증
   - 이미지가 임시 저장됨

2. **전처리**
   - 컴퓨터가 밝기와 대비 조정
   - 노이즈와 흐림 제거
   - 회전된 텍스트 정렬
   - OCR을 위해 이미지 준비

3. **OCR (텍스트 추출)**
   - AI가 이미지를 픽셀 단위로 스캔
   - 텍스트처럼 보이는 영역 찾기
   - 개별 문자 인식
   - 문자를 단어로 결합
   - 존재하는 언어 감지

4. **AI 분석**
   - Claude AI에 텍스트 전송 (ChatGPT와 유사)
   - AI가 맥락과 의미 이해
   - 문서 유형 분류 (메뉴, 영수증, 계약서 등)
   - 중요 정보 추출 (날짜, 가격, 이름)
   - 번역 및 조언 생성

5. **결과 표시**
   - 신뢰도 점수와 함께 원본 텍스트 표시
   - 전체 번역 표시
   - 핵심 정보 강조
   - 문맥적 조언 제공

### 사용된 기술

- **백엔드**: Python (프로그래밍 언어) + FastAPI (웹 프레임워크)
- **프론트엔드**: React (사용자 인터페이스) + Next.js (웹 프레임워크)
- **OCR**: EasyOCR (텍스트 인식 라이브러리)
- **AI**: Claude API (언어 모델)
- **데이터베이스**: PostgreSQL (데이터 저장)
- **스타일링**: Tailwind CSS (디자인)

### 프로젝트 실행

**사전 요구사항:**
- Python 3.10+ 설치
- Node.js 18+ 설치
- Anthropic에서 Claude API 키 받기

**빠른 시작:**
```bash
# 1. 프로젝트 클론
git clone https://github.com/dddoing/ocrproject.git
cd ocrproject

# 2. 환경 설정
echo "ANTHROPIC_API_KEY=your_key" > .env

# 3. Docker로 실행
docker-compose up
```

**수동 설정:**
```bash
# 백엔드
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

# 프론트엔드 (새 터미널)
cd frontend
npm install
npm run dev
```

### 실제 적용 사례

1. **여행**: 표지판, 메뉴, 티켓 번역
2. **비즈니스**: 계약서, 청구서, 영수증 분석
3. **교육**: 학습 자료, 연구 논문 번역
4. **의료**: 처방전, 의료 지침 읽기
5. **쇼핑**: 제품 라벨, 가격 이해

---

## 대학생 및 초보자용

### 기술 아키텍처

**마이크로서비스 지향 아키텍처**를 사용한 **풀스택 웹 애플리케이션**을 구현합니다:

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│   Frontend  │────▶│   Backend    │────▶│  Database   │
│  (Next.js)  │     │  (FastAPI)   │     │ (PostgreSQL)│
└─────────────┘     └──────────────┘     └─────────────┘
                           │
                           ├──▶ OCR Service (EasyOCR)
                           ├──▶ LLM Service (Claude API)
                           ├──▶ Image Processing (OpenCV)
                           └──▶ Cache (Redis)
```

### 시스템 구성 요소

#### 1. **프론트엔드 레이어** (Next.js + React + TypeScript)

**목적**: 문서 업로드 및 결과 확인을 위한 사용자 인터페이스

**주요 컴포넌트:**
- `ImageUploader`: 드래그 앤 드롭으로 파일 업로드 처리
- `ResultViewer`: OCR 추출 결과 표시
- `DocumentAnalysis`: 번역 및 인사이트 표시
- `HistoryList`: 과거 분석 기록 표시

**기술 스택:**
- **Next.js 14**: 서버 사이드 렌더링을 지원하는 React 프레임워크
- **TypeScript**: 타입 안전 JavaScript
- **Tailwind CSS**: 유틸리티 우선 CSS 프레임워크
- **Axios**: API 호출을 위한 HTTP 클라이언트

**파일 구조:**
```
frontend/src/
├── app/              # Next.js App Router
│   ├── page.tsx      # 메인 페이지
│   └── layout.tsx    # 루트 레이아웃
├── components/       # React 컴포넌트
├── lib/              # 유틸리티
│   └── api.ts        # API 클라이언트
├── types/            # TypeScript 정의
└── hooks/            # 커스텀 React hooks
```

#### 2. **백엔드 레이어** (Python + FastAPI)

**목적**: 비즈니스 로직, OCR 처리 및 AI 분석

**아키텍처:**
```
app/
├── main.py              # 애플리케이션 진입점
├── api/
│   ├── routes.py        # API 엔드포인트
│   └── dependencies.py  # 의존성 주입
├── core/
│   ├── config.py        # 설정 관리
│   └── security.py      # 인증 & JWT
├── services/
│   ├── ocr_service.py      # 텍스트 추출
│   ├── llm_service.py      # AI 분석
│   ├── image_service.py    # 전처리
│   └── document_service.py # 분류
├── models/
│   ├── database.py      # SQLAlchemy ORM 모델
│   └── schemas.py       # Pydantic 검증
└── utils/
    ├── helpers.py       # 유틸리티 함수
    └── validators.py    # 입력 검증
```

**주요 엔드포인트:**

| 엔드포인트 | 메서드 | 목적 |
|----------|--------|------|
| `/api/analyze` | POST | 문서 이미지 분석 |
| `/api/history` | GET | 사용자 히스토리 조회 |
| `/api/feedback` | POST | 사용자 피드백 제출 |
| `/health` | GET | 헬스 체크 |

#### 3. **OCR 서비스** (EasyOCR)

**목적**: 딥러닝을 사용하여 이미지에서 텍스트 추출

**작동 방식:**
1. **모델 로딩**: 문자 인식을 위한 사전 훈련된 신경망
2. **텍스트 감지**: CRAFT 알고리즘이 텍스트 영역 찾기
3. **텍스트 인식**: CRNN 모델이 문자 인식
4. **언어 감지**: 문자 패턴을 기반으로 언어 식별

**지원 언어:**
- 한국어 (ko)
- 영어 (en)
- 일본어 (ja)
- 중국어 간체 (ch_sim)
- 스페인어 (es)
- 프랑스어 (fr)
- 독일어 (de)

**코드 예시:**
```python
class OCRService:
    def __init__(self):
        self.reader = easyocr.Reader(['ko', 'en'], gpu=False)

    async def extract_text(self, image: np.ndarray) -> Dict:
        results = self.reader.readtext(image)

        segments = []
        for bbox, text, confidence in results:
            segments.append({
                "text": text,
                "bbox": bbox,
                "confidence": float(confidence)
            })

        return {
            "full_text": " ".join([s["text"] for s in segments]),
            "segments": segments,
            "detected_languages": self._detect_languages(full_text),
            "confidence": average_confidence
        }
```

#### 4. **이미지 전처리** (OpenCV)

**목적**: OCR 정확도 향상을 위한 이미지 품질 개선

**기법:**
1. **노이즈 제거**: Non-local means를 사용한 이미지 노이즈 제거
2. **그레이스케일 변환**: 색상 복잡성 단순화
3. **적응형 임계값**: 텍스트 대비 개선
4. **기울기 보정**: Hough 변환을 사용한 회전 보정

**코드 예시:**
```python
def _enhance_image(self, image: np.ndarray) -> np.ndarray:
    # 노이즈 제거
    denoised = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)

    # 그레이스케일
    gray = cv2.cvtColor(denoised, cv2.COLOR_BGR2GRAY)

    # 적응형 임계값
    thresh = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 11, 2
    )

    # 기울기 보정
    return self._deskew(thresh)
```

#### 5. **LLM 서비스** (Claude API)

**목적**: 맥락 이해 및 번역 생성

**Claude API 통합:**
```python
class LLMService:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)

    async def analyze(self, text: str, target_language: str,
                     document_type: str) -> Dict:
        prompt = self._build_prompt(text, target_language, document_type)

        message = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1500,
            messages=[{"role": "user", "content": prompt}]
        )

        return self._parse_response(message.content[0].text)
```

**프롬프트 엔지니어링 전략:**
- 맥락과 함께 추출된 OCR 텍스트 제공
- 목표 언어 및 문서 유형 지정
- 구조화된 JSON 출력 요청
- 요약, 핵심 정보 및 조언 요청
- 문서 유형별 특정 지침 포함

#### 6. **데이터베이스 레이어** (PostgreSQL)

**스키마 설계:**

```sql
-- 사용자 테이블
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR UNIQUE NOT NULL,
    hashed_password VARCHAR NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

-- 문서 테이블
CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    document_type VARCHAR,
    source_language VARCHAR,
    target_language VARCHAR,
    original_text TEXT,
    translated_text TEXT,
    key_info JSONB,
    confidence_score FLOAT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- 피드백 테이블
CREATE TABLE feedback (
    id SERIAL PRIMARY KEY,
    document_id INTEGER REFERENCES documents(id),
    user_id INTEGER REFERENCES users(id),
    rating INTEGER CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
```

### 데이터 흐름

**완전한 요청 생명주기:**

```
1. 사용자가 이미지 업로드
   └─▶ 프론트엔드가 파일 검증 (타입, 크기)

2. 프론트엔드가 POST 요청 전송
   └─▶ file, target_language, document_type을 포함한 FormData

3. 백엔드가 요청 수신
   ├─▶ 인증 검증 (JWT)
   ├─▶ 파일 형식 검증
   └─▶ 임시 저장소에 저장

4. 이미지 전처리
   ├─▶ 메모리에 이미지 로드
   ├─▶ 노이즈 제거 필터 적용
   ├─▶ 최적 형식으로 변환
   └─▶ 회전/기울기 보정

5. OCR 처리
   ├─▶ EasyOCR 모델 로드
   ├─▶ 텍스트 영역 감지
   ├─▶ 문자 인식
   ├─▶ 신뢰도 점수 계산
   └─▶ 언어 감지

6. 문서 분류
   └─▶ 키워드 및 패턴 분석

7. LLM 분석
   ├─▶ 맥락 인식 프롬프트 구축
   ├─▶ Claude API에 전송
   ├─▶ 구조화된 응답 수신
   └─▶ 파싱 및 검증

8. 응답 컴파일
   ├─▶ OCR + LLM 결과 결합
   ├─▶ 메타데이터 추가 (타이밍, 신뢰도)
   └─▶ JSON으로 포맷

9. 데이터베이스 저장 (비동기)
   └─▶ 문서 레코드 저장

10. 프론트엔드에 응답 전송
    └─▶ 프론트엔드가 결과 렌더링
```

### 성능 최적화

**캐싱 전략 (Redis):**
```python
# 동일한 이미지에 대한 OCR 결과 캐싱
cache_key = f"ocr:{image_hash}"
if cached := redis.get(cache_key):
    return json.loads(cached)

result = ocr_service.extract_text(image)
redis.setex(cache_key, 3600, json.dumps(result))  # 1시간 TTL
```

**비동기 처리:**
```python
# 비차단 데이터베이스 저장
async def save_document(doc_data: dict):
    async with db.session() as session:
        document = Document(**doc_data)
        session.add(document)
        await session.commit()

# Fire and forget
asyncio.create_task(save_document(data))
```

### 테스트 전략

**백엔드 테스트 (pytest):**
```python
def test_ocr_extraction(test_image):
    service = OCRService()
    result = await service.extract_text(test_image)

    assert result["full_text"]
    assert len(result["segments"]) > 0
    assert result["confidence"] > 0.8

def test_api_analyze_endpoint(client, test_image_file):
    response = client.post(
        "/api/analyze",
        files={"file": test_image_file},
        data={"target_language": "en"}
    )

    assert response.status_code == 200
    assert "ocr_result" in response.json()
    assert "analysis" in response.json()
```

**프론트엔드 테스트 (Jest + React Testing Library):**
```typescript
test('ImageUploader가 파일 업로드를 수락함', async () => {
  render(<ImageUploader onAnalysisComplete={jest.fn()} />)

  const file = new File(['image'], 'test.jpg', { type: 'image/jpeg' })
  const input = screen.getByLabelText(/upload/i)

  await userEvent.upload(input, file)

  expect(screen.getByText('test.jpg')).toBeInTheDocument()
})
```

### 배포

**Docker Compose 설정:**
```yaml
services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=${DATABASE_URL}
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
    depends_on:
      - postgres
      - redis

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    depends_on:
      - backend
```

**프로덕션 고려사항:**
- 관리형 데이터베이스 사용 (AWS RDS, Google Cloud SQL)
- 정적 자산용 CDN 구현 (CloudFront, Cloudflare)
- 로드 밸런싱 추가 (nginx, AWS ALB)
- SSL/TLS 인증서 활성화
- 모니터링 설정 (Prometheus, Grafana)
- 로깅 구현 (ELK 스택)

---

## 개발자용

### 개발 워크플로우

#### 로컬 개발 설정

**1. 클론 및 환경 설정:**
```bash
# 저장소 클론
git clone https://github.com/dddoing/ocrproject.git
cd ocrproject

# 템플릿에서 .env 생성
cp .env.example .env

# API 키 추가
echo "ANTHROPIC_API_KEY=sk-ant-your-key" >> .env
```

**2. 백엔드 개발:**
```bash
cd backend

# 가상 환경 생성
python3.10 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt

# 개발 의존성 설치
pip install pytest pytest-cov black flake8 mypy

# 마이그레이션 실행 (구현 시)
alembic upgrade head

# 핫 리로드로 개발 서버 시작
uvicorn app.main:app --reload --port 8000 --log-level debug
```

**3. 프론트엔드 개발:**
```bash
cd frontend

# 의존성 설치
npm install

# 개발 의존성 설치 (package.json에 없는 경우)
npm install --save-dev @types/jest jest

# 개발 서버 시작
npm run dev

# 별도 터미널에서: 타입 에러 감시
npm run type-check -- --watch
```

**4. 데이터베이스 설정:**
```bash
# PostgreSQL 시작
docker run --name dev-postgres \
  -e POSTGRES_USER=devuser \
  -e POSTGRES_PASSWORD=devpass \
  -e POSTGRES_DB=devdb \
  -p 5432:5432 \
  -d postgres:15

# Redis 시작
docker run --name dev-redis \
  -p 6379:6379 \
  -d redis:7-alpine

# 연결 확인
psql postgresql://devuser:devpass@localhost:5432/devdb -c "SELECT version();"
redis-cli ping
```

### 코드 스타일 및 표준

**Python (백엔드):**
```bash
# 코드 포맷
black app/ tests/

# 린트
flake8 app/ tests/ --max-line-length=100

# 타입 체킹
mypy app/

# 모든 체크 실행
black app/ && flake8 app/ && mypy app/ && pytest
```

**설정 파일:**

`.flake8`:
```ini
[flake8]
max-line-length = 100
exclude = venv,.git,__pycache__
ignore = E203,W503
```

`pyproject.toml` (Black용):
```toml
[tool.black]
line-length = 100
target-version = ['py310']
```

**TypeScript/React (프론트엔드):**
```bash
# 린트
npm run lint

# 포맷 (Prettier 사용 시)
npm run format

# 타입 체크
npm run type-check
```

### 새로운 기능 추가

#### 예시: 새로운 문서 유형 "Invoice" 추가

**1. Document Service 업데이트 (백엔드):**

`backend/app/services/document_service.py`:
```python
async def classify(self, text: str, segments: List[Dict]) -> str:
    text_lower = text.lower()

    # 청구서 키워드 추가
    invoice_keywords = [
        'invoice', 'bill to', 'invoice number', 'due date',
        'amount due', 'subtotal', 'net amount'
    ]
    if any(keyword in text_lower for keyword in invoice_keywords):
        return "invoice"

    # ... 기존 코드 ...
```

**2. Invoice 특정 프롬프트로 LLM Service 업데이트:**

`backend/app/services/llm_service.py`:
```python
def _get_type_specific_instructions(self, document_type: str) -> str:
    instructions = {
        # ... 기존 타입 ...
        "invoice": """
        - 청구서 번호, 날짜, 만기일 추출
        - 수량과 가격을 포함한 모든 항목 나열
        - 소계, 세금, 총액 계산 검증
        - 지불 조건 및 방법 식별
        - 연체 또는 비정상적인 요금 표시
        """,
    }
    return instructions.get(document_type, "")
```

**3. TypeScript 타입 추가 (프론트엔드):**

`frontend/src/types/index.ts`:
```typescript
export type DocumentType =
  | 'menu'
  | 'contract'
  | 'receipt'
  | 'invoice'  // 새 타입
  | 'medical'
  | 'sign'
  | 'general';

export interface InvoiceInfo extends KeyInfo {
  invoice_number?: string;
  due_date?: string;
  payment_terms?: string;
  line_items?: Array<{
    description: string;
    quantity: number;
    unit_price: string;
    total: string;
  }>;
}
```

**4. Invoice 특정 컴포넌트 생성:**

`frontend/src/components/InvoiceAnalysis.tsx`:
```typescript
export default function InvoiceAnalysis({ analysis }: { analysis: Analysis }) {
  const invoiceInfo = analysis.key_info as InvoiceInfo;

  return (
    <div className="bg-white rounded-lg p-6">
      <h3 className="text-xl font-bold mb-4">청구서 상세 정보</h3>

      <div className="grid grid-cols-2 gap-4">
        <InfoItem label="청구서 번호" value={invoiceInfo.invoice_number} />
        <InfoItem label="만기일" value={invoiceInfo.due_date} />
        <InfoItem label="지불 조건" value={invoiceInfo.payment_terms} />
      </div>

      <LineItemsTable items={invoiceInfo.line_items} />

      {analysis.advice && (
        <Alert type="warning">{analysis.advice}</Alert>
      )}
    </div>
  );
}
```

**5. DocumentAnalysis 컴포넌트 업데이트:**

`frontend/src/components/DocumentAnalysis.tsx`:
```typescript
import InvoiceAnalysis from './InvoiceAnalysis';

export default function DocumentAnalysis({ analysis }: DocumentAnalysisProps) {
  // 문서 유형별 컴포넌트 렌더링
  if (analysis.document_type === 'invoice') {
    return <InvoiceAnalysis analysis={analysis} />;
  }

  // ... 기존 코드 ...
}
```

**6. 테스트 추가:**

`backend/tests/test_invoice.py`:
```python
def test_invoice_classification():
    service = DocumentService()
    text = "INVOICE #12345\nBill To: John Doe\nAmount Due: $500"

    result = await service.classify(text, [])

    assert result == "invoice"

def test_invoice_analysis():
    service = LLMService()
    text = "청구서 상세 정보..."

    result = await service.analyze(text, "en", "invoice", [])

    assert "invoice_number" in result["key_info"]
    assert "due_date" in result["key_info"]
```

`frontend/src/components/__tests__/InvoiceAnalysis.test.tsx`:
```typescript
test('청구서 상세 정보 렌더링', () => {
  const mockAnalysis = {
    document_type: 'invoice',
    key_info: {
      invoice_number: 'INV-12345',
      due_date: '2025-12-31'
    }
  };

  render(<InvoiceAnalysis analysis={mockAnalysis} />);

  expect(screen.getByText('INV-12345')).toBeInTheDocument();
  expect(screen.getByText('2025-12-31')).toBeInTheDocument();
});
```

### 디버깅 가이드

**백엔드 디버깅:**

1. **디버그 로깅 활성화:**
```python
# app/main.py
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
logger.debug("디버그 메시지")
```

2. **FastAPI 디버그 모드 사용:**
```bash
uvicorn app.main:app --reload --log-level debug
```

3. **대화형 디버깅 (pdb):**
```python
# 중단점 추가
import pdb; pdb.set_trace()

# 또는 Python 3.7+에서 breakpoint() 사용
breakpoint()
```

4. **개별 서비스 테스트:**
```python
# OCR을 독립적으로 테스트
from app.services.ocr_service import OCRService
import cv2

service = OCRService()
image = cv2.imread("test_image.jpg")
result = await service.extract_text(image)
print(result)
```

**프론트엔드 디버깅:**

1. **React Developer Tools:**
   - 브라우저 확장 프로그램 설치
   - 컴포넌트 계층 구조 검사
   - props 및 state 확인

2. **콘솔 디버깅:**
```typescript
// 디버그 로그 추가
console.log('분석 결과:', analysisResult);

// debugger 문 사용
debugger;

// API 호출 로깅
axios.interceptors.request.use(request => {
  console.log('요청 시작', request)
  return request
})
```

3. **네트워크 탭:**
   - API 요청/응답 모니터링
   - 페이로드 및 헤더 확인
   - 응답 상태 코드 검증

**Docker 디버깅:**

```bash
# 로그 보기
docker-compose logs -f backend
docker-compose logs -f frontend

# 컨테이너 셸 접근
docker-compose exec backend bash
docker-compose exec frontend sh

# 컨테이너 상태 확인
docker-compose ps

# 특정 서비스 재시작
docker-compose restart backend
```

### 보안 모범 사례

**1. API 키 관리:**
```python
# API 키를 하드코딩하지 마세요
# ❌ 나쁨
ANTHROPIC_API_KEY = "sk-ant-api03-..."

# ✅ 좋음
from app.core.config import settings
api_key = settings.ANTHROPIC_API_KEY
```

**2. 입력 검증:**
```python
# 파일 업로드 검증
from app.utils.validators import validate_file_extension, validate_file_size

if not validate_file_extension(file.filename):
    raise HTTPException(400, "유효하지 않은 파일 타입")

if not validate_file_size(len(await file.read())):
    raise HTTPException(400, "파일이 너무 큼")
```

**3. SQL 인젝션 방지:**
```python
# ORM (SQLAlchemy) 사용 - 자동으로 SQL 인젝션 방지
# ✅ 좋음
users = session.query(User).filter(User.email == email).all()

# ❌ 나쁨 - 절대 이렇게 하지 마세요
query = f"SELECT * FROM users WHERE email = '{email}'"
```

**4. XSS 방지:**
```typescript
// React는 자동으로 콘텐츠를 이스케이프
// ✅ 안전
<p>{userInput}</p>

// ❌ 위험 - 신뢰할 수 있는 콘텐츠에만 사용
<div dangerouslySetInnerHTML={{__html: userInput}} />
```

**5. 속도 제한:**
```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

@app.post("/api/analyze")
@limiter.limit("10/minute")
async def analyze(request: Request):
    # ...
```

### 모니터링 및 로깅

**애플리케이션 모니터링:**

```python
# app/main.py
from prometheus_client import Counter, Histogram
import time

# 메트릭
request_count = Counter('app_requests_total', '총 요청 수')
request_duration = Histogram('app_request_duration_seconds', '요청 지속 시간')

@app.middleware("http")
async def monitor_requests(request: Request, call_next):
    request_count.inc()

    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time

    request_duration.observe(duration)

    return response
```

**구조화된 로깅:**

```python
import structlog

logger = structlog.get_logger()

logger.info(
    "document_analyzed",
    document_type=doc_type,
    confidence=confidence,
    processing_time=duration,
    user_id=user_id
)
```

### CI/CD 파이프라인

**GitHub Actions 예시:**

`.github/workflows/ci.yml`:
```yaml
name: CI/CD Pipeline

on: [push, pull_request]

jobs:
  backend-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Python 설정
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'

      - name: 의존성 설치
        run: |
          cd backend
          pip install -r requirements.txt
          pip install pytest pytest-cov

      - name: 테스트 실행
        run: |
          cd backend
          pytest --cov=app tests/

      - name: 린트
        run: |
          cd backend
          flake8 app/

  frontend-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Node.js 설정
        uses: actions/setup-node@v2
        with:
          node-version: '18'

      - name: 의존성 설치
        run: |
          cd frontend
          npm ci

      - name: 타입 체크
        run: |
          cd frontend
          npm run type-check

      - name: 린트
        run: |
          cd frontend
          npm run lint

      - name: 테스트 실행
        run: |
          cd frontend
          npm test

  deploy:
    needs: [backend-tests, frontend-tests]
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - name: 프로덕션 배포
        run: |
          # 배포 스크립트
          echo "프로덕션 배포 중..."
```

---

## 전문가 및 고급 사용자용

### 심층 기술 분석

#### OCR 아키텍처 심층 분석

**EasyOCR 파이프라인:**

1. **텍스트 감지 (CRAFT - Character Region Awareness For Text detection)**
   ```python
   # CRAFT는 다음을 예측하는 컨볼루션 신경망 사용:
   # - 문자 영역 점수 (히트맵)
   # - 친화도 점수 (문자 연결)

   # 아키텍처:
   VGG-16 Backbone → Feature Pyramid Network →
   Skip Connections → Final Conv Layer →
   Region Score Map + Affinity Score Map

   # 후처리:
   # 1. 문자 그룹화를 위한 Watershed 알고리즘
   # 2. 연결 요소 분석
   # 3. 바운딩 박스 생성
   ```

2. **텍스트 인식 (CRNN - Convolutional Recurrent Neural Network)**
   ```python
   # 아키텍처:
   Convolutional Layers (특징 추출) →
   Recurrent Layers (시퀀스 모델링을 위한 LSTM/GRU) →
   Transcription Layer (CTC - Connectionist Temporal Classification)

   # CTC는 정렬이 필요 없는 훈련 가능:
   # - 가변 길이 시퀀스 처리
   # - 문자 수준 주석 불필요
   # - 가장 가능성 높은 문자 시퀀스 출력
   ```

**커스텀 OCR 최적화:**

```python
class OptimizedOCRService:
    def __init__(self):
        # GPU 가속 사용
        self.reader = easyocr.Reader(
            ['ko', 'en'],
            gpu=True,
            model_storage_directory='/models',
            download_enabled=False  # 사전 다운로드 모델
        )

        # 커스텀 인식 네트워크
        self.reader.setModelLanguage(
            'ko',
            '/models/custom_korean_model.pth'
        )

    async def extract_text_batch(self, images: List[np.ndarray]) -> List[Dict]:
        """효율성을 위한 배치 처리"""
        # 다중 처리를 사용한 병렬 처리
        with multiprocessing.Pool(processes=4) as pool:
            results = pool.map(self._process_single, images)
        return results

    def _apply_advanced_preprocessing(self, image: np.ndarray) -> np.ndarray:
        """고급 전처리 기법"""
        # 1. 색상 공간 정규화
        lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
        l = clahe.apply(l)
        enhanced = cv2.merge([l,a,b])
        enhanced = cv2.cvtColor(enhanced, cv2.COLOR_LAB2BGR)

        # 2. 형태학적 연산
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
        morph = cv2.morphologyEx(enhanced, cv2.MORPH_CLOSE, kernel)

        # 3. 그림자 제거
        dilated = cv2.dilate(morph, kernel, iterations=1)
        median = cv2.medianBlur(dilated, 21)
        diff = 255 - cv2.absdiff(morph, median)

        # 4. Otsu를 사용한 이진화
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        return binary
```

#### LLM 통합 최적화

**고급 프롬프트 엔지니어링:**

```python
class AdvancedLLMService:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)

        # Few-shot 예시가 있는 프롬프트 템플릿
        self.templates = {
            "menu": self._load_template("menu_template.json"),
            "contract": self._load_template("contract_template.json"),
            # ...
        }

    async def analyze_with_chain_of_thought(
        self,
        text: str,
        target_language: str,
        document_type: str
    ) -> Dict:
        """복잡한 분석을 위한 사고의 연쇄 프롬프팅 사용"""

        # 1단계: 문서 이해
        understanding_prompt = f"""
        먼저, 이 {document_type} 문서를 분석하세요:
        {text}

        단계별로 생각하세요:
        1. 이 문서의 주요 목적은 무엇인가?
        2. 대상 독자는 누구인가?
        3. 주요 섹션은 무엇인가?
        4. 애매하거나 불명확한 부분이 있는가?

        분석을 제공하세요:
        """

        understanding = await self._call_claude(understanding_prompt)

        # 2단계: 맥락을 고려한 번역
        translation_prompt = f"""
        이해를 바탕으로:
        {understanding}

        이제 문서를 {target_language}로 번역하세요. 고려사항:
        - 문화적 맥락과 관용구
        - 전문 용어
        - 어조 및 격식 수준
        - 대상 독자 기대

        번역:
        """

        translation = await self._call_claude(translation_prompt)

        # 3단계: 핵심 정보 추출
        extraction_prompt = f"""
        번역된 문서에서:
        {translation}

        JSON 형식으로 구조화된 정보 추출:
        {{
            "document_metadata": {{...}},
            "key_entities": {{...}},
            "important_dates": [...],
            "financial_info": {{...}},
            "action_items": [...]
        }}
        """

        key_info = await self._call_claude(extraction_prompt)

        # 4단계: 문맥적 조언
        advice_prompt = f"""
        이 {document_type}를 고려하여:
        - 번역: {translation}
        - 핵심 정보: {key_info}

        이 문서 유형에 특정한 실행 가능한 조언을 제공하세요.
        고려사항: 일반적인 함정, 문화적 고려사항, 법적 영향.
        """

        advice = await self._call_claude(advice_prompt)

        return {
            "understanding": understanding,
            "translation": translation,
            "key_info": json.loads(key_info),
            "advice": advice
        }

    async def _call_claude(self, prompt: str, cache: bool = True) -> str:
        """일반적인 프롬프트를 위한 캐싱과 함께 Claude 호출"""

        if cache:
            cache_key = hashlib.md5(prompt.encode()).hexdigest()
            if cached := await self.redis.get(cache_key):
                return cached

        response = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=2000,
            temperature=0.7,  # 작업에 따라 조정
            system="당신은 전문 다국어 문서 분석가입니다.",
            messages=[{"role": "user", "content": prompt}]
        )

        result = response.content[0].text

        if cache:
            await self.redis.setex(cache_key, 3600, result)

        return result
```

**실시간 UX를 위한 스트리밍 응답:**

```python
@app.post("/api/analyze-stream")
async def analyze_stream(file: UploadFile):
    async def generate():
        # OCR 단계
        yield json.dumps({"phase": "ocr", "status": "processing"}) + "\n"
        ocr_result = await ocr_service.extract_text(image)
        yield json.dumps({"phase": "ocr", "status": "complete", "data": ocr_result}) + "\n"

        # 번역 단계
        yield json.dumps({"phase": "translation", "status": "processing"}) + "\n"

        # 토큰별 번역 스트리밍
        async with client.messages.stream(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1500,
            messages=[{"role": "user", "content": prompt}]
        ) as stream:
            async for text in stream.text_stream:
                yield json.dumps({"phase": "translation", "token": text}) + "\n"

        # 최종 분석
        yield json.dumps({"phase": "complete", "data": final_result}) + "\n"

    return StreamingResponse(generate(), media_type="application/x-ndjson")
```

#### 데이터베이스 최적화

**고급 쿼리 최적화:**

```python
# SQLAlchemy 쿼리 최적화 사용
from sqlalchemy.orm import selectinload, joinedload

# N+1 쿼리 방지를 위한 Eager loading
documents = session.query(Document).options(
    selectinload(Document.user),
    selectinload(Document.feedback)
).filter(
    Document.created_at >= datetime.now() - timedelta(days=30)
).all()

# 성능을 위한 인덱스 쿼리
# 자주 쿼리되는 열에 인덱스 추가
class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, index=True)  # 인덱스됨
    document_type = Column(String, index=True)  # 인덱스됨
    created_at = Column(DateTime, index=True)  # 시간 기반 쿼리용 인덱스

    # 일반적인 쿼리 패턴을 위한 복합 인덱스
    __table_args__ = (
        Index('idx_user_date', 'user_id', 'created_at'),
    )

# 데이터베이스 수준 전체 텍스트 검색 사용
from sqlalchemy.dialects.postgresql import TSVECTOR

class Document(Base):
    # ... 기존 열 ...

    search_vector = Column(TSVECTOR)  # PostgreSQL 전체 텍스트 검색

    __table_args__ = (
        Index(
            'idx_search_vector',
            'search_vector',
            postgresql_using='gin'
        ),
    )

# 문서 검색
results = session.query(Document).filter(
    Document.search_vector.match('contract legal terms')
).all()
```

**연결 풀링:**

```python
# 데이터베이스 연결 최적화
from sqlalchemy.pool import QueuePool

engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=20,  # 최대 연결
    max_overflow=40,  # 허용되는 추가 연결
    pool_pre_ping=True,  # 사용 전 연결 확인
    pool_recycle=3600,  # 매시간 연결 재활용
    echo=False  # 프로덕션에서 SQL 로깅 비활성화
)
```

#### 확장성 아키텍처

**마이크로서비스 분해:**

```
┌─────────────────┐
│   API Gateway   │ (Kong, AWS API Gateway)
└────────┬────────┘
         │
    ┌────┴─────┬──────────┬───────────┐
    │          │          │           │
┌───▼────┐ ┌──▼────┐ ┌───▼─────┐ ┌──▼────────┐
│  Auth  │ │  OCR  │ │   LLM   │ │ Document  │
│Service │ │Service│ │ Service │ │  Service  │
└────────┘ └───────┘ └─────────┘ └───────────┘
    │          │          │            │
    └──────────┴──────────┴────────────┘
                    │
              ┌─────▼─────┐
              │  Message  │ (RabbitMQ, Kafka)
              │   Queue   │
              └───────────┘
```

**비동기 작업 큐 (Celery):**

```python
# tasks.py
from celery import Celery

celery_app = Celery(
    'ocr_tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/1'
)

@celery_app.task(bind=True, max_retries=3)
def process_document_async(self, image_path: str, user_id: int):
    try:
        # 장시간 실행 OCR 프로세스
        image = cv2.imread(image_path)
        ocr_result = ocr_service.extract_text(image)

        # LLM 분석
        analysis = llm_service.analyze(ocr_result['full_text'])

        # 데이터베이스에 저장
        save_document(user_id, ocr_result, analysis)

        # WebSocket을 통해 사용자에게 알림
        notify_user(user_id, {"status": "complete", "result": analysis})

    except Exception as exc:
        # 지수 백오프 재시도
        raise self.retry(exc=exc, countdown=2 ** self.request.retries)

# API 엔드포인트
@app.post("/api/analyze-async")
async def analyze_async(file: UploadFile, user_id: int):
    # 파일 저장
    file_path = await save_upload(file)

    # 작업 대기열
    task = process_document_async.delay(file_path, user_id)

    return {"task_id": task.id, "status": "queued"}
```

**Kubernetes를 사용한 로드 밸런싱:**

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ocr-backend
spec:
  replicas: 5
  selector:
    matchLabels:
      app: ocr-backend
  template:
    metadata:
      labels:
        app: ocr-backend
    spec:
      containers:
      - name: backend
        image: ocrproject/backend:latest
        resources:
          requests:
            memory: "512Mi"
            cpu: "500m"
          limits:
            memory: "2Gi"
            cpu: "2000m"
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: url
---
apiVersion: v1
kind: Service
metadata:
  name: ocr-backend-service
spec:
  type: LoadBalancer
  selector:
    app: ocr-backend
  ports:
  - port: 80
    targetPort: 8000
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: ocr-backend-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: ocr-backend
  minReplicas: 3
  maxReplicas: 20
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

#### 성능 벤치마킹

**Locust를 사용한 부하 테스트:**

```python
# locustfile.py
from locust import HttpUser, task, between
import random

class DocumentAnalysisUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def analyze_document(self):
        files = {'file': open('test_images/sample.jpg', 'rb')}
        data = {'target_language': 'en'}

        with self.client.post(
            "/api/analyze",
            files=files,
            data=data,
            catch_response=True
        ) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"상태 {response.status_code}로 실패")

    @task(1)
    def get_history(self):
        self.client.get("/api/history")

# 실행: locust -f locustfile.py --host=http://localhost:8000
```

**성능 메트릭:**

```python
from prometheus_client import Counter, Histogram, Gauge

# 메트릭 정의
ocr_processing_time = Histogram(
    'ocr_processing_seconds',
    'OCR 처리에 소요된 시간',
    buckets=[0.5, 1.0, 2.0, 3.0, 5.0, 10.0]
)

llm_api_calls = Counter(
    'llm_api_calls_total',
    '총 LLM API 호출',
    ['model', 'status']
)

active_analyses = Gauge(
    'active_analyses',
    '현재 분석 중인 문서 수'
)

# 코드 계측
@ocr_processing_time.time()
async def extract_text(image):
    active_analyses.inc()
    try:
        result = await ocr_service.extract_text(image)
        return result
    finally:
        active_analyses.dec()

# LLM 호출 추적
try:
    response = await llm_service.analyze(text)
    llm_api_calls.labels(model='claude-3.5', status='success').inc()
except Exception:
    llm_api_calls.labels(model='claude-3.5', status='error').inc()
    raise
```

#### 고급 보안

**OAuth2 구현:**

```python
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from datetime import datetime, timedelta

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire, "sub": data["user_id"]})

    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
    return encoded_jwt

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="유효하지 않은 자격 증명")

    access_token = create_access_token(
        data={"user_id": user.id, "scopes": form_data.scopes}
    )

    return {"access_token": access_token, "token_type": "bearer"}

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401)
    except JWTError:
        raise HTTPException(status_code=401)

    user = get_user(user_id)
    if user is None:
        raise HTTPException(status_code=401)

    return user
```

**Redis를 사용한 API 속도 제한:**

```python
from fastapi import HTTPException
import time

class RateLimiter:
    def __init__(self, redis_client, requests: int, window: int):
        self.redis = redis_client
        self.requests = requests
        self.window = window

    async def check_rate_limit(self, user_id: str):
        key = f"rate_limit:{user_id}"
        current = await self.redis.get(key)

        if current is None:
            # 첫 요청
            await self.redis.setex(key, self.window, 1)
            return True

        if int(current) >= self.requests:
            raise HTTPException(
                status_code=429,
                detail=f"속도 제한 초과. {self.window}초 후에 다시 시도하세요."
            )

        await self.redis.incr(key)
        return True

rate_limiter = RateLimiter(redis_client, requests=100, window=60)

@app.post("/api/analyze")
async def analyze(user: User = Depends(get_current_user)):
    await rate_limiter.check_rate_limit(user.id)
    # ... 요청 처리
```

#### 비용 최적화

**LLM API 비용 관리:**

```python
class CostOptimizedLLMService:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)
        self.cache = RedisCache()

        # 비용 추적
        self.cost_tracker = {
            'input_tokens': 0,
            'output_tokens': 0,
            'total_cost': 0.0
        }

    async def analyze(self, text: str, target_language: str) -> Dict:
        # 1. 먼저 캐시 확인
        cache_key = f"{hash(text)}:{target_language}"
        if cached := await self.cache.get(cache_key):
            return cached

        # 2. 프롬프트 압축 사용
        compressed_prompt = self._compress_prompt(text)

        # 3. 복잡도에 따라 모델 조정
        model = self._select_model(text)

        # 4. API 호출
        response = self.client.messages.create(
            model=model,
            max_tokens=self._calculate_max_tokens(text),
            messages=[{"role": "user", "content": compressed_prompt}]
        )

        # 5. 사용량 추적
        self._track_usage(response.usage)

        # 6. 결과 캐싱
        await self.cache.setex(cache_key, 3600, response)

        return response

    def _select_model(self, text: str) -> str:
        """작업 복잡도에 따라 모델 선택"""
        word_count = len(text.split())

        if word_count < 100:
            return "claude-3-haiku-20240307"  # 더 저렴하고 빠름
        elif word_count < 500:
            return "claude-3-5-sonnet-20241022"  # 균형잡힌
        else:
            return "claude-3-5-sonnet-20241022"  # 최고 품질

    def _compress_prompt(self, text: str) -> str:
        """중복 정보 제거"""
        # 과도한 공백 제거
        compressed = ' '.join(text.split())

        # 너무 길면 추출적 요약 사용
        if len(compressed) > 10000:
            # 처음과 마지막 단락 유지, 중간 요약
            sentences = sent_tokenize(compressed)
            if len(sentences) > 20:
                return ' '.join(sentences[:5] + ['...'] + sentences[-5:])

        return compressed

    def _track_usage(self, usage):
        """토큰 사용량 및 예상 비용 추적"""
        # Claude 가격 (예시)
        INPUT_COST_PER_1K = 0.003
        OUTPUT_COST_PER_1K = 0.015

        input_cost = (usage.input_tokens / 1000) * INPUT_COST_PER_1K
        output_cost = (usage.output_tokens / 1000) * OUTPUT_COST_PER_1K

        self.cost_tracker['input_tokens'] += usage.input_tokens
        self.cost_tracker['output_tokens'] += usage.output_tokens
        self.cost_tracker['total_cost'] += input_cost + output_cost

        # 비용이 임계값을 초과하면 알림
        if self.cost_tracker['total_cost'] > 100:  # $100
            send_alert("LLM 비용이 $100를 초과했습니다")
```

### 분석 및 인사이트

**커스텀 분석 대시보드:**

```python
# analytics.py
from sqlalchemy import func, and_
from datetime import datetime, timedelta

class AnalyticsService:
    def __init__(self, db_session):
        self.db = db_session

    async def get_usage_stats(self, days: int = 30) -> Dict:
        """종합적인 사용 통계 얻기"""
        start_date = datetime.now() - timedelta(days=days)

        # 문서 처리 통계
        total_docs = await self.db.query(func.count(Document.id))\
            .filter(Document.created_at >= start_date)\
            .scalar()

        # 문서 유형별
        by_type = await self.db.query(
            Document.document_type,
            func.count(Document.id)
        ).filter(
            Document.created_at >= start_date
        ).group_by(Document.document_type).all()

        # 언어 쌍
        language_pairs = await self.db.query(
            Document.source_language,
            Document.target_language,
            func.count(Document.id)
        ).filter(
            Document.created_at >= start_date
        ).group_by(
            Document.source_language,
            Document.target_language
        ).all()

        # 평균 신뢰도 점수
        avg_confidence = await self.db.query(
            func.avg(Document.confidence_score)
        ).filter(
            Document.created_at >= start_date
        ).scalar()

        # 사용자 참여도
        active_users = await self.db.query(
            func.count(func.distinct(Document.user_id))
        ).filter(
            Document.created_at >= start_date
        ).scalar()

        # 피크 사용 시간
        hourly_usage = await self.db.query(
            func.extract('hour', Document.created_at).label('hour'),
            func.count(Document.id)
        ).filter(
            Document.created_at >= start_date
        ).group_by('hour').all()

        return {
            "total_documents": total_docs,
            "by_document_type": dict(by_type),
            "language_pairs": [
                {"from": src, "to": tgt, "count": cnt}
                for src, tgt, cnt in language_pairs
            ],
            "average_confidence": float(avg_confidence or 0),
            "active_users": active_users,
            "hourly_distribution": dict(hourly_usage)
        }
```

---

## 결론

이 가이드는 Universal Document Translator 프로젝트의 기본 이해부터 전문가 수준의 구현 세부사항까지 다루었습니다. 여러분이:

- **학생**으로 OCR 및 AI에 대해 배우는 경우
- **개발자**로 유사한 애플리케이션을 구축하는 경우
- **전문가**로 프로덕션 시스템을 최적화하는 경우

이 프로젝트는 최첨단 AI 통합을 사용한 현대 풀스택 개발을 보여줍니다.

### 핵심 요점

1. **OCR 기술**: 컴퓨터가 이미지에서 텍스트를 추출하는 방법 이해
2. **LLM 통합**: 번역 및 분석을 위한 AI 활용
3. **풀스택 개발**: 확장 가능한 웹 애플리케이션 구축
4. **모범 사례**: 보안, 성능 및 코드 품질
5. **프로덕션 준비**: 배포, 모니터링 및 유지보수

### 다음 단계

- https://github.com/dddoing/ocrproject 에서 코드베이스 탐색
- 자신만의 기능 구축 시도
- 프로젝트에 기여
- 프로덕션에 배포

**즐거운 코딩 되세요!**
