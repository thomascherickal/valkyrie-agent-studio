"""Per-agent facets and keywords for the FinOps & Cloud Cost agents (used by the generated Python versions)."""

# "<role_id>/<agent_id>": "facet one:kw,kw,kw|facet two:kw,kw,kw|facet three:kw,kw,kw"
PROFILES: dict[str, str] = {
    "10-finops-cloud-cost/01-cloud-bill-anomaly": "spike:jumped,spike,increase,surge,from|service:nat gateway,ec2,s3,rds,service|region:us-east-1,eu-west-1,region,us-west|cost center:tag,cost-center,team,project,owner",
    "10-finops-cloud-cost/02-k8s-rightsizing-advisor": "cpu:vcpu,cpu,cores,millicores|memory:memory,ram,gib,mi,gi|requested vs actual:requests,p95 usage,usage,actual,limits|savings:waste,trim,reduce,savings,overprovision",
    "10-finops-cloud-cost/03-idle-resource-reaper": "idle volumes:unattached,ebs,volume,gp3|idle load balancers:alb,elb,load balancer,idle|zombie compute:zombie,vm,instance,stopped,ec2|storage size:tb,gb,snapshot,size,count",
    "10-finops-cloud-cost/04-ri-savings-planner": "baseline:steady,baseline,vcpu,stable|spend:on-demand,per month,/mo,spend|commitment:savings plan,1-year,no-upfront,reserved|coverage:coverage,utilization,discount,break-even",
    "10-finops-cloud-cost/05-llm-token-optimizer": "model tier:high-effort,low,gemini,model|price:$15,1m,per million,price|task type:classification,json,summary,simple,extraction|prompt bloat:prompt,tokens,verbose,context,trim",
    "10-finops-cloud-cost/06-egress-cost-reducer": "cross-az:cross-az,az,availability zone,chatty|vpc endpoints:endpoint,gateway,vpc,privatelink|data volume:tb/mo,tb,gb,traffic|destinations:s3,internet,region,dynamodb,cdn",
    "10-finops-cloud-cost/07-storage-tiering-planner": "age:older than,90 days,age,days|class:standard,intelligent-tiering,glacier,ia|volume:tb,gb,objects,size|lifecycle:lifecycle,expire,transition,retention",
    "10-finops-cloud-cost/08-unit-economics-tracker": "infra cost:infra,infrastructure,monthly,cloud,$3|llm cost:llm,tokens,model,api,$480|volume:runs,invocations,1.6m,per 1|tenants:tenants,customers,active,accounts",
    "10-finops-cloud-cost/09-budget-alert-router": "budget usage:budget,88%,spent,used|timing:day 14,forecast,month,projected,pace|owner:team,squad,owner,data-eng,manager|channel:slack,email,page,channel,notify",
    "10-finops-cloud-cost/10-finops-monthly-brief": "spend:total,$24.5k,spend,cost,bill|variance:mom,-9%,variance,vs,change|savings:savings,realized,$4.2k,saved,reduction|unit margin:margin,unit,per tenant,cogs,per run",
    "10-finops-cloud-cost/11-commitment-coverage-checker": "coverage:coverage,covered,commitment,on-demand,share|utilization:utilization,unused,wasted,committed,used|baseline:steady,baseline,stable,floor,minimum|term:term,year,flexible,convertible,expiry",
    "10-finops-cloud-cost/12-spot-instance-advisor": "workloads:batch,ci,etl,stateless,api|tolerance:interrupt,tolerate,checkpoint,retry,graceful|capacity:vcpu,instances,pool,diversif,zones|savings:discount,spot,on-demand,percent,saving",
    "10-finops-cloud-cost/13-cross-az-traffic-analyst": "traffic:traffic,tb,month,zone,region|sources:mesh,kafka,replication,database,job|placement:zone,az,locality,affinity,spread|cost:cost,per gb,transfer,egress,usd",
    "10-finops-cloud-cost/14-tagging-policy-auditor": "coverage:untagged,tagged,coverage,resources,percent|keys:owner,cost-center,environment,team,project|consistency:spelling,case,variant,prod,production|enforcement:policy,required,deny,automation,remediate",
    "10-finops-cloud-cost/15-chargeback-allocator": "shared costs:kubernetes,networking,observability,support,shared|drivers:usage,requests,cpu,traffic,headcount|teams:team,product,owner,consumer,unit|fairness:fair,explain,showback,chargeback,dispute",
    "10-finops-cloud-cost/16-database-cost-tuner": "sizing:cpu,memory,instance,size,utilization|storage:storage,iops,provisioned,gp3,gb|environments:dev,staging,idle,24/7,nights|backups:backup,retention,snapshot,days,copies",
    "10-finops-cloud-cost/17-observability-cost-reducer": "logs:logs,tb,month,debug,retention|metrics:series,cardinality,metrics,unused,labels|traces:traces,sampling,spans,100%,tail|bill:vendor,bill,usd,cost,commit",
    "10-finops-cloud-cost/18-forecast-variance-explainer": "variance:forecast,actual,over,variance,percent|drivers:traffic,volume,region,launch,migration|price effects:discount,rate,reservation,price,credit|one-offs:one-off,migration,incident,credit,refund",
    "10-finops-cloud-cost/19-saas-license-optimizer": "seats:seats,licences,licenses,users,active|activity:active,90 days,never,opened,login|tiers:tier,plan,enterprise,pro,downgrade|renewal:renewal,days,contract,notice,negotiate",
    "10-finops-cloud-cost/20-gpu-utilization-analyst": "utilization:utilization,percent,gpu,idle,average|queue:queue,wait,jobs,peak,hours|waste:idle,between jobs,over-provisioned,memory,small|scheduling:scheduler,packing,mig,share,preempt",
}
