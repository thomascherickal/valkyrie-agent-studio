"""Per-agent facets and keywords for the C-Suite & Executives (CxOs) agents (used by the generated Python versions)."""

# "<role_id>/<agent_id>": "facet one:kw,kw,kw|facet two:kw,kw,kw|facet three:kw,kw,kw"
PROFILES: dict[str, str] = {
    "12-cxos/01-board-deck-synthesizer": "arr:arr,$4.8m,+22%,qoq,annual recurring|retention:nrr,118%,retention,churn,expansion|burn and runway:burn,runway,28 months,cash,months|milestones:milestone,launch,product,shipped,hired",
    "12-cxos/02-ma-diligence-reviewer": "ip:ip,patent,assignment,trade secret|oss licenses:gpl,gplv3,oss,license|security:security,breach,soc2,pentest,vulnerab|customer concentration:top customer,28%,concentration,arr,contract",
    "12-cxos/03-annual-operating-plan": "hiring:hires,+12,headcount,hiring,recruit|margin and cogs:gross margin,78%,cogs,cloud,cost|arr scenarios:arr,$9.5m,ending,base,upside|assumptions:assumption,driver,fy27,growth,scenario",
    "12-cxos/04-crisis-comms-strategist": "customers:customer,users,logins,affected|press:press,media,public,statement|internal:internal,employees,staff,all-hands|facts:outage,third-party,12%,eu",
    "12-cxos/05-ai-transformation-advisor": "volume:1200,tickets/wk,per week,weekly|roi:roi,savings,hours,automate,cost|compliance:legal,compliance,contract,redline,risk|workflows:triage,l1,support,workflow",
    "12-cxos/06-investor-update-writer": "wins:launched,shipped,won,milestone,closed|metrics:arr,mrr,users,growth,runway|asks:seeking,intros,ask,hire,help|challenges:challenge,risk,delay,churn,lost",
    "12-cxos/07-enterprise-deal-desk": "contract value:$250k,/yr,3-yr,acv,tcv|sla:99.99%,sla,uptime,credit,availability|discount:discount,25%,pricing,margin,price|legal terms:indemnity,liability,termination,security,dpa",
    "12-cxos/08-regulatory-horizon-watch": "eu ai act:eu ai act,high-risk,ai act,transparency|privacy:gdpr,dpa,personal data,consent|audit trails:audit trail,logging,human-in-the-loop,soc2|controls:control,roadmap,deadline,gap",
    "12-cxos/09-org-design-modeler": "span:managers,span,reports,4 managers|headcount:42 engineers,engineers,headcount,team size|platform:platform,shared,infrastructure,enabling|pods:pods,stream-aligned,product,squad",
    "12-cxos/10-ceo-weekly-brief": "sales:pipeline,$1.4m,deals,gtm,bookings|engineering:uptime,99.98%,incident,release,eng|finance:cash,burn,margin,revenue,budget|people:offers,hire,accepted,attrition,morale",
}
