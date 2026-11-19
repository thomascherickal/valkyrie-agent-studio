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
}
