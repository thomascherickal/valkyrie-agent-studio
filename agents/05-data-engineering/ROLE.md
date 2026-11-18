# Data Engineering

Data Engineering suite of 10 focused autonomous agents in Valkyrie AI Agent Studio.

## Engine Policy
- **Default:** `gemini-4-hydrogen` (`thinking_level: low`, `high` optional per agent)
- **Free-First Fallback:** `opencode_free` -> `openrouter_free` -> `ollama` (`qwen3.5:latest`)

## Focused Agents
- `01-etl-pipeline-designer` — **ETL Pipeline Designer**: Designs idempotent partition-aware ingestion DAGs with dead-letter queues. (Tool: `design_idempotent_dag`)
- `02-dbt-model-generator` — **dbt Model Generator**: Generates staging/mart SQL models and schema.yml not-null/unique tests. (Tool: `emit_dbt_model`)
- `03-schema-drift-detector` — **Schema Drift Detector**: Diffs upstream JSON/Avro schemas and flags breaking column removals. (Tool: `analyze_schema_drift`)
- `04-data-quality-guardian` — **Data Quality Guardian**: Defines freshness SLAs, row-count bounds, and referential checks. (Tool: `build_dq_assertions`)
- `05-warehouse-cost-tuner` — **Warehouse Cost Tuner**: Optimizes table partitioning, clustering keys, and slot autoscaling. (Tool: `recommend_clustering`)
- `06-lineage-documenter` — **Lineage Documenter**: Traces column-level provenance from raw ingestion to BI metrics. (Tool: `trace_column_lineage`)
- `07-pii-redaction-planner` — **PII Redaction Planner**: Detects email/SSN/IP columns and applies deterministic hashing policies. (Tool: `classify_pii_columns`)
- `08-backfill-orchestrator` — **Backfill Orchestrator**: Splits multi-year backfills into safe rate-limited date chunks. (Tool: `chunk_date_windows`)
- `09-streaming-lag-analyst` — **Streaming Lag Analyst**: Diagnoses Kafka consumer lag spikes, skew, and rebalance storms. (Tool: `diagnose_partition_skew`)
- `10-metric-layer-definer` — **Metric Layer Definer**: Standardizes canonical NRR, MRR, and active-user YAML definitions. (Tool: `define_semantic_metric`)
