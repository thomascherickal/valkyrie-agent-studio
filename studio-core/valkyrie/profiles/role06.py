"""Per-agent facets and keywords for the Security & AppSec agents (used by the generated Python versions)."""

# "<role_id>/<agent_id>": "facet one:kw,kw,kw|facet two:kw,kw,kw|facet three:kw,kw,kw"
PROFILES: dict[str, str] = {
    "06-security-appsec/01-threat-modeler": "spoofing:spoof,identity,impersonat,auth|tampering:tamper,modif,integrity,local|disclosure:disclos,leak,expose,api key|elevation:privilege,elevation,admin,fastapi",
    "06-security-appsec/02-sast-triage-analyst": "sinks:cwe-78,injection,subprocess,os.system|reachability:reachable,called,user input,request|dead code:dead,dev_script,unused,test|fixes:parameterized,sanitiz,escape,validated",
    "06-security-appsec/03-iam-least-privilege": "actions:action,getobject,putobject,wildcard|resources:resource,arn,bucket,prefix|principals:role,user,principal,analytics,service|conditions:condition,mfa,ip,tag,region",
    "06-security-appsec/04-secret-leak-scanner": "api keys:api_key,aizasy,sk-,key=|credentials:password,secret,credential,private key,bearer|entropy:entropy,random,base64,hex,dummy|rotation:rotate,revoke,rotation,expire,purge",
    "06-security-appsec/05-cve-impact-assessor": "vulnerable component:cve-,parser,library,package|reachability:invoked,unused,called,import|exploitability:exploit,rce,poc,remote,cvss|fix:upgrade,patch,fixed in,version,remove",
    "06-security-appsec/06-soc2-evidence-collector": "controls:cc6,cc7,cc8,control|ci evidence:ci,tests,pipeline,build,100%|approvals:approval,review,pr,merge,sign-off|backups:backup,restore,snapshot,retention,recovery",
    "06-security-appsec/07-auth-flow-reviewer": "pkce:pkce,code_challenge,code_verifier,s256|state and nonce:state,nonce,replay,redirect_uri|tokens:jwt,token,expire,refresh,access token|csrf:csrf,cookie,samesite,origin,xsrf",
    "06-security-appsec/08-container-hardener": "user:user,root,non-root,uid|image pinning:from,latest,digest,sha256|multi-stage:multi-stage,as builder,copy --from,build,slim|secrets and runtime:cmd,expose,healthcheck,env,add",
    "06-security-appsec/09-pentest-remediator": "access control:idor,authorization,org_id,missing,tenant|injection:injection,xss,sql,traversal,payload|poc:poc,get,post,request,/api|patch:check,parameterized,validate,filter,fix",
    "06-security-appsec/10-security-advisory-writer": "affected:affected,versions,v1.,before|fixed:patched,fixed,v1.4.2,upgrade|vulnerability:traversal,injection,cve,endpoint|mitigation:mitigation,workaround,disable,restrict",
    "06-security-appsec/11-api-security-reviewer": "authorization:authorization,owner,tenant,id,role|exposure:fields,excessive,sensitive,response,internal|abuse:rate,limit,pagination,bulk,enumerat|inventory:version,deprecated,undocumented,shadow,endpoint",
    "06-security-appsec/12-supply-chain-assessor": "dependencies:packages,transitive,maintainer,abandoned,pinned|build:build,action,ci,runner,pipeline|artifacts:image,signed,signature,sbom,provenance|response:advisory,patch,update,policy,scan",
    "06-security-appsec/13-forensics-guide": "scope:hosts,accounts,systems,affected,scope|evidence:logs,memory,disk,snapshot,image|timeline:utc,first,alert,detected,hours|handling:custody,hash,preserve,access,legal",
    "06-security-appsec/14-data-classification-advisor": "classes:public,internal,confidential,restricted,class|data types:email,payment,health,token,personal|controls:encrypt,access,mask,retention,logging|handling:share,export,vendor,backup,region",
    "06-security-appsec/15-vendor-security-reviewer": "data access:stores,access,customer,personal,emails|assurance:soc 2,iso,pen test,audit,report|operations:sla,incident,notify,breach,subprocessor|contract:dpa,liability,terms,termination,exit",
    "06-security-appsec/16-phishing-report-triager": "indicators:urgent,link,sender,domain,lookalike|exposure:clicked,entered,password,opened,attachment|spread:sent to,staff,recipients,forwarded,mailbox|response:reset,block,purge,report,takedown",
    "06-security-appsec/17-cloud-posture-reviewer": "exposure:public,bucket,open,0.0.0.0/0,internet|identity:root,mfa,role,admin,key|logging:cloudtrail,logging,audit,flow logs,regions|drift:drift,console,manual,terraform,baseline",
    "06-security-appsec/18-security-training-planner": "audiences:engineers,support,finance,staff,executives|topics:phishing,secure coding,data handling,passwords,mfa|measures:click rate,report rate,completion,incidents,quiz|delivery:short,monthly,workshop,simulation,onboarding",
    "06-security-appsec/19-crypto-usage-reviewer": "hashing:md5,sha1,hash,password,bcrypt|keys:key,hardcoded,secret,rotate,kms|randomness:random,token,seed,secure,predictable|modes:aes,ecb,gcm,iv,nonce",
    "06-security-appsec/20-bug-bounty-triager": "validity:reproduce,proof,poc,steps,valid|severity:xss,injection,rce,idor,impact|scope:in scope,out of scope,domain,asset,program|reward:reward,bounty,duplicate,payout,tier",
}
