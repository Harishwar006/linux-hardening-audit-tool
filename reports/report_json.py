import json
import socket
from datetime import datetime
from core.scoring import calculate_score
from reports.report_html import generate_html

def generate_report(results):
    hardening_score, risk_score, max_score = calculate_score(results)

    report = {
        "hostname": socket.gethostname(),
        "timestamp": datetime.now().isoformat(),
        "hardening_score": hardening_score,
        "risk_score": risk_score,
        "max_risk": max_score,
        "total_checks": len(results),
        "findings": results
    }

    with open("hardening_report.json", "w") as f:
        json.dump(report, f, indent=4)

    generate_html(report)

    print("[+] JSON report generated: hardening_report.json")
    print("[+] Hardening Score:", hardening_score, "/100")
