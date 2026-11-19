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
}
