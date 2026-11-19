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
    "05-data-engineering/11-cdc-pipeline-designer": "source:postgres,mysql,table,wal,binlog|changes:insert,update,delete,change,per second|latency:minutes,latency,lag,fresh,seconds|consistency:order,duplicate,schema,snapshot,exactly",
    "05-data-engineering/12-data-contract-author": "schema:column,type,unique,row,field|semantics:meaning,definition,unit,cents,timezone|quality:null,freshness,unique,range,rows|ownership:owner,team,contact,sla,change",
    "05-data-engineering/13-partition-strategy-advisor": "table:table,rows,tb,size,events|query pattern:filter,where,last,days,customer|partition key:date,partition,key,column,daily|small files:small files,files,mb,compaction,skew",
    "05-data-engineering/14-dedup-strategy-designer": "exact duplicates:duplicate,event_id,retry,same,key|fuzzy matches:near,similar,name,email,fuzzy|window:window,hours,late,arrive,days|survivor:keep,latest,survivor,merge,golden",
    "05-data-engineering/15-scd-modeler": "changes:changes,tier,address,monthly,update|history:history,effective,at the time,as of,point in time|keys:surrogate,natural,key,id,business key|reports:report,revenue,fact,join,as-was",
    "05-data-engineering/16-dag-migration-planner": "jobs:jobs,cron,scripts,batch,schedule|dependencies:depends,after,hidden,upstream,chain|parity:compare,parity,output,diff,same|cutover:wave,cutover,parallel,rollback,switch",
    "05-data-engineering/17-feature-store-reviewer": "skew:training,serving,skew,recomputed,different|leakage:leak,future,label,point-in-time,as of|freshness:nightly,fresh,stale,refresh,latency|reuse:reuse,shared,owner,duplicate,catalog",
    "05-data-engineering/18-data-retention-planner": "datasets:clickstream,invoices,chats,logs,dataset|retention:years,forever,days,keep,delete|legal:law,gdpr,tax,required,regulation|cost:tb,storage,cost,archive,cold",
    "05-data-engineering/19-sql-style-reviewer": "readability:select,alias,cte,format,name|joins:join,where,on,cross,left|correctness:null,group by,distinct,count,date|performance:index,scan,order by,limit,star",
    "05-data-engineering/20-catalog-documenter": "description:table,row per,grain,one row,meaning|columns:column,mrr,id,type,field|lineage:source,upstream,derived,from,model|access:access,pii,owner,restricted,team",
}
