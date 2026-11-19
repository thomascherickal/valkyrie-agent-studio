import type { RoleCatalog } from "../types";

export const ROLE_06: RoleCatalog = {
  "id": "06-security-appsec",
  "name": "Security & AppSec",
  "agents": [
    {
      "id": "01-threat-modeler",
      "name": "Threat Modeler",
      "description": "Runs STRIDE threat modeling across trust boundaries and data flows.",
      "tool": "run_stride_analysis",
      "inputKey": "architecture_desc",
      "outputKey": "threat_matrix",
      "sampleInput": "Desktop Electron UI -> Local FastAPI -> Gemini API"
    },
    {
      "id": "02-sast-triage-analyst",
      "name": "SAST Triage Analyst",
      "description": "Separates reachable injection sinks from dead-code false positives.",
      "tool": "assess_reachability",
      "inputKey": "sast_finding",
      "outputKey": "triage_verdict",
      "sampleInput": "CWE-78 in dev_script.py vs parameterized SQL in prod"
    },
    {
      "id": "03-iam-least-privilege",
      "name": "IAM Least Privilege Auditor",
      "description": "Replaces wildcard IAM permissions with scoped resource ARNs.",
      "tool": "narrow_iam_actions",
      "inputKey": "iam_policy",
      "outputKey": "scoped_policy",
      "sampleInput": "Action: s3:*, Resource: * for analytics-reader role"
    },
    {
      "id": "04-secret-leak-scanner",
      "name": "Secret Leak Scanner",
      "description": "Identifies high-entropy API tokens and outputs rotation runbooks.",
      "tool": "scan_secret_patterns",
      "inputKey": "diff_text",
      "outputKey": "leak_alert",
      "sampleInput": "GEMINI_API_KEY=AIzaSyDummyExampleToken12345"
    },
    {
      "id": "05-cve-impact-assessor",
      "name": "CVE Impact Assessor",
      "description": "Checks if vulnerable dependency functions are actually invoked.",
      "tool": "evaluate_cve_exploit",
      "inputKey": "cve_record",
      "outputKey": "impact_level",
      "sampleInput": "CVE-2026-1042 in transitive XML parser (unused in app)"
    },
    {
      "id": "06-soc2-evidence-collector",
      "name": "SOC2 Evidence Collector",
      "description": "Maps CC6/CC7 controls to CI logs, PR approvals, and backup proofs.",
      "tool": "collect_control_proof",
      "inputKey": "control_id",
      "outputKey": "evidence_bundle",
      "sampleInput": "CC8.1 Change Management \u2014 require 100% tests before merge"
    },
    {
      "id": "07-auth-flow-reviewer",
      "name": "Auth Flow Reviewer",
      "description": "Verifies PKCE, state nonce, short-lived JWTs, and CSRF defenses.",
      "tool": "audit_oauth_flow",
      "inputKey": "auth_spec",
      "outputKey": "auth_findings",
      "sampleInput": "OAuth2 Authorization Code flow without PKCE code_challenge"
    },
    {
      "id": "08-container-hardener",
      "name": "Container Hardener",
      "description": "Audits Dockerfiles for non-root USER, pinned digests, and multi-stage.",
      "tool": "lint_dockerfile",
      "inputKey": "dockerfile_text",
      "outputKey": "hardened_diff",
      "sampleInput": "FROM python:3.12\nRUN pip install fastapi\nCMD python app.py"
    },
    {
      "id": "09-pentest-remediator",
      "name": "Pentest Remediator",
      "description": "Translates pentest PoCs into concrete parameterized code patches.",
      "tool": "draft_security_patch",
      "inputKey": "finding_summary",
      "outputKey": "remediation_pr",
      "sampleInput": "IDOR on GET /api/invoices/{id} missing org_id check"
    },
    {
      "id": "10-security-advisory-writer",
      "name": "Security Advisory Writer",
      "description": "Drafts transparent CVE advisories with affected versions and mitigations.",
      "tool": "format_advisory_md",
      "inputKey": "advisory_input",
      "outputKey": "advisory_doc",
      "sampleInput": "Patched path traversal in export endpoint in v1.4.2"
    },
    {
      "id": "11-api-security-reviewer",
      "name": "API Security Reviewer",
      "description": "Reviews API specs against the OWASP API Top 10 for authorization, exposure, and abuse risks.",
      "tool": "review_api_security",
      "inputKey": "api_spec",
      "outputKey": "api_findings",
      "sampleInput": "GET /invoices/{id} returns any invoice for any logged-in user; list endpoint has no pagination limit"
    },
    {
      "id": "12-supply-chain-assessor",
      "name": "Supply Chain Risk Assessor",
      "description": "Assesses software supply chain risk across dependencies, build systems, and release signing.",
      "tool": "assess_supply_chain",
      "inputKey": "dependency_notes",
      "outputKey": "supply_chain_report",
      "sampleInput": "1,240 transitive packages, 36 maintained by one person, builds pull unpinned actions, images unsigned"
    },
    {
      "id": "13-forensics-guide",
      "name": "Incident Forensics Guide",
      "description": "Guides digital forensics collection with evidence order, preservation, and chain of custody.",
      "tool": "plan_forensics",
      "inputKey": "incident_summary",
      "outputKey": "forensics_plan",
      "sampleInput": "Suspected credential theft on 3 production hosts, first alert 02:10 UTC, logs kept 14 days"
    },
    {
      "id": "14-data-classification-advisor",
      "name": "Data Classification Advisor",
      "description": "Classifies data stores by sensitivity and maps required controls for each class.",
      "tool": "classify_data",
      "inputKey": "data_inventory",
      "outputKey": "classification_map",
      "sampleInput": "Customer DB with emails and payment tokens; analytics warehouse with pseudonymous IDs; public marketing site"
    },
    {
      "id": "15-vendor-security-reviewer",
      "name": "Vendor Security Reviewer",
      "description": "Reviews vendor security questionnaires and evidence to rate third-party risk.",
      "tool": "review_vendor_security",
      "inputKey": "vendor_answers",
      "outputKey": "vendor_risk",
      "sampleInput": "Vendor stores customer emails, SOC 2 Type I only, no pen test in 2 years, subprocessors listed, 99.5% SLA"
    },
    {
      "id": "16-phishing-report-triager",
      "name": "Phishing Report Triager",
      "description": "Triages reported phishing emails by indicators, impact, and required response actions.",
      "tool": "triage_phishing",
      "inputKey": "reported_email",
      "outputKey": "phishing_verdict",
      "sampleInput": "Subject Urgent payroll update; link to payr0ll-portal.example; sent to 240 staff; 12 clicked, 3 entered passwords"
    },
    {
      "id": "17-cloud-posture-reviewer",
      "name": "Cloud Posture Reviewer",
      "description": "Reviews cloud configuration for public exposure, identity risks, logging gaps, and drift.",
      "tool": "review_cloud_posture",
      "inputKey": "cloud_config",
      "outputKey": "posture_report",
      "sampleInput": "3 public storage buckets, 14 security groups open to 0.0.0.0/0, CloudTrail off in 2 regions, root has no MFA"
    },
    {
      "id": "18-security-training-planner",
      "name": "Security Training Planner",
      "description": "Plans role-based security training with topics, cadence, measures, and engagement tactics.",
      "tool": "plan_security_training",
      "inputKey": "team_profile",
      "outputKey": "training_plan",
      "sampleInput": "420 staff: 90 engineers, 40 support with customer data access, 20 finance; phishing click rate 11%"
    },
    {
      "id": "19-crypto-usage-reviewer",
      "name": "Cryptography Usage Reviewer",
      "description": "Reviews code for weak algorithms, key handling, randomness, and mode misuse.",
      "tool": "review_crypto_usage",
      "inputKey": "code_snippet",
      "outputKey": "crypto_findings",
      "sampleInput": "hash = md5(password); key = 'hardcoded-secret'; token = random.randint(100000, 999999); AES in ECB mode"
    },
    {
      "id": "20-bug-bounty-triager",
      "name": "Bug Bounty Triager",
      "description": "Triages bug bounty reports by validity, severity, duplicates, scope, and reward.",
      "tool": "triage_bounty_report",
      "inputKey": "bounty_report",
      "outputKey": "bounty_verdict",
      "sampleInput": "Researcher reports stored XSS in the profile bio field on app.example.com, proof of concept attached"
    }
  ]
};
