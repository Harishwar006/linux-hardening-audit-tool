import socket
from datetime import datetime

def generate_html(report_data):
    findings = report_data["findings"]

    severity_color = {
        "CRITICAL": "red",
        "HIGH": "orange",
        "MEDIUM": "gold",
        "LOW": "green",
        "INFO": "gray"
    }

    rows = ""
    for f in findings:
        color = severity_color.get(f["severity"], "black")
        rows += f"""
        <tr>
            <td>{f['id']}</td>
            <td>{f['title']}</td>
            <td style="color:{color};">{f['severity']}</td>
            <td>{f['status']}</td>
            <td>{f['description']}</td>
            <td>{f['fix']}</td>
        </tr>
        """

    html = f"""
    <html>
    <head>
        <title>Linux Hardening Audit Report</title>
        <style>
            body {{ font-family: Arial; margin: 40px; }}
            h1 {{ color: #2c3e50; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; }}
            th {{ background-color: #34495e; color: white; }}
            tr:nth-child(even) {{ background-color: #f2f2f2; }}
        </style>
    </head>
    <body>
        <h1>Linux Hardening Audit Report</h1>
        <p><b>Hostname:</b> {socket.gethostname()}</p>
        <p><b>Date:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        <p><b>Hardening Score:</b> {report_data['hardening_score']} / 100</p>

        <h2>Findings</h2>
        <table>
            <tr>
                <th>ID</th>
                <th>Title</th>
                <th>Severity</th>
                <th>Status</th>
                <th>Description</th>
                <th>Remediation</th>
            </tr>
            {rows}
        </table>
    </body>
    </html>
    """

    with open("hardening_report.html", "w") as f:
        f.write(html)

    print("[+] HTML report generated: hardening_report.html")
