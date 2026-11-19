pub fn review_api_security(input: &str) -> String {
    format!("[review_api_security] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[11-api-security-reviewer:gemini-4-hydrogen:low] {}", review_api_security(input))
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
        assert!(out.contains("11-api-security-reviewer"));
        assert!(out.contains("review_api_security"));
    }
}
