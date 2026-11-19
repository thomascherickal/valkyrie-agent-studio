pub fn audit_test_pyramid(input: &str) -> String {
    format!("[audit_test_pyramid] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[16-test-pyramid-auditor:gemini-4-hydrogen:low] {}", audit_test_pyramid(input))
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
        assert!(out.contains("16-test-pyramid-auditor"));
        assert!(out.contains("audit_test_pyramid"));
    }
}
