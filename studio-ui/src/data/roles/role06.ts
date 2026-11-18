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
    }
  ]
};
