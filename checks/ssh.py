import subprocess
from core.auditor import finding

def run():
    results = []

    ssh_config = "/etc/ssh/sshd_config"

    # SSH Root Login
    root_login = subprocess.getoutput(
        f"grep -Ei '^PermitRootLogin' {ssh_config}"
    )

    if "yes" in root_login.lower():
        results.append(finding(
            "SSH-001",
            "SSH Root Login",
            "CRITICAL",
            "FAIL",
            "Root login via SSH is enabled",
            "Set PermitRootLogin no in sshd_config"
        ))
    else:
        results.append(finding(
            "SSH-001",
            "SSH Root Login",
            "CRITICAL",
            "PASS",
            "Root login via SSH is disabled",
            "No action required"
        ))

    # SSH Password Authentication
    password_auth = subprocess.getoutput(
        f"grep -Ei '^PasswordAuthentication' {ssh_config}"
    )

    if "yes" in password_auth.lower():
        results.append(finding(
            "SSH-002",
            "SSH Password Authentication",
            "HIGH",
            "FAIL",
            "Password authentication is enabled",
            "Set PasswordAuthentication no and use SSH keys"
        ))
    else:
        results.append(finding(
            "SSH-002",
            "SSH Password Authentication",
            "HIGH",
            "PASS",
            "Password authentication disabled",
            "No action required"
        ))

    # SSH Protocol Version
    protocol = subprocess.getoutput(
        f"grep -Ei '^Protocol' {ssh_config}"
    )

    if "2" not in protocol:
        results.append(finding(
            "SSH-003",
            "SSH Protocol Version",
            "HIGH",
            "FAIL",
            "SSH protocol 2 not enforced",
            "Set Protocol 2"
        ))
    else:
        results.append(finding(
            "SSH-003",
            "SSH Protocol Version",
            "HIGH",
            "PASS",
            "SSH Protocol 2 enforced",
            "No action required"
        ))

    return results
