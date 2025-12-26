import subprocess
from core.auditor import finding

def run():
    results = []

    value = subprocess.getoutput("sysctl -n kernel.randomize_va_space")

    if value != "2":
        results.append(finding(
            "KERN-001",
            "ASLR enabled",
            "HIGH",
            "FAIL",
            f"ASLR value is {value}",
            "Set kernel.randomize_va_space = 2"
        ))
    else:
        results.append(finding(
            "KERN-001",
            "ASLR enabled",
            "HIGH",
            "PASS",
            "ASLR is enabled",
            "No action required"
        ))

    return results
