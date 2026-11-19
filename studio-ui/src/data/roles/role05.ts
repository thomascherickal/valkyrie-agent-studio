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
    },
    {
      "id": "11-cdc-pipeline-designer",
      "name": "CDC Pipeline Designer",
      "description": "Designs change data capture pipelines from operational databases into the warehouse.",
      "tool": "design_cdc_flow",
      "inputKey": "source_tables",
      "outputKey": "cdc_design",
      "sampleInput": "Postgres orders (4M rows, 300 updates/s peak), customers, payments; target warehouse within 5 minutes"
    },
    {
      "id": "12-data-contract-author",
      "name": "Data Contract Author",
      "description": "Drafts data contracts with schema, semantics, quality rules, ownership, and change process.",
      "tool": "draft_data_contract",
      "inputKey": "dataset_spec",
      "outputKey": "contract_doc",
      "sampleInput": "orders_daily: one row per order, order_id unique, amount in cents, refreshed by 06:00 UTC, owner Payments"
    },
    {
      "id": "13-partition-strategy-advisor",
      "name": "Partition Strategy Advisor",
      "description": "Chooses partition keys, sizes, and pruning rules from table and query profiles.",
      "tool": "choose_partitioning",
      "inputKey": "table_profile",
      "outputKey": "partition_plan",
      "sampleInput": "events: 6 TB, 2.1B rows, 90% of queries filter on the last 7 days and customer_id"
    },
    {
      "id": "14-dedup-strategy-designer",
      "name": "Deduplication Strategy Designer",
      "description": "Designs deduplication rules for events and records with keys, windows, and survivorship.",
      "tool": "design_dedup",
      "inputKey": "duplicate_report",
      "outputKey": "dedup_plan",
      "sampleInput": "Events table: 3.4% duplicate event_ids from client retries; customers: 11% near-duplicate names and emails"
    },
    {
      "id": "15-scd-modeler",
      "name": "Slowly Changing Dimension Modeler",
      "description": "Models slowly changing dimensions with type choice, keys, effective dates, and load logic.",
      "tool": "model_scd",
      "inputKey": "dimension_changes",
      "outputKey": "scd_design",
      "sampleInput": "Customer tier changes ~8% of customers a month; reports need revenue by the tier at the time of sale"
    },
    {
      "id": "16-dag-migration-planner",
      "name": "Orchestrator Migration Planner",
      "description": "Plans migration of legacy jobs to a modern orchestrator with parity checks and cutover waves.",
      "tool": "plan_dag_migration",
      "inputKey": "legacy_jobs",
      "outputKey": "migration_plan",
      "sampleInput": "420 cron jobs on 6 servers, 60 with hidden dependencies, nightly batch window 5 hours, moving to Airflow"
    },
    {
      "id": "17-feature-store-reviewer",
      "name": "Feature Store Reviewer",
      "description": "Reviews feature definitions for training and serving skew, leakage, freshness, and reuse.",
      "tool": "review_feature_store",
      "inputKey": "feature_specs",
      "outputKey": "store_review",
      "sampleInput": "user_30d_spend computed in SQL for training, recomputed in the service for serving; refreshed nightly"
    },
    {
      "id": "18-data-retention-planner",
      "name": "Data Retention Planner",
      "description": "Plans retention and deletion schedules by dataset class, purpose, law, and storage cost.",
      "tool": "plan_retention",
      "inputKey": "dataset_catalog",
      "outputKey": "retention_plan",
      "sampleInput": "Clickstream 80 TB/yr kept forever, invoices 7 yrs required, support chats with personal data kept forever"
    },
    {
      "id": "19-sql-style-reviewer",
      "name": "SQL Style Reviewer",
      "description": "Reviews SQL for readability, correctness traps, join risks, and maintainable structure.",
      "tool": "review_sql_style",
      "inputKey": "sql_excerpt",
      "outputKey": "sql_review",
      "sampleInput": "SELECT * FROM orders o, customers c WHERE o.cid = c.id AND created > '2025-01-01' ORDER BY 1"
    },
    {
      "id": "20-catalog-documenter",
      "name": "Data Catalog Documenter",
      "description": "Writes data catalog entries with definitions, lineage, quality status, and access guidance.",
      "tool": "document_dataset",
      "inputKey": "table_metadata",
      "outputKey": "catalog_entry",
      "sampleInput": "fct_subscriptions: one row per subscription per month, columns mrr, plan_id, started_at, churned_at"
    }
  ]
};
