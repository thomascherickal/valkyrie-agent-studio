pub fn plan_enterprise_response(input: &str) -> String {
    format!("[plan_enterprise_response] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[18-enterprise-response-planner:gemini-4-hydrogen:low] {}", plan_enterprise_response(input))
}

fn main() {
    println!("{}", run_agent("sample"));
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_run() {
        let out = run_agent("verify");
        assert!(out.contains("18-enterprise-response-planner"));
        assert!(out.contains("plan_enterprise_response"));
    }
}
