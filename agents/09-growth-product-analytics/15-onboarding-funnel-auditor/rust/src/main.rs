pub fn audit_onboarding(input: &str) -> String {
    format!("[audit_onboarding] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[15-onboarding-funnel-auditor:gemini-4-hydrogen:low] {}", audit_onboarding(input))
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
        assert!(out.contains("15-onboarding-funnel-auditor"));
        assert!(out.contains("audit_onboarding"));
    }
}
