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
}
