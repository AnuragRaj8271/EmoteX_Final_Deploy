class EnsembleModel:
    def __init__(self, smoothing_window=5):
        self.smoothing_window = smoothing_window
        self.history = []
    def combine(self, modalities):
        weighted = {}
        total_w = 0.0
        for name, v in modalities.items():
            w = v.get("conf", 0.5)
            total_w += w
            weighted[name] = v.get("score", 0.0) * w
        if total_w == 0:
            return 0.0
        return sum(weighted.values()) / total_w
