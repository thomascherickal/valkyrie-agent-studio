# DevOps & SRE

DevOps & SRE suite of 10 focused autonomous agents in Valkyrie AI Agent Studio.

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
