# 🎵 한국 음악 산업 주간 뉴스레터 자동화 (Gemini AI)

매주 금요일 오후 4시, bluejeans.signup@gmail.com으로 자동 발송됩니다.

**🆓 완전 무료!** Google Gemini API (월 1,500회 무료)

---

## ⚙️ 설정 방법 (5분 소요)

### 1️⃣ GitHub 저장소 파일 업데이트

GitHub 저장소에서 **기존 파일 3개를 교체**하세요:

1. `newsletter_generator.py` → **삭제 후 새 파일 업로드**
2. `requirements.txt` → **삭제 후 새 파일 업로드**
3. `.github/workflows/weekly.yml` → **삭제 후 새 파일 업로드**

**삭제 방법:**
- 파일 클릭 → 우측 상단 쓰레기통 아이콘 → Commit changes

**업로드 방법:**
- Add file → Upload files → 새 파일 드래그

---

### 2️⃣ Google AI Studio에서 API 키 발급

1. https://aistudio.google.com/app/apikey 접속
2. Google 계정으로 로그인
3. **"Create API key"** 클릭
4. **"Create API key in new project"** 선택
5. 생성된 키 복사 (예: `AIzaSy...`)

**⚠️ 중요:** 이 키는 다시 볼 수 없으니 꼭 복사해서 저장!

**무료 한도:**
- **월 1,500회 무료** (평생!)
- 1회 = 뉴스레터 1통
- **→ 매주 발송해도 평생 무료!** 🎉

---

### 3️⃣ Gmail 앱 비밀번호 생성

1. https://myaccount.google.com/security 접속
2. **2단계 인증 켜기** (필수!)
   - 보안 → 2단계 인증 → 시작하기
3. 앱 비밀번호 생성:
   - 보안 → 2단계 인증 → 앱 비밀번호
   - 앱 선택: `메일`
   - 기기 선택: `기타` → "Newsletter Bot" 입력
   - 생성된 16자리 비밀번호 복사 (공백 제거)

---

### 4️⃣ GitHub Secrets 설정

1. GitHub 저장소 → `Settings` → `Secrets and variables` → `Actions`
2. `New repository secret` 클릭
3. 두 개 추가:

**Secret 1:**
- Name: `GEMINI_API_KEY`
- Value: [2단계에서 복사한 Gemini API 키]

**Secret 2:**
- Name: `GMAIL_APP_PASSWORD`
- Value: [3단계에서 생성한 Gmail 앱 비밀번호, 공백 제거]

---

### 5️⃣ 자동 실행 활성화

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
- **Gemini API:** 
  - 월 1,500회 무료 (평생!)
  - 매주 발송 = 월 4회
  - **→ 영원히 무료!** 🎉
- **Gmail:** 완전 무료

---

## 🆚 Claude vs Gemini 비교

|  | Claude API | Gemini API |
|---|---|---|
| **무료 한도** | $5 크레딧 (약 10-15회) | 월 1,500회 (평생) |
| **웹 검색** | ✅ 지원 | ✅ Google Search 통합 |
| **품질** | 매우 우수 | 우수 |
| **비용** | $5 이후 유료 | 계속 무료 |

**→ Gemini 추천!** 평생 무료로 쓸 수 있어요! 🚀

---

## 📞 도움이 필요하면

설정 중 막히면 `Actions` 탭의 에러 로그 캡쳐해서 문의하세요!

---

## 🎉 완료!

이제 매주 금요일 오후 4시, 자동으로 최신 음악 산업 뉴스가 메일로 옵니다!

**완전 무료, 영원히!** 🎊
