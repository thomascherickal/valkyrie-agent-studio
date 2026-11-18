pub fn audit_oauth_flow(input: &str) -> String {
    format!("[audit_oauth_flow] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[07-auth-flow-reviewer:gemini-4-hydrogen:low] {}", audit_oauth_flow(input))
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
        assert!(out.contains("07-auth-flow-reviewer"));
        assert!(out.contains("audit_oauth_flow"));
    }
}
