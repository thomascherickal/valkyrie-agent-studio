"""Playbooks for the Security & AppSec agents with ids 11 to 20."""

PLAYBOOKS: dict[str, dict[str, list]] = {
    "06-security-appsec/11-api-security-reviewer": {
        "fields": ["endpoint|Endpoint|text|GET /invoices/{id}", "endpoints|Endpoints in scope|number|85", "unauth_checked|Endpoints with a verified ownership check|number|40", "page_limit|Maximum page size you allow|number|100", "current_limit|Current maximum page size|number|10000"],
        "sections": [
            ["Spec under review", "Spec: {input}", "Endpoint: {endpoint}. {unauth_checked} of {endpoints} endpoints have a verified ownership check.", "Most serious API bugs are authorization bugs: the caller is logged in but is not allowed to see this object."],
            ["Object-level authorization", "On every endpoint that takes an id, check that the object belongs to the caller's tenant or user. Do it on the server, in a shared policy layer, and never trust an id sent by the client.", "Test by calling each endpoint with another user's id."],
            ["Excessive data", "Return only the fields the client needs. Filter sensitive fields (tokens, internal flags, other users' data) on the server and do not rely on the client to hide them.", "Use explicit response schemas, not whole database rows."],
            ["Abuse limits", "Today the largest page is {current_limit}. Cap it at {page_limit}, add rate limits per user and per token, and limit bulk operations and expensive queries.", "Return the same error for a missing object and a forbidden one, so ids cannot be enumerated."],
            ["Inventory and versions", "Keep an up-to-date list of every endpoint and version, retire old versions and find shadow or debug endpoints through gateway logs.", "Authenticate every route by default and make public routes an explicit exception."],
        ],
        "metrics": ["Endpoints still to verify|endpoints - unauth_checked|{:,.0f}", "Share verified|unauth_checked / endpoints|{:.0%}", "Page size over the cap|current_limit / page_limit|{:,.0f}x"],
    },
    "06-security-appsec/12-supply-chain-assessor": {
        "fields": ["packages|Transitive packages|number|1240", "single_maintainer|Packages with one maintainer|number|36", "unpinned_actions|Build steps that use unpinned actions|number|18", "signed_share|Share of release artifacts that are signed (0 to 1)|number|0", "patch_days|Median days to apply a security patch|number|45"],
        "sections": [
            ["Footprint", "Notes: {input}", "{packages} transitive packages, {single_maintainer} with a single maintainer.", "Your risk is the sum of everything you run, including what you did not choose directly."],
            ["Dependencies", "Pin versions with a lock file and a hash, review new dependencies, prefer well-maintained packages and watch for typosquats and sudden ownership changes.", "Maintain a software bill of materials (SBOM) for each release so you can answer which builds contain a bad package within minutes."],
            ["Build pipeline", "{unpinned_actions} build steps use unpinned actions. Pin third-party actions to a full commit hash, give each job the least token permissions and keep secrets out of pull request builds from forks.", "Use ephemeral runners and protect the main branch with required reviews."],
            ["Artifact integrity", "Sign images and packages and record build provenance (who built it, from which commit). Verify signatures at deploy time. Signed share today: {signed_share}.", "Aim for the SLSA levels as a roadmap, not as a single project."],
            ["Response speed", "Median patch time is {patch_days} days. Automate update pull requests, subscribe to advisories and set a deadline by severity (for example critical in 7 days).", "Rehearse the response to a compromised dependency once a year."],
        ],
        "metrics": ["Share of packages with one maintainer|single_maintainer / packages|{:.1%}", "Unsigned share of release artifacts|1 - signed_share|{:.0%}"],
    },
    "06-security-appsec/13-forensics-guide": {
        "fields": ["hosts|Hosts involved|number|3", "hours_since|Hours since the first alert|number|9", "log_days|Days of logs retained|number|14", "responder|Lead responder|text|Security on-call", "legal_hold|Legal or regulatory notice needed|text|Yes, possible customer data exposure"],
        "sections": [
            ["Incident", "Summary: {input}", "{hosts} hosts, {hours_since} hours since the first alert. Lead: {responder}. Legal: {legal_hold}.", "Forensics answers what happened, how far it went and whether it is over. Collect before you clean."],
            ["Order of volatility", "Collect the most short-lived evidence first: running processes and network connections, then memory, then disk images or cloud snapshots, then logs and backups.", "Take cloud snapshots of the affected instances before isolating or rebuilding them."],
            ["Preserve and prove", "Work on copies. Hash every image, record who handled it and when, store evidence in a restricted location and keep notes of each action with a timestamp.", "Record times in UTC and note clock drift on each system."],
            ["Logs", "Copy authentication, cloud audit, DNS, proxy and endpoint logs now. Retention is {log_days} days, so anything older is already at risk of being lost.", "Look back past the first alert: attackers are often in earlier."],
            ["Scope and handover", "List accounts, keys and systems the attacker touched and rotate them after the evidence is safe. Brief legal before any notice or contact with the attacker.", "Write the timeline as you go and decide when to bring in an outside forensics firm."],
        ],
        "metrics": ["Days of log history left to review before the oldest rolls off|log_days - hours_since / 24|{:.1f}", "Evidence images needed at one per host|hosts * 2|{:,.0f}"],
    },
    "06-security-appsec/14-data-classification-advisor": {
        "fields": ["stores|Data stores reviewed|number|32", "restricted|Stores holding restricted data|number|6", "unencrypted|Restricted stores without encryption at rest|number|1", "no_owner|Stores without a data owner|number|9", "region|Data residency requirement|text|Customer data stays in the EU"],
        "sections": [
            ["Inventory", "Inventory: {input}", "{stores} stores, {restricted} hold restricted data, {no_owner} have no owner. Residency: {region}.", "Classification decides how much protection each dataset deserves, so you spend effort where harm would be greatest."],
            ["Four classes", "Public (no harm if shared), internal (business use), confidential (customer or commercial data) and restricted (payment, health, credentials, regulated personal data).", "Classify at the dataset level and mark the strictest column, rather than the whole system."],
            ["Controls by class", "Restricted: encryption at rest and in transit, named access with approval, field masking, full access logging and short retention. Confidential: role-based access and encryption. Internal: normal access. Public: integrity checks.", "{unencrypted} restricted store is not encrypted: fix that first."],
            ["Ownership", "Each store needs an owner who approves access and reviews it every quarter. Assign owners to the {no_owner} stores that have none.", "Tag data in the catalog so tools can enforce rules automatically."],
            ["Movement", "Check exports, backups, vendors and analytics copies. Data keeps its class when it is copied. Enforce the region rule: {region}.", "Scan for unexpected sensitive data in logs, tickets and shared drives."],
        ],
        "metrics": ["Share of stores with restricted data|restricted / stores|{:.0%}", "Stores that still need an owner|no_owner|{:,.0f}"],
    },
    "06-security-appsec/15-vendor-security-reviewer": {
        "fields": ["vendor|Vendor|text|MailPilot", "records|Customer records the vendor will hold|number|450000", "assurance|Assurance evidence|text|SOC 2 Type I, no recent penetration test", "breach_hours|Breach notice time in the contract (hours)|number|120", "required_hours|Breach notice time you require (hours)|number|72"],
        "sections": [
            ["Vendor", "Answers: {input}", "Vendor: {vendor}. Will hold {records} customer records. Evidence: {assurance}.", "Third-party risk is your risk. Rate it by what data the vendor holds and how badly its failure would hurt you."],
            ["Tier the vendor", "High tier if it holds restricted data, has access to production systems or is hard to replace. Apply more review to the high tier and less to the low.", "Reassess when the vendor's use grows."],
            ["Evidence", "Ask for a current SOC 2 Type II or ISO 27001 certificate, the scope of the audit, a recent penetration test summary and a list of subprocessors. Type I only shows design, not operation over time.", "Check that the audit scope covers the product you use."],
            ["Contract terms", "Breach notice in the contract is {breach_hours} hours against your requirement of {required_hours}. Negotiate notice time, data processing terms, audit rights, liability and a data return and deletion clause on exit.", "Confirm where data is stored and how it is encrypted."],
            ["Decision", "Approve, approve with conditions (with a dated remediation list) or reject. Record the reason and the review date.", "Review high-tier vendors every year and monitor for vendor breach news."],
        ],
        "metrics": ["Hours the contract is slower than your requirement|breach_hours - required_hours|{:+.0f}", "Records at risk per 1 percent of records exposed|records * 0.01|{:,.0f}"],
    },
    "06-security-appsec/16-phishing-report-triager": {
        "fields": ["recipients|Recipients|number|240", "clicked|People who clicked|number|12", "entered|People who entered credentials|number|3", "minutes_each|Minutes to handle one affected account|number|20", "domain|Lookalike domain|text|payr0ll-portal.example"],
        "sections": [
            ["Report", "Email: {input}", "{recipients} recipients, {clicked} clicked, {entered} entered credentials. Domain: {domain}.", "Treat any credential entry as a compromise until proven otherwise."],
            ["Verdict signals", "Lookalike domain, urgency, mismatch between displayed and real link, new sender, mismatched reply-to and authentication failures (SPF, DKIM, DMARC) all point to phishing.", "Detonate links and attachments in a sandbox, never on a work machine."],
            ["Immediate actions", "Reset passwords and revoke sessions and tokens for the {entered} accounts that entered credentials. Check their mail rules, forwarding and recent sign-ins. Block {domain} at the mail gateway, proxy and DNS.", "Contact the {clicked} who clicked to check for malware or other actions."],
            ["Purge and report", "Remove the message from all mailboxes, search for similar messages from the same sender or infrastructure and report the domain for takedown.", "Thank the person who reported it. Fast reporting is the behaviour you want."],
            ["Follow up", "Add indicators to detection rules, review multi-factor authentication coverage and use phishing-resistant methods (passkeys, security keys) for high-risk groups.", "Run training around real examples, and track click rate and report rate."],
        ],
        "metrics": ["Click rate|clicked / recipients|{:.1%}", "Credential entry rate among clickers|entered / clicked|{:.0%}", "Hours to handle the affected accounts|(clicked + entered) * minutes_each / 60|{:.1f}"],
    },
    "06-security-appsec/17-cloud-posture-reviewer": {
        "fields": ["public_buckets|Public storage buckets|number|3", "open_groups|Security groups open to the internet|number|14", "regions_no_logs|Regions with audit logging off|number|2", "regions|Regions in use|number|6", "root_mfa|Root account protected by MFA (yes or no)|text|No"],
        "sections": [
            ["Configuration", "Config: {input}", "{public_buckets} public buckets, {open_groups} internet-open groups, audit logging off in {regions_no_logs} of {regions} regions. Root MFA: {root_mfa}.", "Most cloud breaches come from misconfiguration, not from clever exploits."],
            ["Fix first", "Enable MFA on the root account and lock it away, block public access on storage unless a bucket is meant to be public and close management ports (SSH, RDP) to the internet.", "Check each open security group for a real reason, then restrict to known ranges or use a bastion or session manager."],
            ["Identity", "Use roles and short-lived credentials instead of long-lived keys, remove unused users and keys, and limit administrators. Review permissions with the access analyzer.", "Require MFA for all human users."],
            ["Logging and detection", "Turn on audit logging in every region and send logs to a separate, protected account. Enable flow logs and a threat-detection service and alert on high-risk events such as root login.", "{regions_no_logs} regions with logging off are blind spots attackers prefer."],
            ["Preventing drift", "Define infrastructure as code, scan it before deploy, apply guardrails (service control policies) and run a continuous posture scan with owners for each finding.", "Track open findings by age and severity."],
        ],
        "metrics": ["Share of regions without audit logging|regions_no_logs / regions|{:.0%}", "Exposures to fix first|public_buckets + open_groups|{:,.0f}"],
    },
    "06-security-appsec/18-security-training-planner": {
        "fields": ["staff|Staff|number|420", "engineers|Engineers|number|90", "click_rate|Phishing click rate (0 to 1)|number|0.11", "target_rate|Target click rate (0 to 1)|number|0.04", "minutes_year|Training minutes per person per year|number|90"],
        "sections": [
            ["Audience", "Profile: {input}", "{staff} staff, {engineers} engineers. Click rate {click_rate}, target {target_rate}.", "Training changes behaviour only when it is short, relevant and repeated. A yearly slide deck does not."],
            ["By role", "Everyone: phishing, passwords and MFA, reporting an incident. Engineers: secure coding and secrets handling. Support: identity checks and customer data handling. Finance: payment fraud and invoice scams.", "Tailor examples to each role's real work."],
            ["Cadence", "Onboarding session, short monthly lessons of 5 to 10 minutes, a yearly workshop for engineers and quarterly phishing simulations followed by instant feedback.", "Total time is about {minutes_year} minutes per person per year."],
            ["Culture", "Make reporting easy (one button) and blame-free. Celebrate reports and never punish those who click. People who fear blame stop reporting.", "Share anonymised stories of real incidents."],
            ["Measures", "Track click rate, report rate (should rise), time to report, repeat clickers and incidents caused by user error. Completion rate alone says little.", "Review results quarterly and change the content that does not move the numbers."],
        ],
        "metrics": ["Click rate reduction needed|(click_rate - target_rate) / click_rate|{:.0%}", "People who clicked at the current rate|staff * click_rate|{:,.0f}", "Training hours per year for everyone|staff * minutes_year / 60|{:,.0f}"],
    },
    "06-security-appsec/19-crypto-usage-reviewer": {
        "fields": ["use_case|Use case|text|Password storage and session tokens", "users|Users whose data is protected|number|250000", "attempts_s|Offline guesses per second an attacker can make|number|10000000000", "token_values|Possible token values|number|1048576", "token_ttl_h|Token lifetime (hours)|number|24"],
        "sections": [
            ["Code", "Snippet: {input}", "Use case: {use_case}. Protects {users} users.", "Do not invent cryptography. Use the platform's reviewed library with its safe defaults."],
            ["Passwords", "Never store passwords with MD5 or SHA-1, or with a fast hash of any kind. Use a slow, salted password hash (Argon2id, scrypt or bcrypt) with a work factor tuned to about 250 ms.", "At {attempts_s} guesses per second a fast hash falls in minutes."],
            ["Keys and secrets", "No keys in source code or images. Keep them in a key management service, give each environment its own key and rotate on a schedule and after any exposure.", "Encrypt with envelope keys so you can rotate without re-encrypting everything at once."],
            ["Randomness", "Use a cryptographically secure generator for tokens, never a general random function. A token with only {token_values} possible values is guessable. Use at least 128 bits of randomness.", "Expire tokens ({token_ttl_h} hours here) and bind them to the session."],
            ["Modes and integrity", "Use authenticated encryption (AES-GCM or ChaCha20-Poly1305) with a unique nonce for every message. ECB leaks patterns and no mode without authentication stops tampering.", "Compare secrets with a constant-time function and use TLS 1.2 or newer for transport."],
        ],
        "metrics": ["Seconds for an attacker to try every token|token_values / attempts_s|{:.6f}", "Chance one random guess hits a given token|1 / token_values|{:.6%}"],
    },
    "06-security-appsec/20-bug-bounty-triager": {
        "fields": ["finding|Finding type|text|Stored XSS in profile bio", "cvss|Severity score (CVSS)|number|6.1", "reports_month|Reports received per month|number|85", "valid_share|Share of reports that are valid (0 to 1)|number|0.18", "reward_usd|Reward for this severity (USD)|number|1500"],
        "sections": [
            ["Report", "Report: {input}", "Finding: {finding}. Severity score {cvss}.", "Triage must be fast and fair: researchers who get a quick, polite answer keep sending good reports."],
            ["Validate", "Reproduce with the researcher's steps in a test account, confirm the asset is in scope and check whether the issue is a duplicate, a known accepted risk or only a theoretical one.", "Ask for missing steps in one clear message and not several."],
            ["Rate severity", "Rate by real impact and ease: who can attack it, what they gain and how much user action is needed. Stored XSS in a profile field that other users view can lead to account takeover.", "Use CVSS as a start, then adjust for your own context and compensating controls."],
            ["Respond and reward", "Acknowledge within a day, give a verdict within a week and pay the tier for the severity: {reward_usd} USD here. Pay duplicates nothing but thank the researcher.", "Explain any downgrade, with evidence."],
            ["Fix and learn", "Fix by output encoding and a content security policy, then search for the same flaw class across the code. Credit the researcher if they agree and track time to fix per severity.", "Feed each report into your test suite."],
        ],
        "metrics": ["Valid reports per month|reports_month * valid_share|{:,.0f}", "Estimated monthly payout at this tier (USD)|reports_month * valid_share * reward_usd|${:,.0f}"],
    },
}
