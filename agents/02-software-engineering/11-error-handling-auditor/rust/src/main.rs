pub fn audit_error_paths(input: &str) -> String {
    format!("[audit_error_paths] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[11-error-handling-auditor:gemini-4-hydrogen:low] {}", audit_error_paths(input))
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
        assert!(out.contains("11-error-handling-auditor"));
        assert!(out.contains("audit_error_paths"));
    }
}
