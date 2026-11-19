# Data Engineering

Data Engineering suite of 20 focused autonomous agents in Valkyrie AI Agent Studio.

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
- `11-cdc-pipeline-designer` — **CDC Pipeline Designer**: Designs change data capture pipelines from operational databases into the warehouse. (Tool: `design_cdc_flow`)
- `12-data-contract-author` — **Data Contract Author**: Drafts data contracts with schema, semantics, quality rules, ownership, and change process. (Tool: `draft_data_contract`)
- `13-partition-strategy-advisor` — **Partition Strategy Advisor**: Chooses partition keys, sizes, and pruning rules from table and query profiles. (Tool: `choose_partitioning`)
- `14-dedup-strategy-designer` — **Deduplication Strategy Designer**: Designs deduplication rules for events and records with keys, windows, and survivorship. (Tool: `design_dedup`)
- `15-scd-modeler` — **Slowly Changing Dimension Modeler**: Models slowly changing dimensions with type choice, keys, effective dates, and load logic. (Tool: `model_scd`)
- `16-dag-migration-planner` — **Orchestrator Migration Planner**: Plans migration of legacy jobs to a modern orchestrator with parity checks and cutover waves. (Tool: `plan_dag_migration`)
- `17-feature-store-reviewer` — **Feature Store Reviewer**: Reviews feature definitions for training and serving skew, leakage, freshness, and reuse. (Tool: `review_feature_store`)
- `18-data-retention-planner` — **Data Retention Planner**: Plans retention and deletion schedules by dataset class, purpose, law, and storage cost. (Tool: `plan_retention`)
- `19-sql-style-reviewer` — **SQL Style Reviewer**: Reviews SQL for readability, correctness traps, join risks, and maintainable structure. (Tool: `review_sql_style`)
- `20-catalog-documenter` — **Data Catalog Documenter**: Writes data catalog entries with definitions, lineage, quality status, and access guidance. (Tool: `document_dataset`)
