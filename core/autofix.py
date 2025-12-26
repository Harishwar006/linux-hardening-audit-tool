import subprocess

SAFE_FIXES = {
    "SSH-001": "sed -i 's/^PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config",
    "SSH-002": "sed -i 's/^PasswordAuthentication.*/PasswordAuthentication no/' /etc/ssh/sshd_config",
    "KERN-001": "sysctl -w kernel.randomize_va_space=2",
    "FS-001": "chmod 600 /etc/shadow"
}

def apply_fixes(findings):
    print("[!] Auto-Fix mode ENABLED")
    print("[!] Applying SAFE fixes only\n")

    for f in findings:
        if f["status"] == "FAIL" and f["id"] in SAFE_FIXES:
            cmd = SAFE_FIXES[f["id"]]
            print(f"[FIX] {f['id']} → {cmd}")
            subprocess.call(cmd, shell=True)

    print("\n[+] Auto-Fix completed")
    print("[!] Restart SSH manually if needed: systemctl restart ssh")
