"""Per-agent facets and keywords for the Software Engineering agents (used by the generated Python versions)."""

# "<role_id>/<agent_id>": "facet one:kw,kw,kw|facet two:kw,kw,kw|facet three:kw,kw,kw"
PROFILES: dict[str, str] = {
    "02-software-engineering/01-architecture-reviewer": "spof:spof,no replica,single node,sole|coupling:coupling,shared db,synchronous,tight|backpressure:backpressure,queue,lag,buffer|durability:outbox,retry,idempotent,dlq",
    "02-software-engineering/02-pr-code-reviewer": "boundary bugs:off-by-one,boundary,index,empty|resource leaks:leak,unclosed,close,connection,file handle|performance:n+1,loop,query,slow|missing tests:test,coverage,untested,assert,mock",
    "02-software-engineering/03-refactor-planner": "size:loc,lines,monolith,large|callers:callers,imports,public,consumers|test coverage:tests,coverage,0%,untested|extraction steps:extract,strangler,facade,wrap,incremental",
    "02-software-engineering/04-api-contract-designer": "endpoints:get,post,put,delete|schema:field,type,string,integer|versioning:version,v1,v2,deprecate,backward|breaking changes:rename,remove,breaking,change type,optional",
    "02-software-engineering/05-sql-query-optimizer": "full scans:seq scan,select *,full scan,scan|indexes:index,composite,where,org_id,btree|sorting:order by,sort,limit,created_at,desc|joins:join,subquery,group by,exists,cte",
    "02-software-engineering/06-dependency-auditor": "unmaintained:unmaintained,abandoned,deprecated,old|license conflicts:gpl,agpl,license,copyleft|bloat:bloat,unused,large,duplicate|pinning:==,pinned,lockfile,version,>=",
    "02-software-engineering/07-migration-assistant": "expand:add column,expand,new column,backfill|contract:drop,contract,remove old,cleanup|rename:rename,alter,change type,split|downtime:downtime,lock,online,concurrently",
    "02-software-engineering/08-tech-debt-triager": "churn:churn,commits,changed,hot|complexity:complexity,cyclomatic,nested,legacy,tangled|bugs:bugs,defects,incidents,regressions,failures|cost:effort,days,quarter,risk,blocks",
    "02-software-engineering/09-concurrency-debugger": "lock order:lock,holds,mutex,deadlock|futures:await,future,unawaited,coroutine|races:race,shared,concurrent,check-then-act|starvation:starv,timeout,blocked,wait",
    "02-software-engineering/10-rust-port-advisor": "cpu hotspots:cpu,hotspot,% cpu,profile,cprofile|latency:p99,p95,ms,latency,slow|gil bound:gil,thread,parallel,cpu-bound,multiprocessing|port plan:pyo3,tokio,rust,crate,ffi",
    "02-software-engineering/11-error-handling-auditor": "swallowed errors:except,pass,ignore,swallow,catch|messages:message,log,context,raise,error|retries:retry,backoff,timeout,idempotent,attempt|fallbacks:fallback,default,paid,success,continue",
    "02-software-engineering/12-api-sunset-planner": "usage:calls,requests,clients,traffic,per day|replacement:v2,successor,migrate,replacement,new version|communication:notice,header,email,docs,deprecat|enforcement:brownout,sunset,shutdown,410,cutoff",
    "02-software-engineering/13-feature-flag-cleaner": "age:older,months,created,stale,days|rollout:100%,rollout,enabled,percent,ramp|ownership:owner,team,missing,unknown,assigned|risk:kill switch,experiment,permission,default,config",
    "02-software-engineering/14-module-boundary-checker": "cycles:imports,cycle,circular,depends,mutual|layers:layer,domain,infrastructure,ui,service|shared state:table,database,global,shared,singleton|public surface:public,api,interface,internal,export",
    "02-software-engineering/15-logging-quality-reviewer": "sensitive data:email,card,password,token,secret|structure:json,field,key,structured,format|levels:info,debug,warn,error,level|context:request id,trace,user id,correlation,here",
    "02-software-engineering/16-cache-strategy-advisor": "read pattern:reads,hit,hot,popular,per second|writes:writes,update,change,invalidate,per second|freshness:stale,ttl,fresh,expire,seconds|failure:stampede,miss,thundering,outage,fallback",
    "02-software-engineering/17-type-safety-planner": "current state:strict,any,untyped,types,lines|bugs:undefined,null,type error,bug,runtime|hotspots:api,boundary,shared,core,parse|ci gate:ci,lint,gate,baseline,ratchet",
    "02-software-engineering/18-idempotency-reviewer": "retries:retry,timeout,again,duplicate,resend|keys:key,idempotency,unique,header,token|storage:table,store,record,constraint,unique|consumers:webhook,queue,event,consumer,at-least-once",
    "02-software-engineering/19-code-owner-mapper": "authors:author,committer,commits,left,remaining|activity:months,last,recent,stale,no commits|concentration:percent,share,only,bus factor,single|review:review,approve,codeowners,team,owner",
    "02-software-engineering/20-codebase-onboarding-guide": "setup:setup,install,run,docker,env|architecture:service,module,folder,monorepo,layer|first task:first,starter,good first,ticket,issue|norms:review,branch,test,style,convention",
}
