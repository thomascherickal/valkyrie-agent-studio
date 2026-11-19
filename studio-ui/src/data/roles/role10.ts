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
    },
    {
      "id": "11-commitment-coverage-checker",
      "name": "Commitment Coverage Checker",
      "description": "Checks reserved capacity and savings plan coverage and utilization against steady usage.",
      "tool": "check_commitment_coverage",
      "inputKey": "usage_summary",
      "outputKey": "coverage_report",
      "sampleInput": "Compute 410k a month on demand; commitments cover 52%, utilization 97%; baseline steady 70% of spend"
    },
    {
      "id": "12-spot-instance-advisor",
      "name": "Spot Instance Advisor",
      "description": "Assesses which workloads can run on spot capacity and designs interruption handling.",
      "tool": "assess_spot_fit",
      "inputKey": "workload_profile",
      "outputKey": "spot_plan",
      "sampleInput": "Batch ETL 120 vCPU nightly, CI runners 60 vCPU, stateless API 200 vCPU; interruptions tolerated for batch and CI"
    },
    {
      "id": "13-cross-az-traffic-analyst",
      "name": "Cross-AZ Traffic Analyst",
      "description": "Analyzes cross-zone and cross-region data transfer and proposes locality fixes.",
      "tool": "analyze_az_traffic",
      "inputKey": "traffic_matrix",
      "outputKey": "az_plan",
      "sampleInput": "Service mesh sends 62% of traffic across zones; Kafka replication 140 TB/month; one analytics job crosses regions"
    },
    {
      "id": "14-tagging-policy-auditor",
      "name": "Tagging Policy Auditor",
      "description": "Audits cloud resource tags for cost allocation coverage, consistency, and owner accuracy.",
      "tool": "audit_tags",
      "inputKey": "resource_tags",
      "outputKey": "tag_report",
      "sampleInput": "12,400 resources: 71% have owner, 58% have cost-center, 9 spellings of environment, 3.1k untagged by spend"
    },
    {
      "id": "15-chargeback-allocator",
      "name": "Chargeback Allocator",
      "description": "Allocates shared cloud and platform costs to teams with fair, explainable drivers.",
      "tool": "allocate_shared_cost",
      "inputKey": "shared_costs",
      "outputKey": "allocation_table",
      "sampleInput": "Shared Kubernetes 84k, networking 31k, observability 52k, support 19k a month; 6 product teams"
    },
    {
      "id": "16-database-cost-tuner",
      "name": "Database Cost Tuner",
      "description": "Tunes managed database cost by sizing, storage, replicas, backups, and idle environments.",
      "tool": "tune_db_cost",
      "inputKey": "db_usage",
      "outputKey": "db_savings",
      "sampleInput": "3 production clusters at 18% CPU, provisioned IOPS 4x used, 9 dev databases running 24/7, backups kept 90 days"
    },
    {
      "id": "17-observability-cost-reducer",
      "name": "Observability Cost Reducer",
      "description": "Reduces logging, metrics, and tracing cost without losing the signals teams need.",
      "tool": "trim_telemetry_cost",
      "inputKey": "telemetry_volumes",
      "outputKey": "telemetry_plan",
      "sampleInput": "Logs 38 TB/month, 2.4M active metric series (40% unused), traces sampled at 100%, vendor bill 96k a month"
    },
    {
      "id": "18-forecast-variance-explainer",
      "name": "Forecast Variance Explainer",
      "description": "Explains cloud cost variance against forecast by volume, price, mix, and one-off effects.",
      "tool": "explain_cost_variance",
      "inputKey": "actual_vs_forecast",
      "outputKey": "variance_story",
      "sampleInput": "Forecast 1.20M, actual 1.38M (+15%); traffic +9%, new region launch, one-off 40k migration; reservation discount lower than planned"
    },
    {
      "id": "19-saas-license-optimizer",
      "name": "SaaS License Optimizer",
      "description": "Optimizes SaaS seats and tiers using activity data, role needs, and renewal dates.",
      "tool": "optimize_seats",
      "inputKey": "license_usage",
      "outputKey": "seat_plan",
      "sampleInput": "CRM 480 seats, 61% active in 90 days; design tool 120 seats, 38 never opened; renewal in 70 days"
    },
    {
      "id": "20-gpu-utilization-analyst",
      "name": "GPU Utilization Analyst",
      "description": "Analyzes GPU utilization and queueing to cut idle accelerator spend and fix scheduling.",
      "tool": "analyze_gpu_use",
      "inputKey": "gpu_metrics",
      "outputKey": "gpu_plan",
      "sampleInput": "64 GPUs, average utilization 31%, jobs queue for 3 hours at peak, 22% of GPU-hours are idle between jobs"
    }
  ]
};
