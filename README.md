# EmoteX Mega Full (Demo)

This repository is a demo scaffold for "EmoteX Mega Full" integrating multimodal analysis, mental health screening,
real-time webcam analytics, ASR, summarization, fake-review detection, explainability, and deployment templates.

**Important:** This is a demo implementation. The mental health module is *not* a clinical tool.
**Disclaimer:** This is not a clinical diagnosis. For emergencies contact professionals.

## Quickstart (docker-compose)
1. Install Docker & Docker Compose.
2. Build and run:
   docker-compose build
   docker-compose up
3. Backend: http://localhost:8000

## Models
A small demo model bundle is included under `backend_models_bundle/`. For full weights, set `HF_MODEL_REPO` and use the admin endpoint to trigger downloads.

## Endpoints
See USAGE.md for cURL examples.
