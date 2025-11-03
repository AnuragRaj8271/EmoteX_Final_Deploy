from backend.app.services.mental_health import score_phq9

def test_phq9_minimal():
    answers = {f"q{i}": 0 for i in range(1,10)}
    r = score_phq9(answers)
    assert r["score"] == 0
    assert r["band"].lower().startswith("minimal")
