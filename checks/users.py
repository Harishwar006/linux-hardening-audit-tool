import subprocess
from core.auditor import finding

def run():
    results = []

    cmd = "awk -F: '($3 == 0) {print $1}' /etc/passwd"
    users = subprocess.getoutput(cmd).splitlines()

    if len(users) > 1:
        results.append(finding(
            "AUTH-001",
            "Multiple UID 0 users",
            "CRITICAL",
            "FAIL",
            f"UID 0 users found: {', '.join(users)}",
            "Ensure only root has UID 0"
        ))
    else:
        results.append(finding(
            "AUTH-001",
            "Multiple UID 0 users",
            "CRITICAL",
            "PASS",
            "Only root has UID 0",
            "No action required"
        ))

    return results
