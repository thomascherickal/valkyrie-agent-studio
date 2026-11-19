pub fn review_log_statements(input: &str) -> String {
    format!("[review_log_statements] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[15-logging-quality-reviewer:gemini-4-hydrogen:low] {}", review_log_statements(input))
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
        assert!(out.contains("15-logging-quality-reviewer"));
        assert!(out.contains("review_log_statements"));
    }
}
