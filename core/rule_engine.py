import json
import subprocess
from core.auditor import finding

def load_rules(path):
    with open(path, "r") as f:
        return json.load(f)

def evaluate_rule(rule):
    output = subprocess.getoutput(rule["check"]).strip()

    expected = rule["expect"]
    status = "FAIL"

    if expected == "NOT_PRESENT" and output == "":
        status = "PASS"
    elif expected == "ONLY_root" and output == "root":
        status = "PASS"
    elif expected == output:
        status = "PASS"

    return finding(
        rule["id"],
        rule["title"],
        rule["severity"],
        status,
        f"Command output: {output if output else 'None'}",
        rule["fix"]
    )

def run_rules(rule_file):
    results = []
    rules = load_rules(rule_file)

    for rule in rules:
        results.append(evaluate_rule(rule))

    return results
