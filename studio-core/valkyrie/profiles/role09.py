"""Per-agent facets and keywords for the Growth & Product Analytics agents (used by the generated Python versions)."""

# "<role_id>/<agent_id>": "facet one:kw,kw,kw|facet two:kw,kw,kw|facet three:kw,kw,kw"
PROFILES: dict[str, str] = {
    "09-growth-product-analytics/01-funnel-dropoff-analyst": "steps:visited,installed,firstrun,deployed,->|counts:1000,420,190,95,users|conversion:conversion,rate,%,percent,converted|dropoff:dropoff,drop,lost,biggest",
    "09-growth-product-analytics/02-cohort-retention-modeler": "day 1:d1,day 1,next day,day one|day 7:d7,day 7,week,7-day|day 30:d30,day 30,month,30-day|segments:cohort,channel,signup,oct,source",
    "09-growth-product-analytics/03-ab-test-interpreter": "significance:p=,p-value,significant,alpha|confidence interval:confidence,interval,ci,95%|sample ratio:srm,sample ratio,mismatch,n=|lift:control,variant,lift,uplift",
    "09-growth-product-analytics/04-activation-metric-finder": "early actions:run,sandbox,created,first|time window:48h,24h,first week,within|retention:retain,90-day,retention,returning|correlation:correlat,higher,3.1x,lift",
    "09-growth-product-analytics/05-pricing-elasticity-analyst": "paywall:paywall,custom python,pro,gate|conversion:upgrade,convert,conversion,paid|revenue:revenue,arpu,mrr,price|usage limits:5 agents,limit,cap,quota,seats",
    "09-growth-product-analytics/06-attribution-mapper": "first touch:first-touch,first touch,initial,origin|multi-touch:linear,multi-touch,touchpoints,assist|cac:cac,spend,cost,per signup|channels:github,search ads,oss,channel",
    "09-growth-product-analytics/07-seo-content-strategist": "keywords:keyword,rust,local llm,ollama|intent:how to,builder,tutorial,best|competition:competition,difficulty,docs,serp|clusters:cluster,topic,pillar,runtime",
    "09-growth-product-analytics/08-churn-cohort-explainer": "contraction:contraction,seat,downgrade,reduced|unused:never deployed,unused,never used,adoption|latency:latency,spike,slow,timeout|cohort:72%,churned,teams,accounts",
    "09-growth-product-analytics/09-plg-loop-designer": "sharing:share,link,blueprint,public,embed|preview:preview,card,svg,demo,og image|signup hook:signup,sign up,try,fork,import|viral loop:referral,invite,loop,organic,viral",
    "09-growth-product-analytics/10-exec-kpi-narrator": "growth:wau,wow,growth,+14%,mau|monetization:free-to-paid,4.8%,paid,mrr,revenue|speed:time-to-first-deploy,median,6m,minutes,latency|narrative:up,down,because,driver,vs",
}
