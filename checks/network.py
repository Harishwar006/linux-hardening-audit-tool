import subprocess
from core.auditor import finding

def run():
    results = []

    output = subprocess.getoutput("ss -tuln | grep LISTEN")

    if output:
        results.append(finding(
            "NET-001",
            "Open listening ports",
            "MEDIUM",
            "INFO",
            "Listening ports detected",
            "Review and disable unnecessary services"
        ))
    else:
        results.append(finding(
            "NET-001",
            "Open listening ports",
            "MEDIUM",
            "PASS",
            "No open ports found",
            "No action required"
        ))

    return results
