PHQ9_BANDS = [
    (0,4,"Minimal"),
    (5,9,"Mild"),
    (10,14,"Moderate"),
    (15,19,"Moderately severe"),
    (20,27,"Severe"),
]

def score_phq9(answers: dict) -> dict:
    vals = [int(v) for v in answers.values()]
    score = sum(vals)
    band = "Unknown"
    for low,high,name in PHQ9_BANDS:
        if low <= score <= high:
            band = name
            break
    suicide_flag = any(int(v) >= 3 for v in answers.values())
    return {
        "score": score,
        "band": band,
        "suicide_flag": suicide_flag,
        "disclaimer": "This is not a clinical diagnosis. For emergencies contact professionals.",
        "diet_suggestions": ["balanced protein", "leafy vegetables", "regular meals"],
        "micro_actions": ["5-min breathing", "hydrate", "step outside"]
    }
