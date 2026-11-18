# Security & AppSec

Security & AppSec suite of 10 focused autonomous agents in Valkyrie AI Agent Studio.

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
