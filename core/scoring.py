SEVERITY_SCORES = {
    "CRITICAL": 10,
    "HIGH": 7,
    "MEDIUM": 4,
    "LOW": 1,
    "INFO": 0
}

def calculate_score(findings):
    max_score = len(findings) * 10
    risk_score = 0

    for f in findings:
        if f["status"] == "FAIL":
            risk_score += SEVERITY_SCORES.get(f["severity"], 0)

    hardening_score = max(0, 100 - int((risk_score / max_score) * 100))
    return hardening_score, risk_score, max_score
