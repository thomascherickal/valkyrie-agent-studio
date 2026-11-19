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
    "09-growth-product-analytics/11-lifecycle-email-planner": "triggers:signup,trial,invite,inactive,upgrade|timing:day,hour,after,delay,days|goal:activation,retention,upgrade,setup,invite|measures:open,click,conversion,unsubscribe,holdout",
    "09-growth-product-analytics/12-ltv-cac-modeler": "revenue:arpa,revenue,price,per month,mrr|margin:margin,gross,cogs,cost,78|churn:churn,monthly,retention,lifetime,cancel|acquisition:cac,payback,blended,spend,months",
    "09-growth-product-analytics/13-experiment-backlog-ranker": "ideas:idea,test,form,banner,checklist|impact:lift,impact,conversion,revenue,expected|effort:effort,days,engineering,design,weeks|traffic:visitors,week,traffic,sample,runtime",
    "09-growth-product-analytics/14-referral-program-designer": "audience:accounts,users,teams,peers,customers|reward:credit,reward,both sides,discount,cash|trigger:invite,referral,share,moment,after|economics:cac,cost,payback,conversion,fraud",
    "09-growth-product-analytics/15-onboarding-funnel-auditor": "steps:signup,verify,create,invite,connect|dropoff:drop,loses,percent,abandon,stuck|time to value:first report,time,minutes,value,aha|friction:required,form,permission,wait,error",
    "09-growth-product-analytics/16-segment-discovery-analyst": "clusters:cluster,segment,group,pattern,users|behaviour:api,dashboard,export,sessions,usage|value:retention,revenue,arpa,paid,churn|action:target,onboard,pricing,message,product",
    "09-growth-product-analytics/17-pricing-page-reviewer": "plans:plan,starter,team,business,tier|clarity:limits,included,tooltip,hidden,features|conversion:cta,toggle,annual,trial,button|objections:faq,security,cancel,refund,support",
    "09-growth-product-analytics/18-pipeline-forecaster": "stages:proposal,negotiation,discovery,stage,closing|conversion:conversion,win rate,historical,close,percent|age:older,days,stale,aging,slipped|risk:risk,slip,discount,champion,competitor",
    "09-growth-product-analytics/19-event-taxonomy-auditor": "naming:signup,sign_up,snake_case,camel,name|duplicates:duplicate,upgrade,same,variant,legacy|properties:property,user_id,plan,context,attribute|governance:owner,schema,tracking plan,review,unused",
    "09-growth-product-analytics/20-win-loss-analyst": "outcomes:won,lost,deals,mid-market,rate|reasons:price,missing,slow,reason,decision|competitors:incumbent,competitor,versus,switched,named|actions:fix,sales,product,pricing,roadmap",
}
