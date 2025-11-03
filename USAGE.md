# USAGE

cURL examples:

POST text analysis:
curl -X POST http://localhost:8000/analyze/text -H "Content-Type: application/json" -d '{"text":"Hello"}'

WebSocket example (send base64 frames):
# Use a websocket client to connect to ws://localhost:8000/ws/live/session123
