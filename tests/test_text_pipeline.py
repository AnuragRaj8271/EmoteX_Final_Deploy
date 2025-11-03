def test_text_demo():
    from backend.app.models.text_model import TextModel
    m = TextModel()
    r = m.analyze("hello")
    assert "sentiment" in r
