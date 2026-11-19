pub fn plan_lifecycle_emails(input: &str) -> String {
    format!("[plan_lifecycle_emails] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[11-lifecycle-email-planner:gemini-4-hydrogen:low] {}", plan_lifecycle_emails(input))
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
        assert!(out.contains("11-lifecycle-email-planner"));
        assert!(out.contains("plan_lifecycle_emails"));
    }
}
