# EmoteX — Final Deploy Build (Generated 2025-11-03T15:52:40.128290Z)

This is the final cleaned package of **EmoteX**, ready for local development or deployment.

---

## ⚡ Quick Local Dev Setup (FastAPI + React)

1. Unzip and move into folder:
```bash
unzip EmoteX_Final_Deploy.zip
cd EmoteX_Final_Deploy
```

2. Setup backend:
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r backend/requirements.txt
cp .env.example .env
# edit .env with your configuration
```

3. Run backend server:
```bash
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

4. Setup frontend:
```bash
cd ../frontend
npm install
npm run dev
# opens on http://localhost:3000 or 5173
```

5. Open browser:
- Frontend → http://localhost:3000
- Backend docs → http://localhost:8000/docs

---

## 🐳 Docker / Docker-Compose (Recommended)

If you have `docker-compose.yml` in the repo:

```bash
cd EmoteX_Final_Deploy
docker-compose up --build
```
Useful commands:
```
docker-compose up -d --build   # run in background
docker-compose logs -f         # view logs
docker-compose down            # stop containers
```

Or build manually:
```
docker build -t emotex-backend ./backend
docker build -t emotex-frontend ./frontend
docker run -p 8000:8000 emotex-backend
docker run -p 3000:3000 emotex-frontend
```

---

## ☁️ Cloud Deployment (Render / Vercel / Heroku)

### Render (recommended for full stack)
1. Push this folder to GitHub:
```bash
git init
git add .
git commit -m "Initial EmoteX Deploy Build"
git branch -M main
git remote add origin https://github.com/YOUR_USER/emotex_final.git
git push -u origin main
```
2. On Render → “New Web Service” → connect this repo
3. Use `render.yaml` for configuration
4. Set environment variables from `.env.example`

### Vercel (frontend only)
Connect the `frontend` folder, and set API URL to point to your backend.

### Heroku
Either deploy two apps (frontend + backend) or use Docker container registry.

---

## ✅ Notes
- Secrets (API keys, tokens) go in `.env`, not committed to Git.
- Backend → FastAPI at port 8000
- Frontend → React dev server (3000 or 5173)
- Docker → unified stack

---

If you want, I can next:
- Add `setup.sh` for one-command local boot
- Add `run_docker.sh` for simplified Docker start
- Auto-generate `.env.example` template
