"""Per-agent facets and keywords for the Engineering & Product Management agents (used by the generated Python versions)."""

# "<role_id>/<agent_id>": "facet one:kw,kw,kw|facet two:kw,kw,kw|facet three:kw,kw,kw"
PROFILES: dict[str, str] = {
    "11-management/01-sprint-capacity-planner": "team:engineers,team,roster,people|time off:pto,holiday,vacation,leave,off|on-call:on-call,rotation,support,pager,interrupt|velocity:velocity,pts,points,story",
    "11-management/02-1on1-prep-assistant": "accomplishments:led,shipped,prs,rollout|blockers:blocked,blocker,stuck,permissions|growth:career,growth,promotion,skills,mentor|feedback:feedback,concern,morale,workload,praise",
    "11-management/03-okr-alignment-checker": "epics:epic,feature,story,project,theme|objectives:okr,okr1,objective,key result,goal|metrics:p99,latency,40%,cut,reduce|alignment:aligned,orphan,unmapped,supports,unrelated",
    "11-management/04-hiring-rubric-builder": "role level:senior,staff,junior,principal,level|skills:rust,python,systems,architecture,coding|signals:signal,evidence,example,depth,tradeoff|scoring:rubric,score,strong,bar,1-4",
    "11-management/05-perf-review-synthesizer": "strengths:strong,excellent,great,systems design|growth areas:can,delegate,improve,earlier|artifacts:shipped,pr,launch,project|peer feedback:peer,teammate,collaborat,feedback",
    "11-management/06-cross-team-dependency": "squads:ui team,core,squad,platform,team|deliverables:needs,/ws/traces,api,handoff,deliver|dates:nov 20,by,deadline,date,due|slips:slip,delay,late,behind,at risk",
    "11-management/07-meeting-action-extractor": "owners:alice,bob,to ship,to verify,owner|decisions:decided,agreed,approved,decision,go with|due dates:fri,by,monday,due,deadline|action items:action,todo,follow up,verify,ship",
    "11-management/08-tech-strategy-summarizer": "proposal:adopt,propose,universal,transpiler|scope:all 120,across,agents,teams,scope|tradeoffs:tradeoff,risk,cost,alternative,pro|decision:decision,approve,rollout,timeline,next",
    "11-management/09-team-health-pulse": "deploy frequency:deploy freq,daily,deploys,frequency|lead time:lead time,3h,commit to,cycle time|failure rate:cfr,change failure,2%,rollback|morale:morale,burnout,survey,happy,stress",
    "11-management/10-quarterly-roadmap-brief": "milestones:milestones,9/10,on track,delivered|confidence:confidence,rating,high,medium,low|risks:risk,behind,week behind,blocker,slip|asks:ask,need,decision,support,headcount",
    "11-management/11-delegation-coach": "tasks:report,negotiation,screens,review,draft|people:engineer,senior,junior,owner,growth|authority:decide,approve,recommend,inform,authority|risk:risk,deadline,quality,customer,visibility",
    "11-management/12-promotion-packet-builder": "impact:led,cut,shipped,migration,result|scope:teams,org,customers,scope,cross-team|growth:mentored,coached,rfc,wrote,taught|evidence:metrics,peer,feedback,quote,data",
    "11-management/13-conflict-mediation-guide": "parties:engineers,team,owner,disagree,between|history:reviews,since,weeks,escalat,incident|impact:concerns,delay,morale,blocked,work|resolution:agree,mediate,decide,boundary,follow up",
    "11-management/14-retro-facilitator": "went well:well,good,pairing,shipped,improved|problems:incident,wait,unclear,slow,blocked|actions:action,owner,due,follow,commit|history:last retro,done,not done,repeat,again",
    "11-management/15-headcount-justifier": "workload:load,on-call,hours,tickets,backlog|delivery:slipped,roadmap,quarter,delay,deadline|team:team of,engineers,attrition,people,capacity|request:requesting,hire,cost,salary,need",
    "11-management/16-first-90-days-planner": "role:manager,team,platform,lead,role|situation:incident,behind,morale,backlog,open|stakeholders:stakeholder,partner,peer,boss,customer|goals:learn,win,plan,goal,priority",
    "11-management/17-tradeoff-advisor": "requests:wants,request,ask,deal,upgrade|value:revenue,tickets,customers,deal,benefit|cost:weeks,effort,engineers,cost,days|risk:risk,deadline,security,end of life,breaking",
    "11-management/18-skip-level-prep-assistant": "signals:survey,engagement,dip,morale,signals|themes:priorities,unclear,decisions,slow,workload|trust:trust,safe,open,honest,feedback|follow up:follow up,action,promise,close,share",
    "11-management/19-blameless-review-facilitator": "timeline:push,down,minutes,alert,rollback|factors:missing,delayed,late,runbook,config|people:on-call,engineer,team,responded,decision|actions:action,fix,owner,prevent,follow up",
    "11-management/20-feedback-writer": "behaviour:interrupted,said,did,meeting,review|impact:stopped,missed,delayed,affected,result|request:next time,please,try,ask,could|context:tuesday,when,where,review,project",
}
