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
    },
    {
      "id": "11-oncall-load-analyzer",
      "name": "On-Call Load Analyzer",
      "description": "Analyzes pager load per person and per service to keep on-call sustainable.",
      "tool": "analyze_oncall_load",
      "inputKey": "pager_stats",
      "outputKey": "oncall_report",
      "sampleInput": "Last 4 weeks: 212 pages, 61 outside working hours, 9 engineers in rotation, top service 74 pages"
    },
    {
      "id": "12-alert-noise-reducer",
      "name": "Alert Noise Reducer",
      "description": "Ranks noisy alerts by page count and action rate and proposes tuning or deletion.",
      "tool": "rank_noisy_alerts",
      "inputKey": "alert_history",
      "outputKey": "noise_plan",
      "sampleInput": "CPUHigh fired 310 times, 4 led to action; DiskSlow 95 times, 60 actioned; QueueLag 40 times, 38 actioned"
    },
    {
      "id": "13-dr-plan-reviewer",
      "name": "Disaster Recovery Reviewer",
      "description": "Reviews disaster recovery plans against RTO, RPO, backups, dependencies, and test evidence.",
      "tool": "review_dr_plan",
      "inputKey": "dr_plan",
      "outputKey": "dr_gaps",
      "sampleInput": "Primary region us-east-1, nightly backups to the same region, restore never tested, RTO 4h, RPO 1h"
    },
    {
      "id": "14-helm-chart-reviewer",
      "name": "Helm Chart Reviewer",
      "description": "Reviews Helm values and templates for safe defaults, resource limits, and upgrade risks.",
      "tool": "review_helm_values",
      "inputKey": "helm_values",
      "outputKey": "chart_review",
      "sampleInput": "replicaCount: 1; image.tag: latest; resources: {}; ingress.enabled: true; no podDisruptionBudget"
    },
    {
      "id": "15-secret-rotation-planner",
      "name": "Secrets Rotation Planner",
      "description": "Plans secret rotation by age, blast radius, and ownership with zero-downtime steps.",
      "tool": "plan_secret_rotation",
      "inputKey": "secret_inventory",
      "outputKey": "rotation_plan",
      "sampleInput": "86 secrets: 23 older than 1 year, 9 shared by several services, 14 database passwords, no owner on 11"
    },
    {
      "id": "16-blast-radius-mapper",
      "name": "Dependency Outage Mapper",
      "description": "Maps which services fail when a dependency fails and ranks single points of failure.",
      "tool": "map_blast_radius",
      "inputKey": "service_map",
      "outputKey": "outage_map",
      "sampleInput": "auth-service is called by 14 services; 6 have no cache or fallback; it runs in one region"
    },
    {
      "id": "17-deploy-freeze-advisor",
      "name": "Deploy Freeze Advisor",
      "description": "Decides whether to freeze deploys using change risk, error budget, and the event calendar.",
      "tool": "decide_freeze",
      "inputKey": "change_calendar",
      "outputKey": "freeze_decision",
      "sampleInput": "Black Friday week, 31 changes queued, error budget 38% left, two incidents last week"
    },
    {
      "id": "18-log-retention-tuner",
      "name": "Log Retention Tuner",
      "description": "Tunes log retention by value, compliance need, and storage cost per log class.",
      "tool": "tune_log_retention",
      "inputKey": "log_volumes",
      "outputKey": "retention_policy",
      "sampleInput": "Audit logs 2 TB/month kept 7 years, app logs 40 TB/month kept 90 days, debug 25 TB/month kept 30 days"
    },
    {
      "id": "19-dns-change-verifier",
      "name": "DNS Change Verifier",
      "description": "Checks planned DNS changes for TTLs, propagation risk, records, and rollback readiness.",
      "tool": "verify_dns_change",
      "inputKey": "dns_change",
      "outputKey": "dns_checklist",
      "sampleInput": "Move api.example.com from the old load balancer to the new one; current TTL 3600; mail records unchanged"
    },
    {
      "id": "20-error-budget-policy-writer",
      "name": "Error Budget Policy Writer",
      "description": "Drafts error budget policies with thresholds, release rules, and escalation paths.",
      "tool": "draft_budget_policy",
      "inputKey": "slo_context",
      "outputKey": "budget_policy",
      "sampleInput": "Checkout API SLO 99.9% over 30 days; product wants weekly releases; last month used 80% of budget"
    }
  ]
};
