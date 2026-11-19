pub fn draft_budget_policy(input: &str) -> String {
    format!("[draft_budget_policy] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[20-error-budget-policy-writer:gemini-4-hydrogen:low] {}", draft_budget_policy(input))
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
        assert!(out.contains("20-error-budget-policy-writer"));
        assert!(out.contains("draft_budget_policy"));
    }
}
