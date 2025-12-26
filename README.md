🔐 Linux Hardening Audit Tool

A lightweight, automated Linux security hardening audit tool that checks system configurations, applies safe auto-fixes, verifies improvements, and generates JSON + HTML reports.
Designed for learning, security auditing, and blue-team practice on Linux systems (Kali, Ubuntu, Debian).
--------------------------------
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

--------------------------------

📁 Project Structure

Copy code

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
-------------------------------
🧠 Checks Implemented (Current)
ID
Check Description
Severity
SSH-01
Disable SSH root login
HIGH
FW-01
Firewall enabled (UFW)
MEDIUM
-------------------------------
⚙️ Requirements
Linux system
Python 3.8+
Root privileges (sudo)
UFW (for firewall checks)
-------------------------------
▶️ How to Run
Copy code
Bash
git clone https://github.com/Harishwar006/linux-hardening-audit-tool.git
cd linux-hardening-audit-tool
sudo python3 audit.py
-------------------------------
🧩 How It Works
Runs security checks
Calculates initial hardening score
Prompts user:
Copy code

Apply SAFE auto-fixes now? (yes/no)
Applies fixes (only safe, non-destructive)
Re-runs audit to verify changes
Generates reports
--------------------------------
📊 Sample Output
Terminal
Copy code

[*] Starting Linux Hardening Audit...
[+] Initial score: 93/100
Apply SAFE auto-fixes now? (yes/no): yes
[*] Re-running audit after fixes...
[+] Final score: 100/100
Generated Files
hardening_report.json
hardening_report.html
---------------------------------
🌐 View HTML Report
Copy code
Bash
xdg-open hardening_report.html
firefox hardening_report.html
---------------------------------
🧪 Auto-Fix Safety Policy
✔ Only SAFE configurations
✔ No service removal
✔ No user deletion
✔ No destructive commands
Examples:
Disable SSH root login
Enable firewall
Service restart提示 only when required
sudo python3 audit.py
---------------------------------
