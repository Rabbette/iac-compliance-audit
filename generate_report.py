"""
IaC Compliance Audit - Checkov Results to Executive Report
---------------------------------------------------------------------
Reads raw Checkov scan results (JSON) and converts them into a clean,
executive-readable Markdown audit report.

Checkov's free/open-source output does not include a severity ranking
out of the box (that's a paid platform feature), so this script applies
its own custom severity tiers based on check ID, the same kind of
judgment call an auditor makes when deciding what to escalate to
leadership versus what to log as a minor finding.
"""

import json
from datetime import datetime

# ---------------------------------------------------------------------
# STEP 1: Define our own severity tiers.
# Each check ID is the unique identifier Checkov assigns to a specific
# rule. We're manually assigning business-risk severity to the ones
# relevant to this audit, since Checkov's free tier doesn't rank them.
# ---------------------------------------------------------------------

SEVERITY_OVERRIDES = {
    "CKV_AWS_24": {"severity": "CRITICAL", "reason": "SSH port open to the entire internet allows unrestricted remote access attempts from anywhere."},
    "CKV_AWS_53": {"severity": "CRITICAL", "reason": "S3 bucket public ACL blocking is disabled, allowing the bucket to be made publicly accessible."},
    "CKV_AWS_54": {"severity": "CRITICAL", "reason": "S3 bucket public policy blocking is disabled, allowing public bucket policies to take effect."},
    "CKV_AWS_55": {"severity": "HIGH", "reason": "S3 bucket does not ignore public ACLs, increasing risk of accidental public exposure."},
    "CKV_AWS_56": {"severity": "HIGH", "reason": "S3 bucket does not restrict public bucket access, increasing risk of accidental public exposure."},
    "CKV_AWS_20": {"severity": "CRITICAL", "reason": "S3 bucket ACL is explicitly set to allow public read access."},
    "CKV_AWS_19": {"severity": "HIGH", "reason": "S3 bucket does not have server-side encryption configured, leaving data unencrypted at rest."},
}

# Default tier for any check not explicitly listed above
DEFAULT_SEVERITY = "MEDIUM"


def load_checkov_results(json_path: str):
    """Reads the raw Checkov JSON scan output."""
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


def classify_findings(checkov_data: dict):
    """
    Walks through every failed check and assigns a severity tier.
    Returns a list of findings sorted by severity (most severe first).
    """
    severity_rank = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
    findings = []

    failed_checks = checkov_data["results"]["failed_checks"]

    for check in failed_checks:
        check_id = check["check_id"]
        override = SEVERITY_OVERRIDES.get(check_id)

        findings.append({
            "check_id": check_id,
            "check_name": check["check_name"],
            "resource": check["resource"],
            "file_path": check["file_path"],
            "line_range": check["file_line_range"],
            "severity": override["severity"] if override else DEFAULT_SEVERITY,
            "business_reason": override["reason"] if override else "Deviates from security best practice; recommend review.",
        })

    findings.sort(key=lambda x: severity_rank.get(x["severity"], 99))
    return findings


def generate_markdown_report(findings: list, output_path: str, scanned_file: str):
    """Writes a clean, executive-readable Markdown audit report."""
    severity_counts = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0}
    for f in findings:
        severity_counts[f["severity"]] += 1

    lines = []
    lines.append("# Infrastructure-as-Code Compliance Audit Report")
    lines.append("")
    lines.append(f"**Scanned file:** `{scanned_file}`")
    lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append(f"**Total findings:** {len(findings)}")
    lines.append("")
    lines.append("## Severity Breakdown")
    lines.append("")
    lines.append("| Severity | Count |")
    lines.append("|---|---|")
    for severity in ["CRITICAL", "HIGH", "MEDIUM", "LOW"]:
        lines.append(f"| {severity} | {severity_counts[severity]} |")
    lines.append("")

    priority_findings = [f for f in findings if f["severity"] in ("CRITICAL", "HIGH")]
    lines.append("## Priority Findings (Critical & High Only)")
    lines.append("")
    lines.append("These require remediation before this infrastructure should ever be deployed. Medium and Low findings are listed in full further below for technical reference, but should not block deployment on their own.")
    lines.append("")
    for finding in priority_findings:
        lines.append(f"### [{finding['severity']}] {finding['check_name']}")
        lines.append(f"- **Check ID:** `{finding['check_id']}`")
        lines.append(f"- **Resource:** `{finding['resource']}`")
        lines.append(f"- **Location:** {finding['file_path']} (lines {finding['line_range'][0]}-{finding['line_range'][-1]})")
        lines.append(f"- **Why it matters:** {finding['business_reason']}")
        lines.append("")

    lines.append("## Full Findings (All Severities)")
    lines.append("")

    for finding in findings:
        lines.append(f"### [{finding['severity']}] {finding['check_name']}")
        lines.append(f"- **Check ID:** `{finding['check_id']}`")
        lines.append(f"- **Resource:** `{finding['resource']}`")
        lines.append(f"- **Location:** {finding['file_path']} (lines {finding['line_range'][0]}-{finding['line_range'][-1]})")
        lines.append(f"- **Why it matters:** {finding['business_reason']}")
        lines.append("")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def print_summary(findings: list):
    """Prints a quick summary to the terminal."""
    severity_counts = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0}
    for f in findings:
        severity_counts[f["severity"]] += 1

    print("=" * 60)
    print("IAC COMPLIANCE AUDIT SUMMARY")
    print("=" * 60)
    print(f"Total findings: {len(findings)}")
    for severity in ["CRITICAL", "HIGH", "MEDIUM", "LOW"]:
        print(f"  {severity}: {severity_counts[severity]}")
    print()
    print("Full report saved to audit_report.md")


if __name__ == "__main__":
    checkov_data = load_checkov_results("checkov_results.json")
    findings = classify_findings(checkov_data)
    generate_markdown_report(findings, "audit_report.md", "main.tf")
    print_summary(findings)
