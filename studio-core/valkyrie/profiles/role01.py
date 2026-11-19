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
    "01-product-management/11-persona-builder": "behaviors:spend,use,track,workflow,routine|goals:want,need,goal,trying to,wish|pain points:frustrat,slow,manual,error,pain|context:team,company,tool,role,industry",
    "01-product-management/12-jtbd-mapper": "trigger:switched,after,when,because,event|job:need,hire,get done,try to,so that|outcome:faster,proof,reduce,avoid,confidence|alternatives:spreadsheet,manual,competitor,workaround,previously",
    "01-product-management/13-kano-classifier": "functional answers:happy,like,expect,would be|dysfunctional answers:unhappy,dislike,without,missing|categories:must-have,delighter,performance,indifferent|sample:respondents,survey,n=,responses",
    "01-product-management/14-north-star-designer": "value moment:value,aha,activation,first,outcome|candidate metrics:weekly,active,count,per week,rate|inputs:breadth,depth,frequency,efficiency|guardrails:quality,churn,latency,support",
    "01-product-management/15-opportunity-tree-builder": "outcome:outcome,retention,increase,raise,target|opportunities:setup,hard,customers say,need,problem|solutions:feature,idea,build,solution,option|experiments:test,experiment,prototype,assumption,validate",
    "01-product-management/16-beta-program-manager": "cohort:accounts,customers,cohort,invite,select|feedback:feedback,survey,interview,issues,weekly|exit gate:go,no-go,criteria,threshold,ready|risks:bug,data,support,rollback,churn",
    "01-product-management/17-sunset-planner": "usage:accounts,runs,weekly,usage,active|replacement:replaced,alternative,migrate,successor,new|notice:notice,announce,deprecate,date,email|cost:maintenance,cost,support,engineer,hours",
    "01-product-management/18-pmf-survey-analyst": "very disappointed:very disappointed,would miss,cannot live,essential|segments:agency,enterprise,startup,segment,role|benefits:benefit,main value,love,favorite,because|improvements:improve,missing,wish,alternative,would add",
    "01-product-management/19-build-buy-evaluator": "build:build,in-house,engineer,months,own|buy:vendor,license,per year,quote,subscription|risk:risk,lock-in,security,compliance,outage|fit:core,differentiat,strategic,roadmap,standard",
    "01-product-management/20-product-ops-cadence-planner": "meetings:weekly,review,sync,standup,planning|reporting:report,dashboard,metrics,update,digest|decisions:decide,decision,approve,owner,escalate|pain points:long,surprise,late,duplicate,unclear",
}
