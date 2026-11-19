pub fn write_security_tests(input: &str) -> String {
    format!("[write_security_tests] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[20-security-test-case-writer:gemini-4-hydrogen:low] {}", write_security_tests(input))
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
        assert!(out.contains("20-security-test-case-writer"));
        assert!(out.contains("write_security_tests"));
    }
}
