import type { RoleCatalog } from "../types";

export const ROLE_03: RoleCatalog = {
  "id": "03-devops-sre",
  "name": "DevOps & SRE",
  "agents": [
    {
      "id": "01-incident-commander",
      "name": "Incident Commander",
      "description": "Structures SEV-1/SEV-2 triage roles, timelines, and mitigation actions.",
      "tool": "build_ics_timeline",
      "inputKey": "alert_payload",
      "outputKey": "command_plan",
      "sampleInput": "SEV-1: API 5xx rate 18% in us-east-1 after deploy #412"
    },
    {
      "id": "02-postmortem-author",
      "name": "Postmortem Author",
      "description": "Drafts blameless RCAs with 5-Whys and SMART remediation tickets.",
      "tool": "generate_five_whys",
      "inputKey": "incident_log",
      "outputKey": "postmortem_md",
      "sampleInput": "Redis OOM caused by unbounded session keys during promo spike"
    },
    {
      "id": "03-terraform-reviewer",
      "name": "Terraform Reviewer",
      "description": "Flags destructive resource replacements and wildcard IAM policies in plans.",
      "tool": "inspect_tf_blast",
      "inputKey": "tf_plan_diff",
      "outputKey": "tf_verdict",
      "sampleInput": "+/- aws_rds_cluster.main (forces replacement), iam:*"
    },
    {
      "id": "04-k8s-manifest-linter",
      "name": "Kubernetes Manifest Linter",
      "description": "Checks deployments for missing probes, limits, and PodDisruptionBudgets.",
      "tool": "lint_k8s_spec",
      "inputKey": "k8s_yaml",
      "outputKey": "lint_findings",
      "sampleInput": "kind: Deployment, replicas: 3, resources: {}, livenessProbe: null"
    },
    {
      "id": "05-slo-burn-monitor",
      "name": "SLO Burn Rate Monitor",
      "description": "Computes multi-window error budget burn rates and alert severities.",
      "tool": "calc_burn_rate",
      "inputKey": "sli_metrics",
      "outputKey": "paging_decision",
      "sampleInput": "SLO: 99.9%, 1h error rate: 1.2%, remaining budget: 18%"
    },
    {
      "id": "06-ci-pipeline-optimizer",
      "name": "CI Pipeline Optimizer",
      "description": "Pinpoints serial bottlenecks and cache misses in GitHub Actions workflows.",
      "tool": "optimize_dag",
      "inputKey": "ci_timings",
      "outputKey": "pipeline_savings",
      "sampleInput": "npm install: 4m, cargo build: 9m (no sccache), pytest: 1m"
    },
    {
      "id": "07-capacity-planner",
      "name": "Capacity Planner",
      "description": "Projects compute and memory headroom from peak QPS growth curves.",
      "tool": "model_headroom",
      "inputKey": "traffic_forecast",
      "outputKey": "scaling_plan",
      "sampleInput": "Current: 4k QPS @ 62% CPU; Q4 forecast: 9.5k QPS"
    },
    {
      "id": "08-runbook-generator",
      "name": "Runbook Generator",
      "description": "Generates step-by-step diagnostic commands and rollback steps for alerts.",
      "tool": "compile_runbook",
      "inputKey": "alert_rule",
      "outputKey": "runbook_md",
      "sampleInput": "HighPostgresConnections > 85% for 5m"
    },
    {
      "id": "09-chaos-test-designer",
      "name": "Chaos Test Designer",
      "description": "Defines steady-state hypotheses and blast-radius bounds for fault drills.",
      "tool": "design_chaos_drill",
      "inputKey": "target_service",
      "outputKey": "chaos_spec",
      "sampleInput": "Payment gateway failover to secondary region"
    },
    {
      "id": "10-rollback-verifier",
      "name": "Rollback Verifier",
      "description": "Evaluates canary error/latency deltas to trigger automated rollbacks.",
      "tool": "eval_canary_gate",
      "inputKey": "canary_stats",
      "outputKey": "rollback_action",
      "sampleInput": "Canary p99: 420ms vs Baseline p99: 95ms"
    }
  ]
};
