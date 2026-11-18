import type { RoleCatalog } from "../types";

export const ROLE_05: RoleCatalog = {
  "id": "05-data-engineering",
  "name": "Data Engineering",
  "agents": [
    {
      "id": "01-etl-pipeline-designer",
      "name": "ETL Pipeline Designer",
      "description": "Designs idempotent partition-aware ingestion DAGs with dead-letter queues.",
      "tool": "design_idempotent_dag",
      "inputKey": "source_spec",
      "outputKey": "dag_spec",
      "sampleInput": "Hourly Stripe webhook events -> BigQuery raw_events"
    },
    {
      "id": "02-dbt-model-generator",
      "name": "dbt Model Generator",
      "description": "Generates staging/mart SQL models and schema.yml not-null/unique tests.",
      "tool": "emit_dbt_model",
      "inputKey": "table_contract",
      "outputKey": "dbt_files",
      "sampleInput": "stg_orders(order_id, customer_id, total_cents, created_at)"
    },
    {
      "id": "03-schema-drift-detector",
      "name": "Schema Drift Detector",
      "description": "Diffs upstream JSON/Avro schemas and flags breaking column removals.",
      "tool": "analyze_schema_drift",
      "inputKey": "schema_diff",
      "outputKey": "drift_alert",
      "sampleInput": "Removed column: user_tier; Added: plan_code (nullable)"
    },
    {
      "id": "04-data-quality-guardian",
      "name": "Data Quality Guardian",
      "description": "Defines freshness SLAs, row-count bounds, and referential checks.",
      "tool": "build_dq_assertions",
      "inputKey": "dataset_profile",
      "outputKey": "dq_rules",
      "sampleInput": "fact_invoices: ~120k rows/day, 0% null invoice_id"
    },
    {
      "id": "05-warehouse-cost-tuner",
      "name": "Warehouse Cost Tuner",
      "description": "Optimizes table partitioning, clustering keys, and slot autoscaling.",
      "tool": "recommend_clustering",
      "inputKey": "query_telemetry",
      "outputKey": "cost_savings",
      "sampleInput": "Full table scan on 4TB events_log filtering by event_date"
    },
    {
      "id": "06-lineage-documenter",
      "name": "Lineage Documenter",
      "description": "Traces column-level provenance from raw ingestion to BI metrics.",
      "tool": "trace_column_lineage",
      "inputKey": "sql_graph",
      "outputKey": "lineage_map",
      "sampleInput": "mart_arr derives from dim_subs + fct_payments"
    },
    {
      "id": "07-pii-redaction-planner",
      "name": "PII Redaction Planner",
      "description": "Detects email/SSN/IP columns and applies deterministic hashing policies.",
      "tool": "classify_pii_columns",
      "inputKey": "columns_list",
      "outputKey": "masking_policy",
      "sampleInput": "email, ip_address, billing_zip, plan_id"
    },
    {
      "id": "08-backfill-orchestrator",
      "name": "Backfill Orchestrator",
      "description": "Splits multi-year backfills into safe rate-limited date chunks.",
      "tool": "chunk_date_windows",
      "inputKey": "backfill_window",
      "outputKey": "backfill_plan",
      "sampleInput": "2024-01-01 to 2026-11-01, max 4 concurrent workers"
    },
    {
      "id": "09-streaming-lag-analyst",
      "name": "Streaming Lag Analyst",
      "description": "Diagnoses Kafka consumer lag spikes, skew, and rebalance storms.",
      "tool": "diagnose_partition_skew",
      "inputKey": "consumer_metrics",
      "outputKey": "lag_remediation",
      "sampleInput": "Partition 3 lag: 450k msgs; Partitions 0-2 lag: 120 msgs"
    },
    {
      "id": "10-metric-layer-definer",
      "name": "Metric Layer Definer",
      "description": "Standardizes canonical NRR, MRR, and active-user YAML definitions.",
      "tool": "define_semantic_metric",
      "inputKey": "kpi_request",
      "outputKey": "metric_yaml",
      "sampleInput": "Net Revenue Retention trailing 12 months by cohort"
    }
  ]
};
