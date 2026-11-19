"""Playbooks for the Security and AppSec agents."""

PLAYBOOKS: dict[str, dict[str, list]] = {
    "06-security-appsec/01-threat-modeler": {
        "fields": ["boundaries|Trust boundaries|list|Electron renderer to local FastAPI, Local FastAPI to Gemini API over the internet, Local disk to agent definitions", "assets|Assets to protect|list|Provider API keys, Agent definitions, Run history and prompts", "authn|Authentication in place|text|Loopback only, no authentication on the local API", "likelihood|Likelihood of the top threat (1 to 5)|number|3", "impact|Impact of the top threat (1 to 5)|number|5"],
        "sections": [
            ["System", "Architecture: {input}", "Authentication today: {authn}", "Draw a data flow diagram first: external entities, processes, data stores and every flow that crosses a boundary."],
            ["Boundaries", "*{boundaries}", "Threats concentrate where data crosses a trust boundary; analyse every flow that crosses one."],
            ["STRIDE per element", "Spoofing: can another local process impersonate the UI? Tampering: can agent definitions or prompts be modified? Repudiation: are actions logged? Information disclosure: where do keys and prompts land (logs, crash reports)? Denial of service: unbounded runs or payloads? Elevation of privilege: does a generated Python agent run with the user's full rights?", "Any local HTTP service can be reached by a web page via DNS rebinding or CSRF: require an origin check and a per-session token."],
            ["Assets", "*{assets}", "Rank assets by confidentiality, integrity and availability impact to decide mitigation order."],
            ["Mitigation and risk", "Score risk as likelihood times impact; 15 or more is a release blocker, 8 to 14 needs a dated plan, below 8 is accepted with an owner.", "Prefer controls that remove the threat: sandbox generated code, store secrets in the OS keychain, bind to 127.0.0.1, validate every input, and add audit logging."],
        ],
        "metrics": ["Risk score (likelihood x impact)|likelihood * impact|{:.0f} of 25", "Share of maximum risk|likelihood * impact / 25|{:.0%}"],
    },
    "06-security-appsec/02-sast-triage-analyst": {
        "fields": ["tool|Scanner and rule|text|Semgrep python.lang.security.dangerous-subprocess-use", "reachable_from|Where the code runs|text|dev_script.py runs only on developer machines; production uses parameterized SQL", "cvss|Base severity (CVSS)|number|7.5", "exposure|Exposure factor (0 unreachable, 0.3 internal, 1 internet-facing)|number|0.1", "fix_sla_days|Fix SLA for this exposure (days)|number|30"],
        "sections": [
            ["Finding", "Finding: {input}", "Scanner: {tool}. Runs where: {reachable_from}."],
            ["Reachability test", "Trace from an entry point (HTTP handler, queue consumer, CLI argument) to the sink. Ask: can attacker-controlled data reach it, is it sanitised on the way, and is the file even deployed or imported?", "A sink in dead code, a test helper or a developer-only script is a low-priority finding, not a false positive to ignore: record the reason."],
            ["Verdict rules", "True positive: tainted input reaches the sink unvalidated. Likely false positive: constant input, parameterised query, allow-listed value. Needs review: dynamic input of unknown origin.", "Parameterised SQL is safe against injection, so flag SQL built with f-strings or concatenation instead."],
            ["Prioritisation", "Adjusted risk = CVSS x exposure. Fix internet-facing injection (CWE-89, CWE-78, CWE-22) within days; schedule internal or dev-only findings with the normal backlog.", "Suppress with an inline comment that states the reason and an expiry date."],
            ["Process", "Close each finding with a verdict, evidence and reviewer. Track false-positive rate per rule and tune or disable rules above 50 percent.", "Re-scan after fixes and require the finding to disappear."],
        ],
        "metrics": ["Adjusted risk (CVSS x exposure)|cvss * exposure|{:.2f}", "Share of raw severity that applies|exposure|{:.0%}"],
    },
    "06-security-appsec/03-iam-least-privilege": {
        "fields": ["principal|Role or principal|text|analytics-reader (assumed by the BI service)", "needed_actions|Actions actually used|list|s3:GetObject, s3:ListBucket", "resources|Resources needed|list|arn:aws:s3:::analytics-prod-curated, arn:aws:s3:::analytics-prod-curated/*", "current_actions|Actions currently granted|number|140", "needed_count|Number of actions actually needed|number|2", "condition|Condition to add|text|aws:SourceVpce equals the BI VPC endpoint"],
        "sections": [
            ["Policy under review", "Policy: {input}", "Principal: {principal}. Currently grants about {current_actions} actions."],
            ["Used actions", "*{needed_actions}", "Derive the list from CloudTrail or IAM Access Analyzer last-accessed data over 90 days, not from guesswork."],
            ["Scoped resources", "*{resources}", "Bucket-level actions (ListBucket) apply to the bucket ARN; object actions (GetObject) apply to bucket/*. Replace Resource * with exact ARNs."],
            ["Hardening", "Add a Condition: {condition}. Consider aws:PrincipalOrgID, aws:SecureTransport and a permissions boundary. Add an explicit Deny for destructive actions on production data.", "Avoid NotAction and iam:PassRole with wildcards; PassRole plus compute creation is a privilege escalation path."],
            ["Rollout", "Test in a non-production account with the IAM policy simulator, deploy the narrow policy alongside the old one, watch AccessDenied for 2 weeks, then remove the wide policy.", "Schedule a quarterly access review."],
        ],
        "metrics": ["Permission reduction|1 - needed_count / current_actions|{:.0%}"],
    },
    "06-security-appsec/04-secret-leak-scanner": {
        "fields": ["secret_type|Secret type|text|Google Gemini API key", "repo_visibility|Repository visibility|text|Private repository, 14 collaborators", "exposed_hours|Hours since the commit|number|6", "rotate_sla_hours|Rotation SLA (hours)|number|1", "owner|Key owner|text|Platform team"],
        "sections": [
            ["Detection", "Diff: {input}", "Type: {secret_type}. Visibility: {repo_visibility}. Owner: {owner}."],
            ["Confirm", "Match known formats (AIza prefix for Google keys, AKIA for AWS, ghp_ for GitHub) and check entropy above about 4.5 bits per character. Treat placeholders (example, dummy, changeme) as findings to confirm with the provider, not to dismiss.", "Verify validity with a harmless authenticated call only if policy allows; otherwise assume it is live."],
            ["Rotate first", "Order: 1. revoke or rotate the key now. 2. Check provider logs for use since the commit. 3. Create a replacement in the secret manager. 4. Remove from code. 5. Scrub history.", "Rotation SLA is {rotate_sla_hours} hour(s); exposed for {exposed_hours} hours already."],
            ["Clean the history", "Deleting the line is not enough: the secret remains in git history, forks and caches. Use git filter-repo or BFG, force-push, and ask collaborators to re-clone.", "Treat anything pushed to a public repository as compromised permanently."],
            ["Prevention", "Install a pre-commit hook (gitleaks, detect-secrets), enable push protection and secret scanning, load secrets from environment variables or a vault, and give keys least privilege and quotas.", "Add the incident to the secret inventory with the rotation date."],
        ],
        "metrics": ["Hours past the rotation SLA|max(0, exposed_hours - rotate_sla_hours)|{:.1f}"],
    },
    "06-security-appsec/05-cve-impact-assessor": {
        "fields": ["cvss|CVSS base score|number|7.5", "epss_pct|EPSS exploit probability (percent)|number|2", "reach_factor|Reachability factor (0 not loaded, 0.3 loaded not called, 1 called)|number|0.1", "patch_sla_days|Patch SLA at this level (days)|number|30", "package|Package and dependency path|text|libxml-parser 3.1 via transitive dependency of report-export"],
        "sections": [
            ["Advisory", "Record: {input}", "Package: {package}. CVSS {cvss}, EPSS {epss_pct} percent."],
            ["Is it reachable?", "Check three levels: is the package installed in the shipped artifact, is the vulnerable module imported, and is the vulnerable function called with attacker-controlled input? Use the call graph (govulncheck, pip-audit with reachability, Snyk) rather than the manifest.", "A transitive parser that is never imported scores low in your context regardless of the CVSS."],
            ["Impact level", "Critical: reachable, internet-facing, exploit known (EPSS above 10 percent or on the CISA KEV list). High: reachable, authenticated or internal. Medium: loaded but not called. Low: not loaded or dev-only.", "Context-adjusted score = CVSS x reachability factor."],
            ["Action and SLA", "Critical: fix or mitigate within 72 hours. High: {patch_sla_days} days or sooner if exploited. Medium: next release. Low: track and bump with routine updates.", "Mitigations: upgrade, pin a patched fork, disable the feature, add a WAF rule, or remove the dependency."],
            ["Record", "Document the decision in a VEX statement (not affected, affected, fixed, under investigation) with the justification so auditors and customers can see it.", "Re-evaluate when the code or the EPSS score changes."],
        ],
        "metrics": ["Context-adjusted score|cvss * reach_factor|{:.2f}", "EPSS probability of exploitation in 30 days (percent)|epss_pct|{:.1f}"],
    },
    "06-security-appsec/06-soc2-evidence-collector": {
        "fields": ["audit_period|Audit period|text|2026-01-01 to 2026-09-30 (Type II)", "prs_merged|Pull requests merged in period|number|412", "prs_reviewed|Merged with required approval and green tests|number|409", "systems|Systems of record|list|GitHub, GitHub Actions, Okta, AWS Backup", "owner|Control owner|text|VP Engineering"],
        "sections": [
            ["Control", "Control: {input}", "Period: {audit_period}. Owner: {owner}."],
            ["Evidence to collect", "Systems: {systems}. For change management (CC8.1): branch protection settings export, the PR list with approver and required status checks, CI run logs, and the deployment record linking each release to its merged PR.", "For CC6 (logical access): quarterly access reviews, joiner and leaver tickets, MFA enforcement report. For CC7 (operations): alert configuration, incident tickets, backup and restore test results."],
            ["Population and sampling", "Auditors choose a sample from the full population (often 25 to 60 items for a population of several hundred). Export the complete list with timestamps first.", "Evidence must be system generated, dated within the period and show who did what; screenshots alone are weak."],
            ["Exceptions", "Every item merged without the required approval is an exception. Record the reason (emergency fix), the retroactive review and the compensating control.", "Prepare an explanation before the auditor finds it."],
            ["Cadence", "Automate collection monthly into a locked evidence folder named by control and date. Re-test the control quarterly so the annual audit holds no surprises.", "Keep a mapping of controls to evidence owners."],
        ],
        "metrics": ["Compliance rate|prs_reviewed / prs_merged|{:.1%}", "Exceptions to explain|prs_merged - prs_reviewed|{:.0f}"],
    },
    "06-security-appsec/07-auth-flow-reviewer": {
        "fields": ["client_type|Client type|text|Public client (desktop and single-page app)", "redirect_uris|Registered redirect URIs|list|http://127.0.0.1:8765/callback, https://app.example.com/callback", "access_ttl_min|Access token lifetime (minutes)|number|60", "refresh_ttl_days|Refresh token lifetime (days)|number|90", "idp|Identity provider|text|Okta with Authorization Code flow"],
        "sections": [
            ["Flow", "Spec: {input}", "Client: {client_type}. Provider: {idp}."],
            ["PKCE", "Public clients must use Authorization Code with PKCE (RFC 7636): a random code_verifier of 43 to 128 characters, code_challenge with S256 (never plain), and the verifier sent at the token exchange. A code flow without code_challenge allows authorization code interception.", "The implicit flow and the password grant should not be used."],
            ["State, nonce and redirects", "Generate an unguessable state per request and verify it on return (CSRF defence); use a nonce for OpenID Connect ID tokens. Register exact redirect URIs and compare by exact match, never by prefix or wildcard.", "Redirect URIs: {redirect_uris}"],
            ["Tokens", "Access tokens should be short lived (5 to 15 minutes); currently {access_ttl_min} minutes. Rotate refresh tokens on every use with reuse detection, bind to the client, and cap lifetime (now {refresh_ttl_days} days).", "Validate JWT signature, iss, aud, exp and nbf on the resource server; reject alg none and pin accepted algorithms."],
            ["Storage and session", "Keep tokens out of localStorage when possible (use httpOnly, Secure, SameSite cookies or the OS keychain on desktop), protect cookie sessions with CSRF tokens, and support revocation and logout.", "Rate limit the token endpoint and log failed exchanges."],
        ],
        "metrics": [],
    },
    "06-security-appsec/08-container-hardener": {
        "fields": ["base_image|Current base image|text|python:3.12 (Debian full image)", "image_mb|Current image size (MB)|number|1100", "slim_mb|Expected hardened image size (MB)|number|180", "critical_cves|Critical and high CVEs in the current image|number|24", "runtime_user|Intended runtime user|text|app (uid 10001)"],
        "sections": [
            ["Dockerfile", "File: {input}", "Base: {base_image}. {image_mb} MB with {critical_cves} critical or high CVEs."],
            ["Base image", "Pin by digest (python:3.12-slim@sha256:...), choose slim or distroless/Chainguard images, and rebuild weekly. Mutable tags such as latest or 3.12 change silently.", "Use a multi-stage build: compile and install in a builder stage, copy only the virtualenv and app into the runtime stage."],
            ["Run as non-root", "Create a user ({runtime_user}) with USER app, set files owned with COPY --chown, and never run as root. Run with a read-only root filesystem, drop all capabilities and no-new-privileges.", "Do not expose the Docker socket or use privileged mode."],
            ["Build hygiene", "Install with pip install --no-cache-dir from a hashed requirements file, add a .dockerignore (git, env files, tests), keep secrets out of layers (use BuildKit secrets), and add a HEALTHCHECK.", "Use the exec form of CMD so signals reach the process: CMD followed by a JSON array."],
            ["Scan and sign", "Scan with Trivy or Grype in CI and fail on fixable critical findings, generate an SBOM, and sign images (cosign).", "Track the CVE count after hardening against the {critical_cves} baseline."],
        ],
        "metrics": ["Size reduction|1 - slim_mb / image_mb|{:.0%}", "Layers of attack surface removed (MB)|image_mb - slim_mb|{:,.0f}"],
    },
    "06-security-appsec/09-pentest-remediator": {
        "fields": ["stack|Stack and data access layer|text|Python FastAPI with SQLAlchemy and Postgres", "endpoints|Affected endpoints|list|GET /api/invoices/:id", "cvss|CVSS score of the finding|number|8.1", "days_open|Days since reported|number|3", "fix_sla_days|Fix SLA (days)|number|14"],
        "sections": [
            ["Finding", "Pentest finding: {input}", "Stack: {stack}. Severity CVSS {cvss}."],
            ["Root cause", "Insecure direct object reference (IDOR): the handler loads a record by id from the URL and never checks that it belongs to the caller's organisation. Authentication is present; authorization is missing (OWASP A01 Broken Access Control).", "Check every sibling route that takes an id for the same flaw, not only the reported one."],
            ["Patch pattern", "Scope the query by the tenant from the authenticated session: select the invoice where id equals the path id AND org_id equals the caller's org_id, and return 404 (not 403) when no row matches. Never take org_id from the request.", "Centralise it in a dependency or repository method so new routes inherit it, and consider Postgres row level security as defence in depth."],
            ["Tests", "Write a regression test: user A requests user B's invoice and must get 404; also test with a missing token, an expired token and an id from another tenant. Add it to CI.", "Include a fuzz of sequential ids to ensure no enumeration is possible; prefer UUIDs."],
            ["Delivery", "Fix SLA {fix_sla_days} days, {days_open} used. Ship the patch with a note for the tester to retest, check logs for past exploitation, and decide on customer notification.", "Rotate any data or tokens that the flaw could have exposed."],
        ],
        "metrics": ["Days left in SLA|fix_sla_days - days_open|{:.0f}", "SLA consumed|days_open / fix_sla_days|{:.0%}"],
    },
    "06-security-appsec/10-security-advisory-writer": {
        "fields": ["product|Product and component|text|Valkyrie Studio export endpoint", "affected|Affected versions|text|1.0.0 through 1.4.1", "fixed|Fixed version|text|1.4.2", "cvss|CVSS base score|number|7.5", "mitigations|Workarounds|list|Disable the export feature, Restrict API access to localhost, Upgrade to 1.4.2"],
        "sections": [
            ["Advisory summary", "Issue: {input}", "Product: {product}. Affected: {affected}. Fixed in {fixed}. CVSS {cvss}.", "Open with one plain sentence: what is wrong, who is affected, what to do."],
            ["Details", "Describe the weakness class (for example CWE-22 path traversal), the conditions needed to exploit it (authentication, network position) and the impact on confidentiality, integrity and availability.", "Do not publish exploit code or step-by-step payloads before users have had time to patch."],
            ["Affected and fixed", "Affected versions: {affected}. Patched version: {fixed}. State how to check the installed version and whether older, unsupported branches are affected.", "Request a CVE identifier from the CNA and use the CVSS 3.1 vector, not only the number."],
            ["Mitigations", "*{mitigations}", "List the upgrade first; workarounds are for those who cannot upgrade immediately."],
            ["Credits and timeline", "Credit the reporter, and list dates: reported, confirmed, fixed, released, disclosed. Aim to disclose within 90 days of the report.", "State whether there is evidence of exploitation, and give a contact for questions."],
        ],
        "metrics": [],
    },
}
