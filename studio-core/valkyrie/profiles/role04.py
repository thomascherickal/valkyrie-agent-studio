"""Per-agent facets and keywords for the QA & Test Automation agents (used by the generated Python versions)."""

# "<role_id>/<agent_id>": "facet one:kw,kw,kw|facet two:kw,kw,kw|facet three:kw,kw,kw"
PROFILES: dict[str, str] = {
    "04-qa-test-automation/01-test-plan-architect": "functional:login,flow,feature,auth,link|boundaries:ttl,expire,minutes,limit,max,min|security:security,token,replay,brute,phishing|risk:risk,critical,high,priority,impact",
    "04-qa-test-automation/02-edge-case-hunter": "numeric bounds:decimal,>0,zero,negative,max|text and unicode:string,unicode,emoji,empty,iso-4217|time:iso8601,timezone,dst,scheduled,date|nulls:null,optional,missing,blank,none",
    "04-qa-test-automation/03-playwright-scripter": "navigation:sign in,goto,open,navigate,page|actions:click,create,toggle,fill,deploy|locators:role,label,testid,text,locator|assertions:expect,visible,shows,should,verify",
    "04-qa-test-automation/04-flaky-test-triager": "timing:timeout,waiting,slow,sleep|race conditions:race,order,async,intermittent,concurrent|clock:clock,date,time,timezone,now|io and network:network,io,disk,port,connection",
    "04-qa-test-automation/05-api-fuzz-generator": "malformed:malformed,invalid json,truncated,unterminated|types:string,type,number,boolean|oversized:oversized,large,length,huge|injection:injection,script,sql,yaml",
    "04-qa-test-automation/06-coverage-gap-finder": "uncovered lines:uncovered,line,missing,not covered|branches:branch,else,if,elif|failure paths:error,exception,fallback,raise|test drafts:test,assert,mock,pytest,fixture",
    "04-qa-test-automation/07-regression-selector": "changed modules:changed,modified,.py,.ts|test mapping:test_,tests/,spec,suite|dependencies:import,depends,calls,module|risk areas:core,billing,auth,critical,shared",
    "04-qa-test-automation/08-accessibility-auditor": "landmarks:landmark,main,nav,header,footer|contrast:contrast,color,ratio,background,wcag|focus order:focus,tabindex,keyboard,tab,onclick|aria:aria,label,button,alt,role=",
    "04-qa-test-automation/09-load-test-modeler": "throughput:rps,requests,qps,throughput|latency thresholds:p95,p99,latency,ms|error budget:error rate,errors,0.1%,failure|ramp profile:ramp,users,vus,duration,soak,spike",
    "04-qa-test-automation/10-bug-repro-distiller": "steps:when,click,open,switch|environment:version,os,browser,windows|actual behavior:crash,error,freeze,fails,blank|expected behavior:expected,should,normally,used to,instead",
    "04-qa-test-automation/11-contract-test-designer": "consumer needs:consumer,consumes,fields,needs,uses|provider:provider,endpoint,service,returns,owner|compatibility:breaking,backward,optional,required,version|pipeline:ci,verify,pact,broker,deploy",
    "04-qa-test-automation/12-test-data-synthesizer": "schema:table,column,unique,foreign key,schema|constraints:not null,unique,check,range,fk|volume:rows,million,users,orders,scale|privacy:pii,email,mask,anonym,gdpr",
    "04-qa-test-automation/13-mutation-test-reviewer": "mutants:mutant,killed,survived,score,generated|survivors:survivor,boundary,rounding,operator,condition|tests:assert,test,case,coverage,missing|equivalent:equivalent,dead code,unreachable,noise,ignore",
    "04-qa-test-automation/14-visual-regression-triager": "diff types:diff,pixel,anti-aliasing,shift,colour|intended:intended,new design,button,redesign,approved|bugs:missing,broken,overlap,cut off,icon|stability:flaky,font,animation,render,browser",
    "04-qa-test-automation/15-device-matrix-planner": "platforms:ios,android,version,os,platform|devices:device,model,screen,top,samsung|coverage:coverage,share,percent,cover,users|capacity:lab,cloud,devices,hours,cost",
    "04-qa-test-automation/16-test-pyramid-auditor": "unit:unit,fast,minutes,isolated,mock|integration:integration,database,service,api,contract|end-to-end:end-to-end,browser,e2e,ui,flow|health:flaky,slow,duration,failure,pipeline",
    "04-qa-test-automation/17-exploratory-charter-writer": "mission:explore,investigate,mission,charter,discover|risks:risk,data loss,duplicate,limit,failure|areas:import,csv,email,report,upload|notes:notes,bug,question,observation,debrief",
    "04-qa-test-automation/18-qa-release-checklist-builder": "scope:release,tickets,change,feature,scope|risk:payment,migration,risk,critical,database|gates:gate,sign-off,approve,exit,criteria|rollback:rollback,flag,revert,monitor,plan",
    "04-qa-test-automation/19-l10n-test-planner": "locales:german,japanese,arabic,portuguese,locale|formats:date,currency,number,address,time zone|layout:expansion,right-to-left,rtl,truncat,font|content:translation,string,plural,hardcoded,context",
    "04-qa-test-automation/20-security-test-case-writer": "authentication:login,password,token,session,reset|authorization:permission,role,access,idor,owner|input:input,injection,validate,upload,parameter|abuse:rate,limit,brute force,enumeration,abuse",
}
