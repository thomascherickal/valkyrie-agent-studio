import type { RoleCatalog } from "../types";

export const ROLE_10: RoleCatalog = {
  "id": "10-finops-cloud-cost",
  "name": "FinOps & Cloud Cost",
  "agents": [
    {
      "id": "01-cloud-bill-anomaly",
      "name": "Cloud Bill Anomaly Detector",
      "description": "Detects daily spend spikes by service, region, and cost-center tag.",
      "tool": "detect_spend_spike",
      "inputKey": "daily_spend",
      "outputKey": "anomaly_alert",
      "sampleInput": "NAT Gateway us-east-1 jumped from $42/day to $610/day"
    },
    {
      "id": "02-k8s-rightsizing-advisor",
      "name": "K8s Rightsizing Advisor",
      "description": "Compares requested vs p95 actual CPU/RAM to trim cluster waste.",
      "tool": "compute_rightsize",
      "inputKey": "pod_metrics",
      "outputKey": "rightsize_patch",
      "sampleInput": "worker-api requests 4 vCPU, p95 usage 0.45 vCPU"
    },
    {
      "id": "03-idle-resource-reaper",
      "name": "Idle Resource Reaper",
      "description": "Lists unattached EBS volumes, idle load balancers, and zombie VMs.",
      "tool": "flag_idle_assets",
      "inputKey": "infra_inventory",
      "outputKey": "reap_candidates",
      "sampleInput": "14 unattached gp3 volumes (2.8 TB), 3 idle ALBs"
    },
    {
      "id": "04-ri-savings-planner",
      "name": "RI & Savings Plan Advisor",
      "description": "Models 1-year no-upfront Savings Plan coverage for steady baselines.",
      "tool": "model_commitment_roi",
      "inputKey": "compute_baseline",
      "outputKey": "savings_plan",
      "sampleInput": "Steady 120 vCPU baseline; currently 100% On-Demand ($4.1k/mo)"
    },
    {
      "id": "05-llm-token-optimizer",
      "name": "LLM Token Optimizer",
      "description": "Routes simple tasks to gemini-4-hydrogen (low) and trims prompt bloat.",
      "tool": "recommend_model_tier",
      "inputKey": "llm_usage",
      "outputKey": "token_savings",
      "sampleInput": "Using high-effort model ($15/1M) for JSON classification"
    },
    {
      "id": "06-egress-cost-reducer",
      "name": "Egress Cost Reducer",
      "description": "Identifies cross-AZ chatty services and missing VPC endpoints.",
      "tool": "find_egress_leaks",
      "inputKey": "network_flow",
      "outputKey": "network_fixes",
      "sampleInput": "18 TB/mo cross-AZ traffic between app and S3 without gateway endpoint"
    },
    {
      "id": "07-storage-tiering-planner",
      "name": "Storage Tiering Planner",
      "description": "Recommends S3 Intelligent-Tiering and Glacier lifecycle rules.",
      "tool": "design_lifecycle_rule",
      "inputKey": "bucket_stats",
      "outputKey": "storage_savings",
      "sampleInput": "45 TB logs older than 90 days stored in S3 Standard"
    },
    {
      "id": "08-unit-economics-tracker",
      "name": "Unit Economics Tracker",
      "description": "Calculates COGS per active tenant and per 1,000 agent invocations.",
      "tool": "calc_unit_cogs",
      "inputKey": "cogs_inputs",
      "outputKey": "unit_economics",
      "sampleInput": "Monthly infra $3,200, LLM $480, 1.6M runs, 400 tenants"
    },
    {
      "id": "09-budget-alert-router",
      "name": "Budget Alert Router",
      "description": "Routes forecasted monthly overruns to squad Slack/email owners.",
      "tool": "route_budget_warning",
      "inputKey": "budget_status",
      "outputKey": "alert_payload",
      "sampleInput": "Team Data-Eng at 88% of monthly budget on day 14"
    },
    {
      "id": "10-finops-monthly-brief",
      "name": "FinOps Monthly Brief",
      "description": "Summarizes cloud spend variance, realized savings, and unit margins.",
      "tool": "compile_finops_brief",
      "inputKey": "monthly_ledger",
      "outputKey": "monthly_report",
      "sampleInput": "Total $24.5k (-9% MoM), Savings realized $4.2k"
    }
  ]
};
