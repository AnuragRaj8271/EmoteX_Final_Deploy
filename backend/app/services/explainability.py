def grad_cam(frame, model):
    return frame

def shap_text(text, model):
    return [{'token':t,'importance':0.01} for t in text.split()[:40]]
