"""Per-agent facets and keywords for the Technical Support agents (used by the generated Python versions)."""

# "<role_id>/<agent_id>": "facet one:kw,kw,kw|facet two:kw,kw,kw|facet three:kw,kw,kw"
PROFILES: dict[str, str] = {
    "07-technical-support/01-ticket-triager": "urgency:down,urgent,prod,outage,asap|product module:saml,sso,api,billing,deploy|sla tier:enterprise,sla,premium,free,pro|issue type:mismatch,error,bug,how do i,feature request",
    "07-technical-support/02-log-bundle-analyzer": "errors:error,exception,fatal,traceback,connectionreset|timestamps:2026-,utc,timestamp,at|upstream:upstream,gateway,502,503|warnings:warn,retry,deprecated,slow",
    "07-technical-support/03-escalation-packager": "environment:ubuntu,windows,macos,v2.|identifiers:trace_id,tr_,ticket,request id|repro steps:steps,reproduce,when,click,run|evidence:logs,screenshot,trace,error,attached",
    "07-technical-support/04-kb-article-drafter": "symptom:error,cors,fails,blocked|cause:because,caused,origin,misconfig,missing|resolution:fixed,set,change,resolved,solution|verification:verify,confirm,restart,works,test",
    "07-technical-support/05-sla-breach-predictor": "priority:p1,p2,enterprise,priority|elapsed time:unassigned,22m,waiting,open for,age|deadline:sla,30m,first response,resolution,due|ownership:assignee,owner,queue,agent",
    "07-technical-support/06-config-validator": "syntax:syntax,indent,colon,yaml,tab,quote|enum values:enum,invalid,thinking_level,allowed,ultra|required fields:required,missing,name,tools,id|types:type,string,int,list,bool",
    "07-technical-support/07-api-error-explainer": "status:400,401,403,404,429,500,502|reason:exhausted,invalid_argument,unauthorized,forbidden|quota:quota,free tier,limit,rate,429s|fix:retry,upgrade,key,backoff,wait",
    "07-technical-support/08-onboarding-concierge": "team size:50-person,org,team,engineers|integrations:github,okta,sso,slack|tech stack:rust,python,microservices,kubernetes|setup goals:deploy,first agent,workspace,checklist",
    "07-technical-support/09-churn-signal-spotter": "escalations:escalation,escalated,3rd,repeat|sentiment:frustrated,angry,disappointed,unhappy|renewal:renewal,contract,expires,21d|recurring:rate-limit,errors,same issue,still",
    "07-technical-support/10-status-page-updater": "status:investigating,identified,monitoring,resolved|impact:elevated latency,degraded,errors,unavailable|scope:us-west,eu,region,router|next:next update,eta,update in,fix",
    "07-technical-support/11-refund-policy-checker": "timing:days ago,bought,purchase,window,renewal|usage:logins,used,usage,active,never|reason:never worked,bug,mistake,charged twice,cancel|amount:annual,plan,refund,full,partial",
    "07-technical-support/12-support-reply-drafter": "problem:stopped,not working,error,since,stuck|impact:production,orders,customers,urgent,blocked|history:second,no reply,waiting,hours,again|tone:sorry,thanks,frustrated,please,apolog",
    "07-technical-support/13-duplicate-ticket-merger": "symptoms:login,loop,error,crash,fails|environment:ios,android,version,release,browser|reporters:company,same,customer,account,user|links:error code,ticket,duplicate,related,linked",
    "07-technical-support/14-outage-comms-writer": "impact:errors,affected,percent,customers,checkout|time:utc,since,started,investigating,update|cause:cause,identified,investigating,fix,mitigat|workaround:workaround,retry,use,avoid,temporary",
    "07-technical-support/15-macro-curator": "usage:used,times,per month,unused,year|quality:csat,reopen,outdated,wrong,tone|coverage:topics,gap,missing,new,issue|maintenance:owner,review,update,retire,version",
    "07-technical-support/16-csat-feedback-analyst": "scores:score,csat,rating,average,responses|negative themes:slow,repeated,rude,unhelpful,wait|positive themes:clear,quick,helpful,thanks,friendly|drivers:first reply,resolution,reopen,handoff,channel",
    "07-technical-support/17-known-issue-matcher": "symptoms:hangs,error,fails,slow,crash|conditions:rows,safari,release,version,only|matches:known issue,duplicate,linked,workaround,fixed|status:fix,eta,workaround,investigating,released",
    "07-technical-support/18-enterprise-response-planner": "account:arr,renewal,account,contract,enterprise|issues:severity,tickets,weeks,outage,incident|stakeholders:exec,sponsor,ceo,champion,owner|recovery:plan,credit,review,call,follow up",
    "07-technical-support/19-support-capacity-planner": "volume:tickets,week,volume,growth,peak|handling:minutes,handle time,average,aht,reply|capacity:agents,shrinkage,hours,utilisation,schedule|targets:sla,response,backlog,queue,target",
    "07-technical-support/20-bug-report-qualifier": "behaviour:wrong,shows,expected,actual,error|scope:customers,accounts,since,affected,only|evidence:screenshot,log,attached,steps,id|severity:tax,money,data loss,blocked,workaround",
}
