"""Per-agent facets and keywords for the Product Management agents (used by the generated Python versions)."""

# "<role_id>/<agent_id>": "facet one:kw,kw,kw|facet two:kw,kw,kw|facet three:kw,kw,kw"
PROFILES: dict[str, str] = {
    "01-product-management/01-prd-architect": "goals:goal,objective,outcome,so that,enable,improve|non-goals:non-goal,out of scope,exclude,not include,later phase|acceptance criteria:accept,given,when,then,must,should,support",
    "01-product-management/02-roadmap-prioritizer": "reach:reach,users,accounts,customers|impact:impact,revenue,lift,massive|confidence:confidence,certain,evidence,0.8|effort:effort,person-months,weeks,sprints",
    "01-product-management/03-user-story-splitter": "actor:as a,as an,admin,user,customer|capability:want,manage,export,create,view,edit|acceptance:given,when,then,should,verify|size:epic,large,split,estimate,points",
    "01-product-management/04-competitive-intel": "competitor features:launched,released,added,introduced|pricing:pricing,usage-based,per seat,plan|compliance:soc2,gdpr,iso,hipaa|differentiation:unique,unlike,gap,parity",
    "01-product-management/05-voice-of-customer": "feature requests:requested,wish,add,want|pain points:times out,slow,crash,bug,error|sentiment:nps,love,hate,frustrated,great|churn risk:cancel,churn,switch,leave,competitor",
    "01-product-management/06-launch-readiness": "engineering:engineering,build,deploy,qa|docs:docs,documentation,guide,changelog|legal:legal,security,pentest,privacy|support:support,billing,sales,training",
    "01-product-management/07-pricing-modeler": "price:price,per seat,/seat,per month,tier|usage:tokens,included,usage,quota,overage,100k|cogs:cogs,cost,per 1k,infrastructure,compute|margin:margin,arpa,revenue,profit,discount",
    "01-product-management/08-experiment-designer": "hypothesis:hypothesis,lifts,increase,reduce|sample size:mde,sample,power,baseline|guardrails:guardrail,churn,latency,error rate|metrics:activation,d1,conversion,retention",
    "01-product-management/09-release-notes-writer": "features:feat,add,new,introduce,support|fixes:fix,bug,resolve,patch,race|breaking:breaking,remove,deprecate,drop,migrate|internal:chore,refactor,ci,test,docs",
    "01-product-management/10-stakeholder-brief": "shipped:shipped,released,launched,delivered,demo|kpis:kpi,latency,p99,wau,revenue|risks:risk,concern,delay,slip,at risk|blockers:blocker,blocked,waiting,dependency,escalat",
}
