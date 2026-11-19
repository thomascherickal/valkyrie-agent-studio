"""Per-agent facets and keywords for the Data Engineering agents (used by the generated Python versions)."""

# "<role_id>/<agent_id>": "facet one:kw,kw,kw|facet two:kw,kw,kw|facet three:kw,kw,kw"
PROFILES: dict[str, str] = {
    "05-data-engineering/01-etl-pipeline-designer": "source:webhook,api,stripe,source|schedule:hourly,daily,cron,schedule|idempotency:idempotent,dedupe,partition,upsert,merge|error handling:dead letter,retry,dlq,failure,alert",
    "05-data-engineering/02-dbt-model-generator": "staging:stg_,staging,source,rename|marts:mart,fct_,dim_,fact,dimension|tests:not null,unique,accepted_values,relationships,test|columns:_id,_cents,created_at,total,customer",
    "05-data-engineering/03-schema-drift-detector": "removed:removed,dropped,deleted,missing|added:added,new column,nullable,optional|type changes:type,changed,int,string|impact:breaking,downstream,consumers,required",
    "05-data-engineering/04-data-quality-guardian": "freshness:freshness,latest,stale,delay|volume:rows/day,row count,rows,volume|nulls:null,not null,0%,missing,blank|referential:foreign key,referential,orphan,unique,join",
    "05-data-engineering/05-warehouse-cost-tuner": "partitioning:partition,event_date,pruning,range,date|clustering:cluster,clustering,sort key,filter|scan size:tb,full scan,bytes,scan|slots:slot,autoscal,slots,flex",
    "05-data-engineering/06-lineage-documenter": "sources:raw,source,ingest,stg_,landing|transformations:derives,join,select,from,dim_,fct_|metrics:mart,metric,arr,bi,dashboard|columns:column,field,alias,sum(,as",
    "05-data-engineering/07-pii-redaction-planner": "direct identifiers:email,ssn,name,phone|network identifiers:ip,ip_address,device,cookie|quasi identifiers:zip,billing_zip,birth,address|safe fields:plan_id,id,status,count",
    "05-data-engineering/08-backfill-orchestrator": "date window:to,start,end,window|chunking:chunk,month,week,day,split|concurrency:concurrent,workers,parallel,max,pool|rate limits:rate limit,throttle,quota,per second,retry",
    "05-data-engineering/09-streaming-lag-analyst": "lag:lag,msgs,behind,offset|skew:partition,skew,hot key,uneven|rebalance:rebalance,rebalancing,group,join,session timeout|throughput:consumer,throughput,poll,slow,batch size",
    "05-data-engineering/10-metric-layer-definer": "retention:nrr,net revenue retention,churn,cohort|revenue:mrr,arr,revenue,subscription|activity:active user,dau,mau,wau|definition:trailing,12 months,window,filter",
}
