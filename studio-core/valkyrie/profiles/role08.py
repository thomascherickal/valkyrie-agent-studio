"""Per-agent facets and keywords for the Developer Relations & Docs agents (used by the generated Python versions)."""

# "<role_id>/<agent_id>": "facet one:kw,kw,kw|facet two:kw,kw,kw|facet three:kw,kw,kw"
PROFILES: dict[str, str] = {
    "08-developer-relations-docs/01-quickstart-author": "prerequisites:install,requires,prerequisite,toolchain|steps:deploy,run,create,first|commands:cli,command,terminal,cargo|verification:verify,expected,output,success,works",
    "08-developer-relations-docs/02-api-reference-polisher": "curl:curl,http,post,header,-h|python:python,requests,httpx,import|typescript:typescript,fetch,axios,await,ts|parameters:param,body,endpoint,response,deploy",
    "08-developer-relations-docs/03-sdk-sample-generator": "python:python,pip,import,def,async|typescript:typescript,npm,const,interface,node|rust:rust,cargo,crate,tokio,fn|options:thinking,low,mode,model,gemini,invoke",
    "08-developer-relations-docs/04-changelog-curator": "breaking:moved,breaking,removed,replaced|deprecations:deprecat,sunset,legacy,end of life|migration:codemod,migrate,upgrade,rename|new:electron,vite,gui,added",
    "08-developer-relations-docs/05-community-qa-helper": "question:how do i,how to,can i,why|models and providers:openrouter,ollama,free models,gemini|answer steps:set,run,configure,env|links:docs,guide,discussion,link,issue",
    "08-developer-relations-docs/06-tutorial-video-scripter": "intro:intro,topic,today,overview|terminal commands:terminal,command,run,pymoo,cli|demo:tuning,demo,every 3 runs,agent,show|recap:recap,summary,next,takeaway,wrap",
    "08-developer-relations-docs/07-docs-freshness-checker": "routes:/run-agent,/api/,route,endpoint|cli flags:flag,--,cli,option|mismatch:docs say,instead,outdated,differs,vs|code source:api_server.py,code,source,function",
    "08-developer-relations-docs/08-cfp-abstract-writer": "problem:problem,pain,challenge,gil|approach:compiling,tokio,approach,transpil|takeaways:takeaway,learn,attendees,lessons|audience:audience,beginner,advanced,engineers",
    "08-developer-relations-docs/09-hackathon-kit-builder": "theme:theme,build,finops,automated|starter prompts:prompt,starter,template,example|datasets:dataset,data,csv,sample|judging:judging,rubric,score,criteria,hours",
    "08-developer-relations-docs/10-dev-survey-analyst": "pain points:pain,difficult,toolchain,slow|delights:delight,love,1-click,easy|onboarding:onboarding,setup,install,getting started|docs and sdk:docs,sdk,examples,reference",
    "08-developer-relations-docs/11-migration-guide-writer": "changes:rename,remove,drop,change,deprecate|code:before,after,example,snippet,call|steps:step,upgrade,order,first,then|support:version,python,support,end of life,deadline",
    "08-developer-relations-docs/12-error-reference-writer": "codes:code,e1042,error,status,429|causes:cause,because,when,limit,mismatch|fixes:fix,retry,check,header,regenerate|examples:example,request,response,json,curl",
    "08-developer-relations-docs/13-api-example-tester": "examples:example,snippet,code,language,sample|failures:broken,fails,error,outdated,renamed|automation:ci,test,run,sandbox,schedule|maintenance:owner,update,release,sdk,version",
    "08-developer-relations-docs/14-docs-ia-reviewer": "structure:pages,sections,navigation,top-level,depth|naming:overview,intro,title,name,label|paths:click,from,quickstart,search,link|types:tutorial,guide,reference,concept,how-to",
    "08-developer-relations-docs/15-devrel-metrics-reporter": "reach:visits,views,subscribers,talks,members|activation:api keys,first call,signup,activated,quickstart|community:discord,members,questions,answered,contributors|content:docs,blog,video,tutorial,talk",
    "08-developer-relations-docs/16-tech-blog-outliner": "thesis:cut,how we,why,lesson,thesis|audience:engineers,readers,level,senior,beginner|evidence:benchmark,results,graph,p99,before|structure:section,intro,steps,conclusion,code",
    "08-developer-relations-docs/17-webinar-planner": "format:live,build,demo,minutes,speakers|audience:developers,registrants,level,target,attendees|promotion:email,social,invite,partner,registration|follow up:recording,replay,survey,resources,leads",
    "08-developer-relations-docs/18-sample-app-reviewer": "setup:clone,install,run,start,readme|security:key,secret,env,hard-coded,token|quality:test,error,comment,structure,example|maintenance:version,dependency,update,ci,node",
    "08-developer-relations-docs/19-contributing-guide-writer": "project:rust,cli,project,repo,language|workflow:fork,branch,pull request,review,merge|standards:test,lint,format,commit,style|community:maintainers,triage,conduct,issue,welcome",
    "08-developer-relations-docs/20-developer-journey-mapper": "stages:discover,evaluate,start,build,production|friction:wait,approval,confusing,error,review|channels:search,docs,community,support,sdk|measures:drop,time,first call,days,conversion",
}
