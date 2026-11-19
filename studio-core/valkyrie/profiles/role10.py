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
}
