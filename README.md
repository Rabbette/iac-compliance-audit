# IaC Compliance Audit

Audits cloud infrastructure for security misconfigurations *before* it's ever deployed, using static analysis on Infrastructure-as-Code (Terraform) files. This is the "Shift Left" security model: catching problems in the blueprint instead of after the building is already standing.

## Scenario

A fictional company's proposed AWS infrastructure (`main.tf`) is scanned for security violations using Checkov, a free, open-source static analysis tool, before deployment. The raw scan results are then converted into a clean, severity-ranked report suitable for both engineers and leadership.

## What's deliberately wrong in `main.tf`

This Terraform file is never deployed, it exists purely to be scanned. It contains intentional violations:

1. An S3 bucket configured with public read access
2. Public access blocking explicitly disabled on that bucket
3. An S3 bucket with no encryption configured
4. A security group with SSH (port 22) open to the entire internet (`0.0.0.0/0`)
5. An IAM policy granting unrestricted `*` permissions on `*` resources (violates least privilege)

## How it works

```
main.tf                 -> the deliberately misconfigured Terraform file (never deployed)
checkov_results.json    -> raw scan output from Checkov (generated, see below)
generate_report.py      -> converts raw results into a readable, severity-ranked Markdown report
audit_report.md         -> the final report (generated)
```

Checkov's free/open-source tier doesn't assign severity rankings out of the box, that's a paid platform feature. `generate_report.py` applies its own custom severity tiers (Critical/High/Medium/Low) based on business risk, the same judgment call an auditor applies when deciding what to escalate.

## Running it yourself

**Step 1: Install Checkov** (one-time, free, no account needed):

```
pip install checkov
```

**Step 2: Run the scan** and save results as JSON:

```
checkov -f main.tf --output json --output-file-path . --quiet
```

This creates a file called `results_json.json`. Rename it to `checkov_results.json` (or just point the script at whatever name it generates).

**Step 3: Generate the readable report:**

```
python generate_report.py
```

This reads `checkov_results.json` and produces `audit_report.md`, a severity-ranked, leadership-readable summary.

## What I'd build next

- Scan multiple Terraform files across a whole module/repo, not just one file
- Add a "remediated" tracking field so re-scans show progress over time
- Wire this into a GitHub Action so every pull request gets an automatic compliance check before merge
