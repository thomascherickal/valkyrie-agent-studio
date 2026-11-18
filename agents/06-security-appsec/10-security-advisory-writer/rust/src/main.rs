pub fn format_advisory_md(input: &str) -> String {
    format!("[format_advisory_md] {}", input.trim())
}

pub fn run_agent(input: &str) -> String {
    format!("[10-security-advisory-writer:gemini-4-hydrogen:low] {}", format_advisory_md(input))
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
        assert!(out.contains("10-security-advisory-writer"));
        assert!(out.contains("format_advisory_md"));
    }
}
