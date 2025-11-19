# MCP 서버 설정 가이드

이 가이드는 Universal Document Translator 프로젝트를 위한 세 가지 MCP 서버 설정을 도와줍니다.

## 사전 요구사항

- Node.js 18+ 설치
- Claude Code CLI 설치
- Docker 설치 (PostgreSQL용)
- 저장소 접근 권한이 있는 GitHub 계정

## 1단계: PostgreSQL 데이터베이스 설정

먼저 Docker를 사용하여 PostgreSQL 데이터베이스를 시작합니다:

```bash
# PostgreSQL 컨테이너 시작
docker run --name doc-translator-db \
  -e POSTGRES_USER=docuser \
  -e POSTGRES_PASSWORD=yourpassword \
  -e POSTGRES_DB=docdb \
  -p 5432:5432 \
  -d postgres:15

# 실행 중인지 확인
docker ps | grep doc-translator-db

# 선택사항: 연결 확인
docker exec -it doc-translator-db psql -U docuser -d docdb
# \q를 입력하여 종료
```

## 2단계: GitHub Personal Access Token 생성

1. GitHub 방문: https://github.com/settings/tokens
2. "Generate new token" → "Generate new token (classic)" 클릭
3. 이름 지정: "Universal Document Translator MCP"
4. 다음 범위 선택:
   - ✅ `repo` (비공개 저장소의 전체 제어)
   - ✅ `workflow` (GitHub Action 워크플로우 업데이트)
   - ✅ `read:user` (사용자 프로필 데이터 읽기)
5. "Generate token" 클릭
6. **토큰을 즉시 복사** (다시 볼 수 없습니다)

## 3단계: 환경 변수 설정

프로젝트 루트에 `.env` 파일 생성:

```bash
# 예제 파일 복사
cp .env.example .env

# 값으로 편집
nano .env  # 또는 선호하는 편집기 사용
```

`.env`에 자격 증명 추가:

```bash
# PostgreSQL 데이터베이스
DATABASE_URL=postgresql://docuser:yourpassword@localhost:5432/docdb

# GitHub 토큰
GITHUB_PERSONAL_ACCESS_TOKEN=ghp_your_actual_token_here

# Claude API (애플리케이션용)
ANTHROPIC_API_KEY=your_claude_api_key_here
```

그런 다음 셸로 내보내기:

```bash
# 환경 변수 로드
export $(cat .env | grep -v '^#' | xargs)

# 또는 macOS/Linux에서 셸 프로필에 추가 (~/.zshrc 또는 ~/.bashrc):
echo 'export GITHUB_PERSONAL_ACCESS_TOKEN=ghp_your_token' >> ~/.zshrc
echo 'export DATABASE_URL=postgresql://docuser:yourpassword@localhost:5432/docdb' >> ~/.zshrc
source ~/.zshrc
```

## 4단계: MCP 설정 확인

`.mcp.json` 파일이 이미 생성되었습니다. 존재하는지 확인:

```bash
cat .mcp.json
```

세 서버의 설정을 모두 확인할 수 있어야 합니다:
- ✅ GitHub MCP 서버
- ✅ Filesystem MCP 서버
- ✅ PostgreSQL MCP 서버

## 5단계: MCP 서버 테스트

환경 변수를 설정하면 Claude Code가 자동으로 MCP 서버를 사용합니다. 확인 방법:

```bash
# 설정된 모든 MCP 서버 나열
claude mcp list

# 특정 서버에 대한 세부 정보 얻기
claude mcp get github
claude mcp get filesystem
claude mcp get postgresql
```

## 6단계: Claude Code에서 확인

1. 프로젝트 디렉토리에서 Claude Code 열기
2. `/mcp` 입력하여 모든 MCP 서버 상태 보기
3. 세 서버가 모두 사용 가능으로 표시되어야 함

## MCP 서버 사용

### GitHub MCP 서버

이제 Claude Code에 다음을 요청할 수 있습니다:
- Pull request 생성
- 이슈 및 댓글 읽기
- 브랜치 관리
- 저장소 정보 보기

예시 명령:
```
"이 저장소의 모든 열린 이슈 보여줘"
"feature/ocr-service라는 새 브랜치 생성해"
"현재 변경사항으로 PR 생성해"
```

### Filesystem MCP 서버

향상된 파일 작업:
```
"백엔드 디렉토리의 모든 Python 파일 나열해"
"디렉토리 구조 보여줘"
"'OCR'을 포함하는 모든 파일 찾아"
```

### PostgreSQL MCP 서버

데이터베이스 쿼리 및 관리:
```
"데이터베이스의 모든 테이블 보여줘"
"사용자 히스토리 테이블 쿼리해"
"문서 테이블에 인덱스 생성해"
```

## 문제 해결

### MCP 서버가 표시되지 않음

1. 환경 변수가 설정되었는지 확인:
   ```bash
   echo $GITHUB_PERSONAL_ACCESS_TOKEN
   echo $DATABASE_URL
   ```

2. PostgreSQL이 실행 중인지 확인:
   ```bash
   docker ps | grep doc-translator-db
   ```

3. 데이터베이스 연결 테스트:
   ```bash
   psql $DATABASE_URL -c "SELECT version();"
   ```

### GitHub 토큰 문제

- 토큰에 올바른 범위가 있는지 확인 (`repo`, `workflow`, `read:user`)
- 토큰은 `ghp_`로 시작해야 함 (classic 토큰)
- 토큰이 만료되지 않았는지 확인

### PostgreSQL 연결 문제

- Docker 컨테이너가 실행 중인지 확인
- 포트 5432가 다른 프로세스에서 사용 중이지 않은지 확인:
  ```bash
  lsof -i :5432
  ```
- 직접 연결 시도:
  ```bash
  docker exec -it doc-translator-db psql -U docuser -d docdb
  ```

## 보안 참고사항

- ✅ `.env` 파일은 `.gitignore`에 있음 - 절대 커밋하지 마세요
- ✅ `.mcp.json`은 환경 변수 참조를 사용 - 커밋해도 안전
- ✅ 주기적으로 GitHub 토큰 교체
- ✅ 가능한 경우 읽기 전용 데이터베이스 자격 증명 사용

## 다음 단계

1. git 저장소 초기화 (아직 완료하지 않은 경우):
   ```bash
   git init
   ```

2. GitHub 저장소 생성 및 연결

3. 백엔드 및 프론트엔드 구축 시작:
   ```bash
   # CLAUDE.md의 설정 지침을 따르세요
   ```

4. 전체 MCP 기능으로 프로젝트 개발을 돕기 위해 Claude Code를 사용하세요!

## 추가 리소스

- [MCP 문서](https://code.claude.com/docs/en/mcp)
- [GitHub MCP 서버](https://github.com/modelcontextprotocol/servers/tree/main/src/github)
- [PostgreSQL MCP 서버](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres)
- [Filesystem MCP 서버](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)
