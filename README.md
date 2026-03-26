# 🎵 한국 음악 산업 주간 뉴스레터 자동화

매주 금요일 오후 4시, bluejeans.signup@gmail.com으로 자동 발송됩니다.

## ⚙️ 설정 방법 (5분 소요)

### 1️⃣ GitHub 저장소 만들기

1. https://github.com 접속 (계정 없으면 생성)
2. 우측 상단 `+` → `New repository`
3. Repository name: `music-newsletter` (아무거나 OK)
4. **Public** 선택
5. `Create repository` 클릭

---

### 2️⃣ 코드 업로드

**방법 A: 웹에서 직접 (추천)**

1. GitHub 저장소 페이지에서 `Add file` → `Upload files`
2. 아래 4개 파일 업로드:
   - `newsletter_generator.py`
   - `requirements.txt`
   - `.github/workflows/weekly.yml`
   - `README.md`

**방법 B: Git 명령어**
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/[당신username]/music-newsletter.git
git push -u origin main
```

---

### 3️⃣ Claude API 키 발급

1. https://console.anthropic.com 접속
2. 로그인 후 `API Keys` 메뉴
3. `Create Key` 클릭
4. 키 복사 (이 키는 다시 볼 수 없으니 꼭 저장!)

**참고:** 첫 $5 무료, 이후 사용량 과금

---

### 4️⃣ Gmail 앱 비밀번호 생성

1. https://myaccount.google.com/security 접속
2. **2단계 인증 켜기** (필수!)
   - 보안 → 2단계 인증 → 시작하기
3. 앱 비밀번호 생성:
   - 보안 → 2단계 인증 → 앱 비밀번호
   - 앱 선택: `메일`
   - 기기 선택: `기타` → "Newsletter Bot" 입력
   - 생성된 16자리 비밀번호 복사 (공백 제거)

---

### 5️⃣ GitHub Secrets 설정

1. GitHub 저장소 → `Settings` → `Secrets and variables` → `Actions`
2. `New repository secret` 클릭
3. 두 개 추가:

**Secret 1:**
- Name: `ANTHROPIC_API_KEY`
- Value: [3단계에서 복사한 Claude API 키]

**Secret 2:**
- Name: `GMAIL_APP_PASSWORD`
- Value: [4단계에서 생성한 Gmail 앱 비밀번호, 공백 제거]

---

### 6️⃣ 자동 실행 활성화

1. GitHub 저장소 → `Actions` 탭
2. `I understand my workflows, go ahead and enable them` 클릭
3. 왼쪽에서 `Weekly Music Newsletter` 선택
4. `Enable workflow` 클릭

---

## ✅ 테스트 실행

바로 테스트해보고 싶다면:

1. `Actions` 탭 → `Weekly Music Newsletter`
2. 우측 `Run workflow` → `Run workflow` 클릭
3. 1-2분 후 bluejeans.signup@gmail.com 확인!

---

## 📅 자동 실행 일정

- **매주 금요일 오후 4시** (한국 시간)
- PC 끄기 OK (GitHub이 클라우드에서 실행)
- 실패 시 이메일로 알림

---

## 🔧 문제 해결

### 뉴스레터가 안 와요
1. `Actions` 탭에서 실행 로그 확인
2. Secrets 값이 정확한지 확인
3. Gmail 앱 비밀번호 재생성

### 발송 시간 변경하고 싶어요
`.github/workflows/weekly.yml` 파일에서:
```yaml
- cron: '0 7 * * 5'  # 금요일 오후 4시
```
변경:
- `0 7` → 시간 (UTC 기준, 한국시간 -9시간)
- 마지막 `5` → 요일 (0=일요일, 1=월요일, ..., 5=금요일)

예: 매주 월요일 오전 9시 → `0 0 * * 1`

---

## 💰 비용

- **GitHub Actions:** 완전 무료
- **Claude API:** 
  - 첫 $5 무료
  - 뉴스레터 1회: 약 $0.30-0.50
  - 월 4회 = 월 $1.20-2.00

---

## 📞 도움이 필요하면

설정 중 막히면 `Actions` 탭의 에러 로그 캡쳐해서 문의하세요!

---

## 🎉 완료!

이제 매주 금요일 오후 4시, 자동으로 최신 음악 산업 뉴스가 메일로 옵니다! 🚀
