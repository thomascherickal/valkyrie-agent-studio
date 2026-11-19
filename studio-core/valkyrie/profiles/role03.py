"""Per-agent facets and keywords for the DevOps & SRE agents (used by the generated Python versions)."""

# "<role_id>/<agent_id>": "facet one:kw,kw,kw|facet two:kw,kw,kw|facet three:kw,kw,kw"
PROFILES: dict[str, str] = {
    "03-devops-sre/01-incident-commander": "severity:sev-1,sev-2,sev1,p1|impact:5xx,error rate,down,customers,users|trigger:deploy,release,config change,after,migration|mitigation:rollback,restart,failover,scale,disable",
    "03-devops-sre/02-postmortem-author": "timeline:at,utc,detected,started|root cause:oom,caused,because,unbounded|contributing factors:spike,promo,missing,no alert,lack of|remediation:fix,add,ticket,action item,monitor",
    "03-devops-sre/03-terraform-reviewer": "destructive:forces replacement,destroy,-/+,replace|iam wildcards:wildcard,admin,policy,full access|stateful:rds,database,volume,bucket|exposure:0.0.0.0/0,public,open,ingress",
    "03-devops-sre/04-k8s-manifest-linter": "probes:liveness,readiness,probe,startup|resources:resources,limits,requests,cpu|availability:replicas,pdb,disruption,affinity|security:privileged,runasroot,securityctx,latest",
    "03-devops-sre/05-slo-burn-monitor": "slo target:slo,99.9,99.95,objective,target|error rate:error rate,errors,failed,5xx,sli|budget:budget,remaining,consumed,burn|windows:1h,6h,24h,5m,window,multi-window",
    "03-devops-sre/06-ci-pipeline-optimizer": "serial steps:serial,sequential,needs,depends|caching:cache,sccache,restore-keys,miss|slow steps:npm install,cargo build,pytest,docker build|parallelism:matrix,parallel,shard,split",
    "03-devops-sre/07-capacity-planner": "traffic:qps,rps,requests,peak,traffic|utilization:cpu,memory,utilization,headroom|growth:forecast,growth,q4,projected,increase|scaling:nodes,replicas,instances,autoscal,scale out",
    "03-devops-sre/08-runbook-generator": "alert condition:for 5m,threshold,alert,rule|diagnosis:check,query,logs,kubectl,psql|mitigation:kill,restart,scale,increase,drain|rollback:rollback,revert,undo,restore,previous",
    "03-devops-sre/09-chaos-test-designer": "steady state:steady,baseline,normal,slo|fault injection:failover,kill,latency,partition|blast radius:blast,radius,percent,scope|abort conditions:abort,stop,rollback,threshold,halt",
    "03-devops-sre/10-rollback-verifier": "latency delta:p99,p95,latency,ms|error delta:error,5xx,failure,exception|baseline comparison:baseline,canary,vs,control,delta|rollback decision:rollback,promote,threshold,abort,hold",
    "03-devops-sre/11-oncall-load-analyzer": "volume:pages,alerts,per week,total,incidents|after hours:night,weekend,outside,hours,off-hours|distribution:engineers,rotation,share,top,person|actionability:actionable,noise,no action,auto-resolved,duplicate",
    "03-devops-sre/12-alert-noise-reducer": "alerts:alert,fired,times,rule,threshold|actions:actioned,action,led to,resolved,fix|duplicates:duplicate,flap,again,repeat,storm|tuning:threshold,for,duration,window,severity",
    "03-devops-sre/13-dr-plan-reviewer": "objectives:rto,rpo,recovery,objective,hours|backups:backup,snapshot,nightly,region,copy|testing:tested,drill,restore,exercise,last|dependencies:dns,identity,secrets,third party,dependency",
    "03-devops-sre/14-helm-chart-reviewer": "image:image,tag,latest,digest,pull|resources:resources,limits,requests,cpu,memory|availability:replica,pdb,disruption,affinity,probe|exposure:ingress,service,tls,public,network",
    "03-devops-sre/15-secret-rotation-planner": "age:older,year,months,age,expired|sharing:shared,several,services,reuse,copy|types:database,api key,certificate,token,password|ownership:owner,team,unknown,missing,rotation",
    "03-devops-sre/16-blast-radius-mapper": "dependency:calls,depends,upstream,downstream,service|fallbacks:cache,fallback,degrade,default,circuit|redundancy:region,replica,zone,single,failover|impact:users,revenue,customer,checkout,login",
    "03-devops-sre/17-deploy-freeze-advisor": "calendar:black friday,holiday,launch,event,week|queue:changes,queued,pending,release,deploys|budget:error budget,remaining,slo,left,burn|history:incidents,last week,rollback,failed,outage",
    "03-devops-sre/18-log-retention-tuner": "classes:audit,application,debug,access,security|retention:days,years,kept,retention,keep|volume:tb,gb,per month,volume,ingest|compliance:compliance,legal,regulation,pci,soc2",
    "03-devops-sre/19-dns-change-verifier": "records:cname,a record,mx,txt,record|ttl:ttl,seconds,cache,propagation,lower|cutover:cutover,switch,weight,canary,traffic|rollback:rollback,revert,old,previous,backup",
    "03-devops-sre/20-error-budget-policy-writer": "slo:slo,99.9,availability,target,objective|budget:budget,remaining,burn,consumed,minutes|actions:freeze,release,reliability,priority,policy|escalation:escalate,review,exec,owner,agree",
}
