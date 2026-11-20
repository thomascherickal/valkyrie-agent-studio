# Security & AppSec

Security & AppSec suite of 20 focused autonomous agents in Valkyrie Agent Studio.

## Engine Policy
- **Default:** `gemini-4-hydrogen` (`thinking_level: low`, `high` optional per agent)
- **Free-First Fallback:** `opencode_free` -> `openrouter_free` -> `ollama` (`qwen3.5:latest`)

## Focused Agents
- `01-threat-modeler` — **Threat Modeler**: Runs STRIDE threat modeling across trust boundaries and data flows. (Tool: `run_stride_analysis`)
- `02-sast-triage-analyst` — **SAST Triage Analyst**: Separates reachable injection sinks from dead-code false positives. (Tool: `assess_reachability`)
- `03-iam-least-privilege` — **IAM Least Privilege Auditor**: Replaces wildcard IAM permissions with scoped resource ARNs. (Tool: `narrow_iam_actions`)
- `04-secret-leak-scanner` — **Secret Leak Scanner**: Identifies high-entropy API tokens and outputs rotation runbooks. (Tool: `scan_secret_patterns`)
- `05-cve-impact-assessor` — **CVE Impact Assessor**: Checks if vulnerable dependency functions are actually invoked. (Tool: `evaluate_cve_exploit`)
- `06-soc2-evidence-collector` — **SOC2 Evidence Collector**: Maps CC6/CC7 controls to CI logs, PR approvals, and backup proofs. (Tool: `collect_control_proof`)
- `07-auth-flow-reviewer` — **Auth Flow Reviewer**: Verifies PKCE, state nonce, short-lived JWTs, and CSRF defenses. (Tool: `audit_oauth_flow`)
- `08-container-hardener` — **Container Hardener**: Audits Dockerfiles for non-root USER, pinned digests, and multi-stage. (Tool: `lint_dockerfile`)
- `09-pentest-remediator` — **Pentest Remediator**: Translates pentest PoCs into concrete parameterized code patches. (Tool: `draft_security_patch`)
- `10-security-advisory-writer` — **Security Advisory Writer**: Drafts transparent CVE advisories with affected versions and mitigations. (Tool: `format_advisory_md`)
- `11-api-security-reviewer` — **API Security Reviewer**: Reviews API specs against the OWASP API Top 10 for authorization, exposure, and abuse risks. (Tool: `review_api_security`)
- `12-supply-chain-assessor` — **Supply Chain Risk Assessor**: Assesses software supply chain risk across dependencies, build systems, and release signing. (Tool: `assess_supply_chain`)
- `13-forensics-guide` — **Incident Forensics Guide**: Guides digital forensics collection with evidence order, preservation, and chain of custody. (Tool: `plan_forensics`)
- `14-data-classification-advisor` — **Data Classification Advisor**: Classifies data stores by sensitivity and maps required controls for each class. (Tool: `classify_data`)
- `15-vendor-security-reviewer` — **Vendor Security Reviewer**: Reviews vendor security questionnaires and evidence to rate third-party risk. (Tool: `review_vendor_security`)
- `16-phishing-report-triager` — **Phishing Report Triager**: Triages reported phishing emails by indicators, impact, and required response actions. (Tool: `triage_phishing`)
- `17-cloud-posture-reviewer` — **Cloud Posture Reviewer**: Reviews cloud configuration for public exposure, identity risks, logging gaps, and drift. (Tool: `review_cloud_posture`)
- `18-security-training-planner` — **Security Training Planner**: Plans role-based security training with topics, cadence, measures, and engagement tactics. (Tool: `plan_security_training`)
- `19-crypto-usage-reviewer` — **Cryptography Usage Reviewer**: Reviews code for weak algorithms, key handling, randomness, and mode misuse. (Tool: `review_crypto_usage`)
- `20-bug-bounty-triager` — **Bug Bounty Triager**: Triages bug bounty reports by validity, severity, duplicates, scope, and reward. (Tool: `triage_bounty_report`)
