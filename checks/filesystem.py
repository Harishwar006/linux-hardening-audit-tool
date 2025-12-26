import subprocess
from core.auditor import finding

def run():
    results = []

    perm = subprocess.getoutput("stat -c %a /etc/shadow")

    if perm not in ["600", "640"]:
        results.append(finding(
            "FS-001",
            "/etc/shadow permissions",
            "HIGH",
            "FAIL",
            f"Permissions are {perm}",
            "Run: chmod 600 /etc/shadow"
        ))
    else:
        results.append(finding(
            "FS-001",
            "/etc/shadow permissions",
            "HIGH",
            "PASS",
            "Permissions are secure",
            "No action required"
        ))

    return results
