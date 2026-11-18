# FinOps & Cloud Cost

FinOps & Cloud Cost suite of 10 focused autonomous agents in Valkyrie AI Agent Studio.

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
