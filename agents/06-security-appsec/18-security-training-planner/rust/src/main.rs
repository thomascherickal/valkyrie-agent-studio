pub fn plan_security_training(input: &str) -> String {
    format!("[plan_security_training] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[18-security-training-planner:gemini-4-hydrogen:low] {}", plan_security_training(input))
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
        assert!(out.contains("18-security-training-planner"));
        assert!(out.contains("plan_security_training"));
    }
}
