from checks import users, filesystem, network, kernel, ssh
from reports.report_json import generate_report
from core.rule_engine import run_rules
from core.autofix import apply_fixes
from core.scoring import calculate_score

def run_all_checks():
    results = []
    results += users.run()
    results += filesystem.run()
    results += network.run()
    results += kernel.run()
    results += ssh.run()
    results += run_rules("rules/cis_basic.json")
    return results

def main():
    # Initial audit
    before_results = run_all_checks()
    before_failed = [f for f in before_results if f["status"] == "FAIL"]
    before_score, _, _ = calculate_score(before_results)

    print(f"\n[+] Initial audit completed")
    print(f"[+] Failed checks: {len(before_failed)}")
    print(f"[+] Hardening Score: {before_score}/100")

    # Ask for auto-fix
    if before_failed:
        choice = input("\n[?] Apply SAFE auto-fixes now? (yes/no): ").strip().lower()

        if choice == "yes":
            apply_fixes(before_results)

            print("\n[+] Re-running audit after fixes...\n")
            after_results = run_all_checks()
            after_failed = [f for f in after_results if f["status"] == "FAIL"]
            after_score, _, _ = calculate_score(after_results)

            fixed_count = len(before_failed) - len(after_failed)
            score_gain = after_score - before_score

            print("========== AUTO-FIX VERIFICATION ==========")
            print(f"✓ Issues before fix : {len(before_failed)}")
            print(f"✓ Issues after fix  : {len(after_failed)}")
            print(f"✓ Fixed successfully: {fixed_count}")
            print(f"✓ Score improved    : +{score_gain} points")
            print("==========================================")

            generate_report(after_results)
            return

        else:
            print("[!] Auto-fix skipped by user")

    generate_report(before_results)

if __name__ == "__main__":
    main()
