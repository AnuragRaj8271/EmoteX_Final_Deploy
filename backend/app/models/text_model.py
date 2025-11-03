class TextModel:
    def analyze(self, text):
        return {'sentiment':'neutral','summary':text[:200],'fake_score':0.05}
