🔐 Linux Hardening Audit Tool

A lightweight, automated Linux security hardening audit tool that checks system configurations, applies safe auto-fixes, verifies improvements, and generates JSON + HTML reports.

Designed for learning, security auditing, and blue-team practice on Linux systems (Kali, Ubuntu, Debian).

---

🚀 Features

✅ Security hardening checks (SSH, Firewall, etc.)

🔧 Optional SAFE auto-fix during audit

🔁 Re-runs audit after fixes to verify effectiveness

📊 Security score calculation (0–100)

📄 Generates:

JSON report (machine-readable)

HTML report (human-friendly)


🧩 Modular & extensible architecture

🛡️ Root privilege validation (safe execution)

---

📁 Project Structure

linux-audit-tool/
│
├── audit.py                  # Main audit engine
├── hardening_report.json     # JSON output (auto-generated)
├── hardening_report.html     # HTML output (auto-generated)
│
├── reports/
│   ├── __init__.py
│   └── report_html.py        # HTML report generator
│
└── README.md

---

🧠 Checks Implemented (Current)

ID	Check Description	Severity

SSH-01	Disable SSH root login	HIGH
FW-01	Firewall enabled (UFW)	MEDIUM

---

⚙️ Requirements

Linux system (Kali / Ubuntu / Debian)

Python 3.8+

Root privileges (sudo)

UFW (for firewall checks)

---

▶️ How to Run

git clone https://github.com/yourusername/linux-hardening-audit-tool.git
cd linux-hardening-audit-tool
sudo python3 audit.py

---

🧩 How It Works

1. Runs security checks

2. Calculates initial hardening score

3. Prompts user:

Apply SAFE auto-fixes now? (yes/no)

4. Applies fixes (only safe, non-destructive)

5. Re-runs audit to verify changes

6. Generates reports

---

📊 Sample Output

Terminal

[*] Starting Linux Hardening Audit...
[+] Initial score: /100
Apply SAFE auto-fixes now? (yes/no): yes
[*] Re-running audit after fixes...
[+] Final score: /100

Generated Files

hardening_report.json

hardening_report.html

---

🌐 View HTML Report

xdg-open hardening_report.html  (or)
firefox hardening_report.html

---

🧪 Auto-Fix Safety Policy

✔ Only SAFE configurations
✔ No service removal
✔ No user deletion
✔ No destructive commands

Examples:

Disable SSH root login

Enable firewall

Service restart  only when required

---



---

Just say NEXT 🚀
