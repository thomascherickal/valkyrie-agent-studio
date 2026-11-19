# DevOps & SRE

DevOps & SRE suite of 20 focused autonomous agents in Valkyrie AI Agent Studio.

## Engine Policy
- **Default:** `gemini-4-hydrogen` (`thinking_level: low`, `high` optional per agent)
- **Free-First Fallback:** `opencode_free` -> `openrouter_free` -> `ollama` (`qwen3.5:latest`)

## Focused Agents
- `01-incident-commander` — **Incident Commander**: Structures SEV-1/SEV-2 triage roles, timelines, and mitigation actions. (Tool: `build_ics_timeline`)
- `02-postmortem-author` — **Postmortem Author**: Drafts blameless RCAs with 5-Whys and SMART remediation tickets. (Tool: `generate_five_whys`)
- `03-terraform-reviewer` — **Terraform Reviewer**: Flags destructive resource replacements and wildcard IAM policies in plans. (Tool: `inspect_tf_blast`)
- `04-k8s-manifest-linter` — **Kubernetes Manifest Linter**: Checks deployments for missing probes, limits, and PodDisruptionBudgets. (Tool: `lint_k8s_spec`)
- `05-slo-burn-monitor` — **SLO Burn Rate Monitor**: Computes multi-window error budget burn rates and alert severities. (Tool: `calc_burn_rate`)
- `06-ci-pipeline-optimizer` — **CI Pipeline Optimizer**: Pinpoints serial bottlenecks and cache misses in GitHub Actions workflows. (Tool: `optimize_dag`)
- `07-capacity-planner` — **Capacity Planner**: Projects compute and memory headroom from peak QPS growth curves. (Tool: `model_headroom`)
- `08-runbook-generator` — **Runbook Generator**: Generates step-by-step diagnostic commands and rollback steps for alerts. (Tool: `compile_runbook`)
- `09-chaos-test-designer` — **Chaos Test Designer**: Defines steady-state hypotheses and blast-radius bounds for fault drills. (Tool: `design_chaos_drill`)
- `10-rollback-verifier` — **Rollback Verifier**: Evaluates canary error/latency deltas to trigger automated rollbacks. (Tool: `eval_canary_gate`)
- `11-oncall-load-analyzer` — **On-Call Load Analyzer**: Analyzes pager load per person and per service to keep on-call sustainable. (Tool: `analyze_oncall_load`)
- `12-alert-noise-reducer` — **Alert Noise Reducer**: Ranks noisy alerts by page count and action rate and proposes tuning or deletion. (Tool: `rank_noisy_alerts`)
- `13-dr-plan-reviewer` — **Disaster Recovery Reviewer**: Reviews disaster recovery plans against RTO, RPO, backups, dependencies, and test evidence. (Tool: `review_dr_plan`)
- `14-helm-chart-reviewer` — **Helm Chart Reviewer**: Reviews Helm values and templates for safe defaults, resource limits, and upgrade risks. (Tool: `review_helm_values`)
- `15-secret-rotation-planner` — **Secrets Rotation Planner**: Plans secret rotation by age, blast radius, and ownership with zero-downtime steps. (Tool: `plan_secret_rotation`)
- `16-blast-radius-mapper` — **Dependency Outage Mapper**: Maps which services fail when a dependency fails and ranks single points of failure. (Tool: `map_blast_radius`)
- `17-deploy-freeze-advisor` — **Deploy Freeze Advisor**: Decides whether to freeze deploys using change risk, error budget, and the event calendar. (Tool: `decide_freeze`)
- `18-log-retention-tuner` — **Log Retention Tuner**: Tunes log retention by value, compliance need, and storage cost per log class. (Tool: `tune_log_retention`)
- `19-dns-change-verifier` — **DNS Change Verifier**: Checks planned DNS changes for TTLs, propagation risk, records, and rollback readiness. (Tool: `verify_dns_change`)
- `20-error-budget-policy-writer` — **Error Budget Policy Writer**: Drafts error budget policies with thresholds, release rules, and escalation paths. (Tool: `draft_budget_policy`)
