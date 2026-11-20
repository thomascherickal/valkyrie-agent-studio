# FinOps & Cloud Cost

FinOps & Cloud Cost suite of 20 focused autonomous agents in Valkyrie Agent Studio.

## Engine Policy
- **Default:** `gemini-4-hydrogen` (`thinking_level: low`, `high` optional per agent)
- **Free-First Fallback:** `opencode_free` -> `openrouter_free` -> `ollama` (`qwen3.5:latest`)

## Focused Agents
- `01-cloud-bill-anomaly` — **Cloud Bill Anomaly Detector**: Detects daily spend spikes by service, region, and cost-center tag. (Tool: `detect_spend_spike`)
- `02-k8s-rightsizing-advisor` — **K8s Rightsizing Advisor**: Compares requested vs p95 actual CPU/RAM to trim cluster waste. (Tool: `compute_rightsize`)
- `03-idle-resource-reaper` — **Idle Resource Reaper**: Lists unattached EBS volumes, idle load balancers, and zombie VMs. (Tool: `flag_idle_assets`)
- `04-ri-savings-planner` — **RI & Savings Plan Advisor**: Models 1-year no-upfront Savings Plan coverage for steady baselines. (Tool: `model_commitment_roi`)
- `05-llm-token-optimizer` — **LLM Token Optimizer**: Routes simple tasks to gemini-4-hydrogen (low) and trims prompt bloat. (Tool: `recommend_model_tier`)
- `06-egress-cost-reducer` — **Egress Cost Reducer**: Identifies cross-AZ chatty services and missing VPC endpoints. (Tool: `find_egress_leaks`)
- `07-storage-tiering-planner` — **Storage Tiering Planner**: Recommends S3 Intelligent-Tiering and Glacier lifecycle rules. (Tool: `design_lifecycle_rule`)
- `08-unit-economics-tracker` — **Unit Economics Tracker**: Calculates COGS per active tenant and per 1,000 agent invocations. (Tool: `calc_unit_cogs`)
- `09-budget-alert-router` — **Budget Alert Router**: Routes forecasted monthly overruns to squad Slack/email owners. (Tool: `route_budget_warning`)
- `10-finops-monthly-brief` — **FinOps Monthly Brief**: Summarizes cloud spend variance, realized savings, and unit margins. (Tool: `compile_finops_brief`)
- `11-commitment-coverage-checker` — **Commitment Coverage Checker**: Checks reserved capacity and savings plan coverage and utilization against steady usage. (Tool: `check_commitment_coverage`)
- `12-spot-instance-advisor` — **Spot Instance Advisor**: Assesses which workloads can run on spot capacity and designs interruption handling. (Tool: `assess_spot_fit`)
- `13-cross-az-traffic-analyst` — **Cross-AZ Traffic Analyst**: Analyzes cross-zone and cross-region data transfer and proposes locality fixes. (Tool: `analyze_az_traffic`)
- `14-tagging-policy-auditor` — **Tagging Policy Auditor**: Audits cloud resource tags for cost allocation coverage, consistency, and owner accuracy. (Tool: `audit_tags`)
- `15-chargeback-allocator` — **Chargeback Allocator**: Allocates shared cloud and platform costs to teams with fair, explainable drivers. (Tool: `allocate_shared_cost`)
- `16-database-cost-tuner` — **Database Cost Tuner**: Tunes managed database cost by sizing, storage, replicas, backups, and idle environments. (Tool: `tune_db_cost`)
- `17-observability-cost-reducer` — **Observability Cost Reducer**: Reduces logging, metrics, and tracing cost without losing the signals teams need. (Tool: `trim_telemetry_cost`)
- `18-forecast-variance-explainer` — **Forecast Variance Explainer**: Explains cloud cost variance against forecast by volume, price, mix, and one-off effects. (Tool: `explain_cost_variance`)
- `19-saas-license-optimizer` — **SaaS License Optimizer**: Optimizes SaaS seats and tiers using activity data, role needs, and renewal dates. (Tool: `optimize_seats`)
- `20-gpu-utilization-analyst` — **GPU Utilization Analyst**: Analyzes GPU utilization and queueing to cut idle accelerator spend and fix scheduling. (Tool: `analyze_gpu_use`)
