"""
FastAPI main app entrypoint -- lightweight demo scaffold.
Implements routes and websocket skeletons as required by the spec.
"""
from fastapi import FastAPI, WebSocket, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from .core.config import settings

app = FastAPI(title="EmoteX Mega Full (demo)", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/metrics")
async def metrics():
    return {"metrics": "prometheus_metrics_placeholder"}

@app.post("/analyze/text")
async def analyze_text(payload: dict):
    text = payload.get("text", "")
    return {
        "text": text,
        "sentiment": "neutral",
        "emotion_probs": {"happy": 0.1, "sad": 0.1, "neutral": 0.8},
        "fake_review_score": 0.05,
        "summary": text[:200]
    }

@app.post("/summarize")
async def summarize(payload: dict):
    text = payload.get("text", "")
    return {"summary": text[:300], "method": "demo-chunked-bart"}

@app.post("/detect_fake_review")
async def detect_fake(payload: dict):
    review = payload.get("text", "")
    return {"fraud_prob": 0.07, "explanation": "demo heuristics"}

@app.post("/analyze/voice")
async def analyze_voice(file: UploadFile = File(...)):
    return {"transcript": "demo transcript", "emotion": "neutral", "confidence": 0.9}

@app.get("/replay/{session_id}")
async def get_replay(session_id: str):
    return {"session_id": session_id, "timeline": [], "media_urls": []}

@app.post("/mental/questionnaire")
async def mental_questionnaire(payload: dict):
    phq9 = payload.get("phq9", {})
    score = sum(int(v) for v in phq9.values()) if isinstance(phq9, dict) else 0
    suicide_flag = any(int(v)>=3 for v in phq9.values())
    return {
        "phq9_score": score,
        "band": "moderate" if 10 <= score < 15 else "minimal",
        "suicide_flag": bool(suicide_flag),
        "disclaimer": "This is not a clinical diagnosis. For emergencies contact professionals.",
        "suggested_diet": ["leafy greens", "omega-3 rich fish", "nuts"],
        "micro_actions": ["5-min breathing", "walk 10 mins"]
    }

@app.post("/assistant/query")
async def assistant_query(payload: dict):
    q = payload.get("query", "")
    return {"response": f"assistant fallback response to: {q}"}

@app.websocket("/ws/live/{session_id}")
async def websocket_live(websocket: WebSocket, session_id: str):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_json({
                "session_id": session_id,
                "emotion_probs": {"happy": 0.2, "neutral": 0.7, "sad": 0.1},
                "engagement_score": 0.65
            })
    except Exception:
        await websocket.close()
